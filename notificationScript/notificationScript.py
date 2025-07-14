from dotenv import load_dotenv
import os
import time
import requests
from bs4 import BeautifulSoup
from plyer import notification
import smtplib
from email.message import EmailMessage

# Load environment variables from .env file
load_dotenv()

PRODUCT_URL = os.getenv("PRODUCT_URL")
TARGET_PRICE = float(os.getenv("TARGET_PRICE"))
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
TO_EMAIL = os.getenv("TO_EMAIL")

HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}

def send_email(subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = TO_EMAIL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def check_price():
    try:
        response = requests.get(PRODUCT_URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        # Try multiple ways to find the price
        price_tag = (
            soup.find(id="priceblock_ourprice") or
            soup.find(id="priceblock_dealprice") or
            soup.find(id="price_inside_buybox") or
            soup.find("span", {"class": "a-price-whole"})
        )

        if not price_tag:
            print("Price not found on page.")
            return False

        price_str = price_tag.get_text().strip()
        price_clean = ''.join(c for c in price_str if c.isdigit() or c == '.')
        price = float(price_clean)

        print(f"Current price: ${price:.2f}")

        if price <= TARGET_PRICE:
            print("Price is below target! Sending notification...")

            # Show desktop notification
            notification.notify(
                title="Amazon Price Alert!",
                message=f"Price dropped to ${price:.2f}!",
                timeout=10
            )

            # Send email
            send_email(
                "Amazon Price Alert!",
                f"The price dropped to ${price:.2f}!\nCheck it here: {PRODUCT_URL}"
            )

            return True
        else:
            print("Price is still too high.")
            return False

    except Exception as e:
        print("Error checking price:", e)
        return False

if __name__ == "__main__":
    while True:
        if check_price():
            break
        time.sleep(600)  # 10 minutes

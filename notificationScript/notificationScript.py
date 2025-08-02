from dotenv import load_dotenv
import os
import requests
from bs4 import BeautifulSoup
from email.message import EmailMessage
import smtplib

# Load environment variables
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
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = TO_EMAIL

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

def check_price():
    try:
        response = requests.get(PRODUCT_URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, "html.parser")

        price_tag = (
            soup.find(id="priceblock_ourprice")
            or soup.find(id="priceblock_dealprice")
            or soup.find(id="price_inside_buybox")
            or soup.find("span", {"class": "a-price-whole"})
        )

        if not price_tag:
            return "Price not found on page."

        price_str = price_tag.get_text().strip()
        price_clean = ''.join(c for c in price_str if c.isdigit() or c == '.')
        price = float(price_clean)

        if price <= TARGET_PRICE:
            send_email(
                "Amazon Price Alert!",
                f"The price dropped to ${price:.2f}!\nCheck it here: {PRODUCT_URL}"
            )
            return f"Price dropped to ${price:.2f}! Email sent!"
        else:
            return f"Price is still too high: ${price:.2f}"

    except Exception as e:
        return f"Error checking price: {e}"

def main():
    return check_price()

if __name__ == "__main__":
    print(main())

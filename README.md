Amazon Price Notifier
A simple Python app that checks the price of an Amazon product and sends you an email notification when the price drops below your target.

Features
Checks Amazon product price using web scraping

Sends email alerts via Gmail SMTP when price drops below target

Simple Flask web interface to manually trigger price checks

Easily configurable via environment variables

Setup
1. Clone the repo
bash
Copy
Edit
git clone https://github.com/mohamedwaked05/PriceNotifierScript.git
cd PriceNotifierScript/notificationScript
2. Create a .env file
Create a .env file in the notificationScript folder with the following variables:

env
Copy
Edit
PRODUCT_URL=https://www.amazon.com/your-product-url
TARGET_PRICE=100.00
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password
TO_EMAIL=recipient-email@gmail.com
Replace PRODUCT_URL with the full Amazon product URL.

Set TARGET_PRICE to your desired price threshold.

Use your Gmail email and an App Password for EMAIL_PASSWORD.

TO_EMAIL is the recipient email for notifications.

3. Install dependencies
Use pip to install required libraries:

bash
Copy
Edit
pip install -r requirements.txt
4. Run the Flask app
Start the web app:

bash
Copy
Edit
python app.py
Open http://localhost:8000 in your browser and click the "Run Price Check" button.

How it works
The script scrapes the Amazon product page to find the current price.

If the price is at or below the target, it sends you an email notification.

The Flask web app lets you trigger the price check manually and view the result.

Notes
You must enable 2-Step Verification on your Gmail account and generate an App Password to use Gmail SMTP.

The app uses web scraping, so if Amazon changes their page structure, price detection might break and require updates.

License
MIT License © Mohamed Waked


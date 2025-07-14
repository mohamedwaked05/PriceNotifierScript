# Amazon Price Notifier

A simple Python script that monitors the price of an Amazon product and sends you an email alert when the price drops below your target.

## Features

- Checks the price of any Amazon product by scraping its webpage.
- Sends email notifications when the price is below your specified target.
- Runs periodically (every 10 minutes by default).
- Easy to configure with environment variables.
- Can be deployed on free hosting services like Replit for 24/7 monitoring.

## Requirements

- Python 3.7 or higher
- Packages: `requests`, `beautifulsoup4`, `python-dotenv`, `plyer` (optional for desktop notifications)
- A Gmail account with an [App Password](https://support.google.com/accounts/answer/185833) for sending emails securely

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/amazon-price-notifier.git
cd amazon-price-notifier

# Price Notifier Script 💰📉

![Python](https://img.shields.io/badge/python-3.13+-blue?logo=python)
![Flask](https://img.shields.io/badge/flask-2.0+-lightgrey?logo=flask)
![License](https://img.shields.io/badge/license-MIT-green)

A Python-based price tracking and notification tool that monitors product prices and alerts you when they drop below your target.

![Demo](https://img.shields.io/badge/demo-live-success) → [https://pricenotifierscript.onrender.com](https://pricenotifierscript.onrender.com)

## Features ✨

- 📊 Track prices of products from Amazon (and potentially other sites)
- 🔔 Send notifications when price drops below a set target
- 🌐 Flask-based web interface with `/run` endpoint to trigger checks
- ⚙️ Easy environment variable configuration with `.env`
- 🚀 Simple deployment ready (tested on Render.com)

## Getting Started 🚀

### Prerequisites

- Python 3.13+
- pip package manager
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
### Installation

1. Clone the repository:
bash
git clone https://github.com/mohamedwaked05/PriceNotifierScript.git 
cd PriceNotifierScript
Create and activate a virtual environment (recommended):

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate    # Windows
Install dependencies:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bash
pip install -r requirements.txt
Create a .env file in the root folder and add your configuration:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

env
TARGET_PRICE=100.0
PRODUCT_URL=https://www.amazon.com/your-product-url
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-app-password
RECEIVER_EMAIL=receiver-email@example.com

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Usage 🖥️
Run the Flask app:

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

bash
python app.py
Visit http://localhost:8000/run to trigger a price check and notification.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Deployment ☁️
This app is ready to be deployed on platforms like Render.com.

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Remember to:

-Set your environment variables in your deployment platform

-Use the start command: python app.py

-Bind to the port your hosting service expects

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Contributing 🤝
Feel free to submit issues or pull requests!

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

License 📄
MIT License © Mohamed Waked






Price Notifier Script
A Python-based price tracking and notification tool that monitors product prices and alerts you when they drop below your target.

Features
Track prices of products from Amazon (and potentially other sites)

Send notifications when price drops below a set target

Flask-based web interface with /run endpoint to trigger checks

Easy environment variable configuration with .env

Simple deployment ready (tested on Render.com)

Demo
The app is live at: https://pricenotifierscript.onrender.com

Getting Started
Prerequisites
Python 3.13+

pip package manager

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/mohamedwaked05/PriceNotifierScript.git
cd PriceNotifierScript
Create and activate a virtual environment (recommended):

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Create a .env file in the root folder and add your configuration variables:

env
Copy
Edit
TARGET_PRICE=100.0
PRODUCT_URL=https://www.amazon.com/your-product-url
EMAIL_ADDRESS=your-email@example.com
EMAIL_PASSWORD=your-app-password
RECEIVER_EMAIL=receiver-email@example.com
Usage
Run the Flask app:

bash
Copy
Edit
python app.py
Visit http://localhost:8000/run to trigger a price check and notification.

Deployment
This app is ready to be deployed on platforms like Render.com.

Make sure to:

Set your environment variables in your deployment platform

Use the correct start command: python app.py

Bind to the port your hosting service expects

Contributing
Feel free to submit issues or pull requests!

License
MIT License © Mohamed Waked

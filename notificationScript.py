# Imports
# Loading environment  variables from .env 
from dotenv import load_dotenv
# Accesses system environment variables
import os
# Time
import time
# HTTP Requests
import requests
# Parses HTML content
from bs4 import BeautifulSoup
# Adds desktop notification
from plyer import notification
# Sends SMS via Twilio account
from twilio.rest import Client

# Loading environment variables from .env file
load_dotenv()

# Get the variables from the .env for messaging
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
messaging_service_sid = os.getenv("MESSAGING_SERVICE_SID")
my_number = os.getenv("MY_NUMBER")

# Function to send a text message using Twilio
def send_text_notification():
    # Twilio client with .env credentials
    client = Client(account_sid, auth_token)

    # Creates and sends message
    message = client.messages.create(
        body="COMP-2045 is now available! Go register before it's full!",
        messaging_service_sid=messaging_service_sid,
        to=my_number
    )
    
    # Print confirmation in terminal with message SID
    print("Twilio text sent! SID:", message.sid)

# Get Course info and webpage URL from .env
URL = os.getenv("COURSE_URL")
COURSE_CODE = os.getenv("COURSE_CODE")

# Adding headers to mimic a real browser (to avoid getting blocked)
HEADERS = {"User-Agent": "Mozilla/5.0"}

# Function to check if course is available
def check_course():
    try:
        # Send a GET request to the courses page
        response = requests.get(URL, headers=HEADERS)
        # Parse the HTML using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Extract all text only content from HTML
        page_text = soup.get_text()

        # Check if the course code is within the HTML text AND does not include the word "full" within 200 characters after
        if COURSE_CODE in page_text and "Full" not in page_text.split(COURSE_CODE)[1][:200]:
            print("COMP-2045 might be available! Sending notification...")
            
            # Show a desktop notification
            notification.notify(
                title="COMP-2045 is available!",
                message="Go sign up before it fills up again!",
                timeout=10
            )

            # Call the send text function to send a text message via Twilio
            send_text_notification()

            # Stop the loop
            return True
        else:
            # If its still full try the loop again - Show in terminal
            print("Still full... checking again soon.")
            return False
    # Handle errors    
    except Exception as e:
        print("Error during check:", e)
        return False

# Infinite loop to check every 10 minutes until course opens
while True:
    if check_course():
        break
    time.sleep(600)
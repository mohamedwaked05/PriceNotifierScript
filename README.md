# Course Availability Notifier

This Python script monitors a specific course (like "COMMST3029") and alerts you instantly when a spot opens up so you can register before it fills up again!

It works by checking the course site every 10 minutes, then sends a desktop notification and a text message when the course is available.

---

## Features

- Automatically checks the course availability in a loop
- Uses BeautifulSoup to parse the HTML and look for keywords
- Sends SMS notifications via Twilio
- Pops up a desktop notification with details
- Keeps your credentials secure in a .env file

---

## Requirements

- Python 3.7+
- [Twilio account](https://www.twilio.com/)
- Your public course registration URL

---

## Installation

1. **Clone this repository**
   ```bash
   git clone https://github.com/datababedev/CourseNotificationScript.git

2. **Install required packages**
   ```bash
   pip install -r requirements.txt

3. **Create a `.env` file**
   In the project root, create a file named `.env` and paste the following:

   ```env
   COURSE_URL=https://your-college-course-page.com
   COURSE_CODE=COMMST3029
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   MESSAGING_SERVICE_SID=your_messaging_service_sid
   MY_NUMBER=+12045551234
   ```

  ***Don’t share this file! It contains your private API keys and phone number.***

---

## How To Use
Run the script with:

```bash
python course_checker.py
```

You’ll see output like:

```bash
Still full... checking again soon.
Still full... checking again soon.
COMMST3029 might be available! Sending notification...
Twilio text sent! SID: SMxxxxxxxxxxxx
```
--- 
## How It Works

- The script sends a request to the course registration page using requests
- It uses BeautifulSoup to parse the HTML and search for your course code
- If the course code is found and doesn't say "Full" nearby:
  - It sends a desktop notification using plyer
  - It sends an SMS alert using Twilio
- The script runs every 10 minutes in a loop until the course becomes available

  ---
  ## How you can customize it
- Update your Course Code
- Change what the notifications say
- Add a testing feature to test if it works
- Change text notifications to emails or completely change it from SMS to discord or other notification servers
- Remove or update the desktop notifications
- Change the amount of time it takes to refresh the check

---

## FAQ

**Q: Can I use this for a different course?**  
A: Yes! Just change `COURSE_CODE` and `COURSE_URL` in your `.env` file.

**Q: Will this work if the course page is behind a login?**  
A: No, unfortunately the script can only access publicly available pages.

**Q: Can I get email alerts instead of SMS?**  
A: This version uses Twilio for SMS. You can modify it to use `smtplib` for email.

**Q: Can I run this script on a schedule in the background?**  
A: Yes! You can use Task Scheduler (Windows) or cron (Mac/Linux) to run it at intervals.

**Q: Can I use this without having my laptop running?**  
A: Not by default. This script runs *locally* on your computer, so it only works while your laptop is on and the script is running.

If you want it to run 24/7 without keeping your laptop open, you have a few options:
- Host it on a cloud server
- Use a Raspberry Pi or another device that stays on
- Deploy it on AWS Lambda or another serverless platform
**Let me know what you do!**

## Community
Join the Discussions to ask questions or suggest features!

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from datetime import datetime

# Load credentials from GitHub Secrets
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# Recipients
to_recipients = [
    "hfquery@motilaloswal.com"
]

cc_recipients = [
    "customercare@motilaloswal.com"
]

# Dynamic date
today = datetime.now().strftime("%d %b %Y")

# Subject
subject = f"URGENT: Foreclosure Letter Pending for Over 50 Days – Immediate Action Required ({today})"

# Email body
body = f"""
Dear Sir/Madam,

I am writing to formally escalate my request for the issuance of my Foreclosure Letter (FCL), which has been pending for more than 50 days despite multiple follow-ups.

I have already:
- Contacted my Bangalore branch manager multiple times with no resolution.
- Spoken to your customer support team last week, who acknowledged my request via email and assured that the payment link for the Foreclosure Letter would be shared shortly.

However, till date, no payment link or update has been provided.

This delay is unacceptable and is not in line with standard banking practices. Other banks provide foreclosure letters immediately upon request. The continued inaction is causing unnecessary financial and mental distress.

Please note that such prolonged delay constitutes a “deficiency in service” under applicable Consumer Protection laws. I request that this matter be treated with urgency to avoid further escalation.

I hereby request you to do one of the following on priority:
1. Share the payment link for issuance of the Foreclosure Letter immediately, OR
2. Confirm the exact date by which the Foreclosure Letter will be issued.

Relevant documents, including the sanction letter and account statement, have already been shared earlier for your reference.

Kindly confirm resolution within 48 hours of receipt of this email.

Regards,  
Akshay Narendra  
Mobile: 9620045087  
Email: abi.akshay8@gmail.com
"""

def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(to_recipients)
    msg["Cc"] = ", ".join(cc_recipients)
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    all_recipients = to_recipients + cc_recipients

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, all_recipients, msg.as_string())
        print("✅ Foreclosure escalation email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)

if __name__ == "__main__":
    send_email()
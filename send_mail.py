import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
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
    "customercare@motilaloswal.com",
    "grievances@motilaloswal.com",
    "query@motilaloswal.com",
    "IR.MOAlts@motilaloswal.com"
]


# Attachments (relative to repo root)
ATTACHMENTS = [
    "attachments/DOC-20251127-WA0004..pdf",
    "attachments/Image.jpeg"
]

# Dynamic date
today = datetime.now().strftime("%d %b %Y")

# Subject
subject = f"URGENT: Foreclosure Letter Pending for Over 50 Days – Immediate Action Required ({today})"

# Email body
body = """
Dear Sir/Madam,

    I am writing to formally escalate my request for the issuance of my Foreclosure Letter (FCL), which has been pending for more than 50 days despite multiple follow-ups.

    Loan Code : LXMOBANGAL5423-240681055
    Applicant Name : NARENDRAN KOTTINIGAL NARAYANAN

I have already:
- Contacted my Bangalore branch manager multiple times with no resolution.
- Spoken to your customer support team last week, who acknowledged my request via email and assured that the payment link for the Foreclosure Letter would be shared shortly.

However, till date, no payment link or update has been provided.

This delay is unacceptable and is not in line with standard banking practices. Other banks provide foreclosure letters immediately upon request. The continued inaction is causing unnecessary financial and mental distress.

Please note that such prolonged delay constitutes a “deficiency in service” under applicable Consumer Protection laws.

I request you to do one of the following immediately:
1. Share the payment link for issuance of the Foreclosure Letter, OR
2. Confirm the exact date by which the Foreclosure Letter will be issued.

Please find the sanction letter and supporting documents attached for your reference.

Kindly confirm resolution within 48 hours of receipt of this email.

Regards,  
Akshay Narendra  
Mobile: 9620045087  
Email: abi.akshay8@gmail.com

"""

def attach_files(msg, file_paths):
    for file_path in file_paths:
        if not os.path.exists(file_path):
            print(f"⚠️ Attachment not found, skipping: {file_path}")
            continue

        with open(file_path, "rb") as f:
            part = MIMEBase("application", "octet-stream")
            part.set_payload(f.read())

        encoders.encode_base64(part)
        filename = os.path.basename(file_path)

        part.add_header(
            "Content-Disposition",
            f'attachment; filename="{filename}"'
        )

        msg.attach(part)
        print(f"📎 Attached: {filename}")

def send_email():
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = ", ".join(to_recipients)
    msg["Cc"] = ", ".join(cc_recipients)
    msg["Subject"] = subject

    msg.attach(MIMEText(body, "plain"))

    # Attach files
    attach_files(msg, ATTACHMENTS)

    all_recipients = to_recipients + cc_recipients

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, all_recipients, msg.as_string())
        print("✅ Email sent successfully with attachments!")
    except Exception as e:
        print("❌ Error sending email:", e)

if __name__ == "__main__":
    send_email()
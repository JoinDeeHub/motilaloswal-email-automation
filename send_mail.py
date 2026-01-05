import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

# Load credentials from GitHub Secrets
EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

# Recipients
to_recipients = [
    "nodalofficer@pnbhousing.com",
    "cpc@rbi.org.in",
    "customercare@pnbhousing.com",
    "gro.south@pnbhousing.com",
    "gro.north@pnbhousing.com",
    "gro.west@pnbhousing.com",
    "executivedirector@pnbhousing.com"

]

cc_recipients = [
    "Girisha.hp@pnbhousing.com",
    "Manigandan.Ranganathan@pnbhousing.com",
    "durga.nair@pnbhousing.com",
    "nagesha.as@pnbhousing.com"
]

# Subject & Body
subject = "Request for Refund of EMI Payment Due to Delay in E-Katha Update"
body = """
Hi Sir/Madam,

The reason for this request is a significant delay beyond my control: The Karnataka Government's E-Katha portal remains non-functional and has not been updated, preventing me from obtaining the crucial E-Katha document required to complete the legal registration of the property financed by this loan. Consequently, the property registration process and associated formalities are stalled indefinitely.

As the property registration is incomplete and ownership cannot be formally transferred due to this administrative issue caused by the government portal, I believe the continued deduction of EMIs under these circumstances is unjustified. The delay stems entirely from external factors not attributable to me.

Therefore, I kindly request you to:

- Initiate a full refund of the EMI amount(s) deducted towards my Home Loan Account,
- For the period during which the E-Katha document remains unavailable, preventing registration.

Loan Account No: HOU/BLRS/0924/1308242XX

I trust you will recognize the exceptional nature of this situation caused by government system delays. I request your urgent attention to this matter and the processing of this refund without undue delay.

Please inform me promptly if any additional documentation or information is required from my end to facilitate this refund process.

Thank you for your time, understanding, and cooperation. I look forward to your positive resolution.

Sincerely,  
DEEPIKA NARENDRAN  

"""

def send_email():
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join(to_recipients)
    msg['Cc'] = ", ".join(cc_recipients)
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    all_recipients = to_recipients + cc_recipients

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, all_recipients, msg.as_string())
        print("✅ Email sent successfully!")
    except Exception as e:
        print("❌ Error sending email:", e)

if __name__ == "__main__":
    send_email()
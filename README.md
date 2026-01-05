
📧 Motilal Oswal Email Automation
=================================

Automated email escalation system using **Python + GitHub Actions** to send **scheduled, compliant, attachment-enabled emails** without UI automation or APIs.

This project is designed for **reliable, repeatable follow-ups** (e.g., foreclosure letter delays), ensuring timely escalation with supporting documents.

---

🚀 Features
-----------

- ✅ Fully automated email sending using GitHub Actions
- ⏰ Scheduled daily execution (cron-based)
- 📎 Supports **multiple attachments** (PDF, images, etc.)
- 🔐 Secure credentials via GitHub Secrets
- 🧪 Local + GitHub Actions tested
- ⚠️ Graceful handling of missing attachments
- 🧾 Audit-friendly logs

---

📁 Project Structure
--------------------

`. ├── attachments/ │   ├── DOC-20251127-WA0004..pdf │   └── Image.jpeg ├── motilaloswal-email-automation.drawio ├── README.md ├── requirements.txt └── send_mail.py`

---

🛠️ Tech Stack
---------------

- **Python 3**
- **SMTP (Gmail)**
- **GitHub Actions**
- **MIME Email Handling**

No APIs. No browser automation. No third-party services.

---

⚙️ Setup Instructions
-----------------------

### 1️⃣ Clone the Repository

`git clone https://github.com/<your-username>/motilaloswal-email-automation.git cd motilaloswal-email-automation`

---

### 2️⃣ Gmail Configuration (Required)

You must use a **Gmail App Password**.

Steps:

1. Enable **2-Step Verification** on your Google account
2. Generate an **App Password → Mail**
3. Save the 16-character password

---

### 3️⃣ Configure GitHub Secrets

Go to:

**Repository → Settings → Secrets and variables → Actions**

Add:

| Secret Name        | Description        |
| ------------------ | ------------------ |
| `EMAIL_ADDRESS`  | Sender Gmail ID    |
| `EMAIL_PASSWORD` | Gmail App Password |

⚠️ **Do not use your normal Gmail password**

---

▶️ Running Locally (Optional Test)
------------------------------------

`export EMAIL_ADDRESS="your_gmail@gmail.com" export EMAIL_PASSWORD="your_app_password" python send_mail.py`

Expected output:

`📎 Attached: DOC-20251127-WA0004..pdf 📎 Attached: Image.jpeg ✅ Email sent successfully with attachments!`

---

🤖 GitHub Actions Automation
----------------------------

### Workflow Trigger

- ⏰ **Daily at 11:11 AM IST**
- ▶️ Manual trigger supported (`workflow_dispatch`)

### Cron Used

`41 5 * * *`

(IST = UTC + 5:30)

---

📎 Attachment Handling
----------------------

- Attachments are read from the `attachments/` folder
- Supported formats: PDF, JPEG, PNG, etc.
- Missing files are skipped safely with warnings
- Gmail attachment size limit: ~25 MB

---

🔐 Security & Compliance
------------------------

- ❌ No credentials in code
- ❌ No browser automation
- ❌ No scraping
- ✅ Secrets managed by GitHub
- ✅ Read-only email access

Safe for **personal automation and escalation use**.

---

🧪 Tested Scenarios
-------------------

- ✔️ Local execution
- ✔️ GitHub Actions manual trigger
- ✔️ Scheduled cron run
- ✔️ Multiple attachments
- ✔️ Error handling (missing files)

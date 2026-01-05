# 📧 Automated Daily Email Sender (RBI/PNB Housing Complaint)

This repository automates the sending of a daily email to **PNB Housing Finance** & **RBI grievance officers** regarding *EMI refund due to E-Katha delays*.  
The script is scheduled to run automatically every day at **11:11 AM IST** using **GitHub Actions**.

---

## 📂 Repository Structure
<pre class="overflow-visible!" data-start="2408" data-end="2713"><div class="contain-inline-size rounded-2xl relative bg-token-sidebar-surface-primary"><div class="sticky top-9"><div class="absolute end-0 bottom-0 flex h-9 items-center pe-2"><div class="bg-token-bg-elevated-secondary -token--secondary flex items-center gap-4 rounded-sm px-2 font-sans -xs"></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="whitespace-pre!"><span><span>
├── send_email.py # Python script to build & send the email
├── requirements.txt # Python dependencies
├── .github/
│ └── workflows/
│ └── email.yml # GitHub Actions workflow (schedules the email daily)
└── README.md # Project documentation </span></span></code></div></div></pre>

---

## ⚙️ Setup

### 1️⃣ Clone the Repo  
git clone https://github.com/<your-username>/<repo-name>.git
cd <repo-name>



### 2️⃣ Gmail App Password  
- Enable **2FA** on your Gmail account.  
- Go to **Google Account → Security → App Passwords**.  
- Generate a **16-character App Password** for "Mail".  
- This will be used instead of your regular Gmail password.

### 3️⃣ Add GitHub Secrets  
In your GitHub repo:  
- Go to **Settings → Secrets and variables → Actions → New repository secret**  
- Add the following secrets:

| Secret Name    | Value                              |
|----------------|----------------------------------|
| EMAIL_ADDRESS  | [yourgmail@gmail.com](mailto:yourgmail@gmail.com)          |
| EMAIL_PASSWORD | your 16-character App Password   |

### 4️⃣ Dependencies (For Local Testing Only)  
If you want to test locally before automating:  
pip install -r requirements.txt
python send_email.py



---

## 🛠️ How It Works

**send_email.py**  
- Reads your email address + password from GitHub Secrets.  
- Builds the message with subject, body, recipients (To + Cc).  
- Connects to Gmail’s SMTP server and sends the email.  

**email.yml**  
- Runs daily at **11:11 AM IST (05:41 UTC)**.  
- Uses GitHub Actions runner with Python 3.x.  
- Executes `send_email.py`.

---

## 📅 Automation Schedule  

- The email will be sent automatically every day at:  
  **11:11 AM IST (05:41 UTC)**  
- Schedule can be modified inside `.github/workflows/email.yml`.

---

## 📧 Email Content

**Subject:**  
`Request for Refund of EMI Payment Due to Delay in E-Katha Update`

**Recipients (To):**  
- [example@pnbhousing.com](mailto:example@pnbhousing.com)  

**CC:**  
- [example@pnbhousing.com](mailto:example@pnbhousing.com)  

**Body:**  
- Includes details about **EMI refund request**  
- Reason: **E-Katha portal delay**  
- Loan Account No: **HOU/BLRS/0924/1308242**

---

## 🖥️ Local Testing Setup (Optional)

**If you want to run the script on your own machine before pushing:**  

Install dependencies:  
`pip install -r requirements.txt`



Add your email and password to your shell environment:  
- If you use Bash: open `~/.bashrc`  
- If you use Zsh: open `~/.zshrc`  

Add these lines:  
`export EMAIL_ADDRESS="yourgmail@gmail.com"`

`export EMAIL_PASSWORD="your-app-password"`



Reload the shell:  
`source ~/.bashrc` # or `source ~/.zshrc`



Run the script:  
`python send_email.py`



✅ Local environment variables are only for testing. GitHub Actions will still use Secrets for the real daily run.

---

## 🔧 Tools & Technologies Used

1. **Python 3**  
   Programming language used to write the automation script.  
   Modules used:  
   - `smtplib` → Connects to Gmail’s SMTP server.  
   - `email.mime` → Creates the email structure (subject, body, recipients, cc).  

2. **SMTP (Simple Mail Transfer Protocol)**  
   Standard protocol for sending emails.  
   The script connects to Gmail’s SMTP server (`smtp.gmail.com`, port 587) using TLS encryption.  

3. **Gmail App Passwords**  
   Secure 16-character password generated in your Google account.  
   Used for authentication instead of your real Gmail password.  
   Required since Gmail blocks “less secure apps”.  

4. **GitHub Actions (CI/CD)**  
   Automates the running of your script daily at 11:11 AM IST.  
   Uses a hosted Ubuntu runner to run your Python script in the cloud.  
   Workflow file (`.github/workflows/email.yml`) defines the schedule and steps.  

5. **GitHub Secrets**  
   Secure place to store sensitive credentials (`EMAIL_ADDRESS`, `EMAIL_PASSWORD`).  
   These are injected as environment variables during the GitHub Actions run.  

6. **Linux (Optional for Local Testing)**  
   If testing locally, environment variables can be added in `~/.bashrc` or `~/.zshrc`.  
   The script can be run with `python send_email.py` before pushing to GitHub.

---

## ⚙️ How the Project Works

### 🔄 Workflow Overview  
**Email Script (`send_email.py`):**  
- Loads Gmail ID & App Password from environment variables.  
- Prepares the email:  
  - Subject → EMI Refund Request.  
  - Body → Explains E-Katha issue and refund request.  
  - Recipients → PNB Housing Finance grievance team + RBI (To + Cc).  
- Connects to Gmail SMTP server using TLS.  
- Sends the email.  

**GitHub Actions (`email.yml`):**  
- Runs automatically every day at 11:11 AM IST (05:41 UTC).  
- Sets up Python on a GitHub-hosted Linux runner.  
- Passes Gmail ID & App Password from Secrets into the script.  
- Executes `send_email.py`.  

**GitHub Secrets:**  
- Protect Gmail credentials.  
- Inject them only at runtime (never stored in logs or repo).  

**Local Testing (Optional):**  
- Export environment variables in your Linux shell.  
- Run `python send_email.py` to verify before pushing to GitHub.

---

## ✅ Benefits

- No need to keep your laptop/server running.  
- Secure (secrets stored in GitHub).  
- Runs every day at the exact configured time.

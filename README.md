# 📧 AI Outreach Automation (Version 1)

An AI-powered email generation and automation system built using **LangChain**, **LCEL**, **Google Gemini**, and the **Gmail API**. Instead of manually generating an email, copying it into Gmail, and sending it, the application generates a professional email and securely sends it directly from the authenticated user's Gmail account using OAuth 2.0.

> 🚀 Version 1 focuses on building a complete end-to-end AI email automation pipeline.

---

## ✨ Features

- 🤖 AI-powered email generation using Google Gemini
- ⚡ LCEL (LangChain Expression Language) pipeline
- 📝 Prompt engineering with reusable templates
- 📦 Structured JSON output parsing
- 📧 Professional email formatting
- 🔒 Secure Gmail authentication using OAuth 2.0
- 📨 Direct email delivery using Gmail API
- 💻 Simple command-line interface

---

## 🛠️ Tech Stack

- Python
- LangChain
- LCEL (LangChain Expression Language)
- Google Gemini
-  Gmail API
- OAuth 2.0
- Google Cloud Console
---

## ⚙️ Project Workflow

```text
User Inputs
      │
      ▼
Prompt Template
      │
      ▼
Google Gemini
      │
      ▼
JSON Output Parser
      │
      ▼
EmailMessage (MIME)
      │
      ▼
Base64 Encoding
      │
      ▼
OAuth 2.0 Authentication
      │
      ▼
Gmail API
      │
      ▼
Email Successfully Delivered
```

---



---

## 🔐 Security

This project uses **OAuth 2.0** for secure Gmail authentication.

No Gmail password is stored or used.

The application only requests the permissions required to send emails.

---

## 🚀 Getting Started

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Outreach-Automation.git
cd AI-Outreach-Automation
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Create a `.env` file

```env
api_key=YOUR_GEMINI_API_KEY
```

### Configure Gmail API

- Create a project in Google Cloud Console
- Enable Gmail API
- Configure OAuth Consent Screen
- Create OAuth Client Credentials
- Download `credentials.json`
- Place it inside the project directory

### Run the application

```bash
python app.py
```

The first execution will open a browser window asking you to authenticate with your Google account.

After successful authentication, a `token.json` file will automatically be generated and reused for future executions.

---

## 💡 Why This Project?

Traditional workflow:

```
Open ChatGPT
↓

Generate Email
↓

Copy Email
↓

Open Gmail
↓

Paste Email
↓

Add Recipient
↓

Click Send
```

AI Outreach Automation:

```
Enter Details
↓

Generate Email
↓

Send Automatically
```

The goal is to reduce manual effort and create a seamless AI-powered email workflow.

---

## 🚀 Future Roadmap

### ✅ Version 1 (Completed)
- AI Email Generation
- LCEL Pipeline
- Gmail API Integration
- OAuth 2.0 Authentication
- Automatic Email Delivery
---

## 📖 What I Learned

This project helped me gain practical experience with:

- LangChain
- LCEL
- Prompt Engineering
- Structured AI Outputs
- JSON Output Parsing
- Gmail API
- OAuth 2.0
- Google Cloud Console
- MIME Email Creation
- Base64 Encoding
- API Integration

---

## 🌟 Version

**Current Release:** Version 1.0

> More exciting features and AI automation capabilities are coming soon.

---

## 👨‍💻 Author

**Fahad Syed**

If you found this project interesting, feel free to ⭐ the repository and follow my journey as I continue building AI-powered applications.

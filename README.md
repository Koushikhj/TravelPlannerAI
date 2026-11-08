# ✈️ TravelPlannerAI – AI-Powered Travel Planning Assistant

TravelPlannerAI is an AI-powered travel planning application that helps users generate personalized travel itineraries using **Google Gemini AI**, **n8n workflow automation**, and **Python Streamlit**.

The application combines Generative AI and workflow automation to simplify travel planning and provide AI-generated travel recommendations.

## 🚀 Features

- 🤖 **AI-Powered Planning:** Uses Google Gemini AI to generate travel itineraries.
- 🌍 **Personalized Travel Planning:** Generates travel plans based on user-provided trip details.
- ⚡ **Workflow Automation:** Uses n8n to automate the AI request and response process.
- 🔗 **API Integration:** Connects the Streamlit application with n8n through webhooks.
- 💻 **Interactive Interface:** Simple and user-friendly interface built with Streamlit.
- 📋 **AI-Generated Itineraries:** Provides structured travel recommendations.

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | User interface |
| n8n | Workflow automation |
| Google Gemini AI | AI-powered itinerary generation |
| Webhooks | Communication between application and n8n |
| REST APIs | API integration |

## 🏗️ Project Architecture

```text
          User
           |
           v
    Streamlit Frontend
           |
           v
      Python app.py
           |
           v
       n8n Webhook
           |
           v
     Google Gemini AI
           |
           v
    AI-Generated Response
           |
           v
    Streamlit Frontend
           |
           v
          User
```

## 📂 Project Structure

```text
TravelPlannerAI/
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Koushikhj/TravelPlannerAI.git
```

### 2. Navigate to the Project Directory

```bash
cd TravelPlannerAI
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

**Windows:**

```powershell
.\venv\Scripts\Activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure n8n

- Start your local n8n instance.
- Open the n8n workflow editor.
- Configure the Google Gemini API credentials.
- Set up the Gemini model node and webhook response.
- Activate your workflow.
- Configure the webhook URL in the Python application.

### 7. Run the Application

```bash
streamlit run app.py
```

Open your browser:

```text
http://localhost:8501
```

## 🔑 Prerequisites

- Python 3.x
- Node.js and npm
- n8n
- Google Gemini API key
- Required Python dependencies

**Important:** Never upload API keys, credentials, or `.env` files containing secrets to GitHub.

## 🎯 Project Objective

The main objective of TravelPlannerAI is to demonstrate how Generative AI, Python application development, API integration, and workflow automation can be combined to build an intelligent travel planning assistant.

## 👨‍💻 Developer

**Koushik HJ**

- GitHub: [@Koushikhj](https://github.com/Koushikhj)
- Project: [TravelPlannerAI](https://github.com/Koushikhj/TravelPlannerAI)

---

⭐ If you find this project interesting, consider giving the repository a star!

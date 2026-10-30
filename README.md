
#  Scam Message Investigator

##  Project Overview

Scam Message Investigator is an AI-powered application designed to analyze suspicious SMS messages, emails, and WhatsApp messages. It uses the Gemma 3 (1B) language model through Ollama to identify potential scam indicators and generate an investigation report.

The application helps users understand suspicious messages, recognize possible phishing attempts, and learn how to stay safe from online scams.

##  Objectives

- Analyze suspicious text messages using AI.
- Identify potential scam and phishing indicators.
- Classify messages based on their possible risk level.
- Explain suspicious words, links, and requests.
- Provide safety recommendations to users.
- Generate downloadable investigation reports.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Streamlit | Web application interface |
| Ollama | Runs the AI model locally |
| Gemma 3 (1B) | AI-based message analysis |
| Requests | Connects Python with Ollama API |

##  Project Structure

```text
Scam-Message-Investigator/
│
├── app.py
├── requirements.txt
└── README.md
```

##  Features

### 1. Message Input
Users can paste suspicious SMS, email, or WhatsApp messages into the application.

### 2. AI-Based Investigation
The Gemma 3 model analyzes the provided message and generates an investigation report.

### 3. Risk Level Classification
The application identifies a possible risk level:
- Low Risk
- Medium Risk
- High Risk

### 4. Warning Sign Detection
Highlights suspicious words, unknown links, urgent requests, and other possible warning signs.

### 5. Safety Recommendations
Provides suggestions to help users avoid potential online scams.

### 6. Download Report
Allows users to download the generated investigation report as a text file.

## Installation and Setup

### Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/Scam-Message-Investigator.git
```

### Step 2: Navigate to the Project Folder

```bash
cd Scam-Message-Investigator
```

### Step 3: Create a Virtual Environment

```bash
python -m venv venv
```

### Step 4: Activate the Virtual Environment

For Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### Step 5: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 6: Install Ollama

Download Ollama from:

https://ollama.com/download

### Step 7: Download the Gemma Model

```bash
ollama pull gemma3:1b
```

### Step 8: Run the Application

```bash
streamlit run app.py
```

The application will open in your web browser.

##  Application Workflow

1. User opens the Scam Message Investigator application.
2. User enters a suspicious message.
3. Streamlit sends the message to the Python backend.
4. Python sends the message to the Ollama API.
5. Gemma 3 analyzes the message.
6. The AI generates an investigation report.
7. The report is displayed on the application.
8. User can download the report.

##  Sample Input

```text
Congratulations! You have won a cash prize
of ₹50,000. Click this link immediately to
claim your reward. Your account will expire
in 24 hours.
```

##  Expected Output

The investigation report includes:

- Risk Level
- Message Type
- Warning Signs
- Explanation
- Recommended Actions

##  Safety and Limitations

- AI-generated results are preliminary assessments.
- The application does not independently verify URLs or sender identities.
- A message classified as low risk is not guaranteed to be safe.
- Users should never share passwords, OTPs, or banking details through suspicious links.
- Important financial or security messages should be verified through official channels.

##  Future Enhancements

- Add URL safety checking.
- Support image-based scam message detection using OCR.
- Add multilingual message analysis.
- Maintain investigation history.
- Improve risk classification accuracy.
- Add a more detailed investigation dashboard.



                                                            # 🧠 MindGuard AI

### Secure Crisis-Aware Mental Health Assistant

<p align="center">
  <img src="https://img.shields.io/badge/version-v1.0.0-blue" />
  <img src="https://img.shields.io/badge/backend-Flask-red" />
  <img src="https://img.shields.io/badge/database-PostgreSQL-blue" />
  <img src="https://img.shields.io/badge/authentication-Flask--Login-green" />
  <img src="https://img.shields.io/badge/AI-Llama%203.x-purple" />
  <img src="https://img.shields.io/badge/security-Zero--Trust-brightgreen" />
</p>

---

## 📌 Version

**v1.0.0 — Stable Release**

---

## 📑 Table of Contents

* [Overview](#-overview)
* [Why This Project Matters](#-why-this-project-matters)
* [Core Features](#-core-features)
* [System Architecture](#-system-architecture)
* [Database Schema](#-database-schema)
* [Technology Stack](#-technology-stack)
* [Installation](#-installation)
* [Environment Configuration](#-environment-configuration)
* [Running the Application](#-running-the-application)
* [Application Flow](#-application-flow)
* [Crisis Handling Strategy](#-crisis-handling-strategy)
* [Security Considerations](#-security-considerations)
* [Future Enhancements](#-future-enhancements)
* [Author](#-author)
* [Disclaimer](#-disclaimer)

---

## 📌 Overview

MindGuard AI is a privacy-focused, crisis-aware conversational AI system engineered to provide empathetic mental health support while enforcing strict security boundaries and responsible AI behavior.

Rather than functioning as a simple chatbot, the platform integrates structured risk detection, crisis override mechanisms, validated LLM outputs, and secure multi-user isolation to ensure that sensitive user conversations remain protected and context-aware.

The system combines:

* Secure authentication
* Persistent PostgreSQL-backed chat memory
* Emotion classification and risk scoring
* Controlled LLM integration
* Zero-trust conversation isolation

---

## 🎯 Why This Project Matters

Mental health AI systems must go beyond text generation. They require:

* Safety-aligned response handling
* Structured risk-awareness
* Privacy-centric user isolation
* Controlled AI output validation

MindGuard AI demonstrates how conversational AI can be engineered responsibly by combining backend security, relational database integrity, structured AI pipelines, and risk-aware design into a scalable architecture.

---

## 🚀 Core Features

### 🔐 Secure Authentication

* User registration & login (Flask-Login)
* Secure password hashing (Werkzeug)
* Session-based access control
* Conversation ownership enforcement

### 🧠 Risk-Aware Conversational AI

* Emotion classification (sadness, anxiety, fear, frustration, etc.)
* Risk scoring engine
* Crisis override protection layer
* Structured JSON validation of AI outputs
* Deterministic inference pipeline (controlled temperature)

### 🗄 Persistent Conversation Storage

* PostgreSQL relational schema
* User-to-conversation mapping
* Timestamp-based dynamic resurfacing
* Secure DB-level ownership filtering

### 🛡 Zero-Trust Architecture

* Route-level validation
* Database-level ownership filtering
* Defensive JSON parsing
* Controlled model fallback mechanism
* Environment-based configuration

---

## 🏗 System Architecture

```
User
  ↓
Flask Backend
  ↓
Crisis Risk Engine
  ↓
LLM Service (Llama 3.x via HuggingFace Router)
  ↓
Structured JSON Validation
  ↓
PostgreSQL Database
```

Every request is validated against the authenticated user before accessing conversation data, ensuring strict data isolation.

---

## 🗄 Database Schema

### Users

* id
* username
* password_hash
* created_at

### Conversations

* id
* user_id (Foreign Key → Users)
* created_at
* updated_at

### Messages

* id
* conversation_id (Foreign Key)
* sender (user / assistant)
* content
* emotion
* risk_score
* created_at

This schema ensures relational integrity, multi-user isolation, and clean separation of responsibilities.

---

## 🛠 Technology Stack

| Layer          | Technology                     |
| -------------- | ------------------------------ |
| Backend        | Flask                          |
| Authentication | Flask-Login                    |
| ORM            | Flask-SQLAlchemy               |
| Database       | PostgreSQL                     |
| AI Model       | Llama 3.x (HuggingFace Router) |
| Configuration  | python-dotenv                  |
| Frontend       | HTML, CSS, Vanilla JavaScript  |

---

## 📦 Installation

```bash
git clone https://github.com/imrcoder07/MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant.git
cd MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant

python -m venv venv
venv\Scripts\activate     # Windows
# OR
source venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

---

## ⚙ Environment Configuration

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql+psycopg2://postgres:your_password@localhost:5432/mental_health_ai
HF_TOKEN=your_huggingface_token
SECRET_KEY=your_secret_key
```

---

## ▶ Running the Application

```bash
python app.py
```

Open:

```
http://127.0.0.1:5000
```

---

## 🔎 Application Flow

1. User registers and authenticates securely.
2. A new conversation session is initiated.
3. Incoming messages are analyzed by the crisis risk engine.
4. A risk score is assigned.
5. If high risk:

   * LLM generation is bypassed.
   * Crisis support response is returned.
6. Otherwise:

   * Conversation history is structured.
   * Sent to LLM.
   * JSON response validated and sanitized.
7. Message and metadata stored in PostgreSQL.
8. Conversation timestamp updated for resurfacing logic.

---

## ⚠ Crisis Handling Strategy

MindGuard AI includes a dedicated safety layer that:

* Detects crisis-sensitive language
* Assigns structured risk levels
* Prevents unsafe model outputs
* Enforces controlled response templates

This ensures responsible AI behavior rather than blind generative output.

---

## 🔐 Security Considerations

* Secure password hashing
* Environment variable secret isolation
* Route-level conversation validation
* Database-level user isolation
* JSON output schema enforcement
* API failure fallback handling
* High-risk override protection

The system prioritizes privacy, responsible AI constraints, and secure multi-user interaction.

---

## 📈 Future Enhancements

* Emotion analytics dashboard
* User sentiment trends
* Admin monitoring tools
* Docker containerization
* CI/CD integration
* Audit logging system
* Model fine-tuning

---

## 👤 Author

**Islam**
B.Tech – Computer Science & Engineering
GitHub: [https://github.com/imrcoder07](https://github.com/imrcoder07)
LinkedIn: [https://linkedin.com/in/islam07](https://linkedin.com/in/islam07)

---

## ⭐ Support

If you find this project insightful or useful, consider giving it a ⭐ on GitHub.

---

## ⚠ Disclaimer

MindGuard AI provides AI-assisted conversational support and does not replace licensed medical or psychological professionals. For serious mental health concerns, consult qualified professionals or emergency services.




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

## 📌 Overview

**MindGuard AI** is a privacy-focused, crisis-aware conversational AI platform designed to provide empathetic mental health support while enforcing strict user isolation and responsible AI deployment principles.

The system combines:

* Secure user authentication
* PostgreSQL-backed persistent chat memory
* LLM-powered structured responses
* Crisis risk detection and override mechanisms
* Zero-trust multi-user architecture

Unlike basic chatbot demos, MindGuard AI implements layered safety controls and ownership validation to ensure responsible AI interaction within a secure SaaS-style backend.

---

## 🚀 Core Features

### 🔐 Secure Authentication

* User registration & login (Flask-Login)
* Password hashing (Werkzeug secure hashing)
* Session management with access control

### 🧠 Risk-Aware Conversational AI

* Emotion classification (sadness, anxiety, fear, etc.)
* Risk scoring engine
* Crisis override system for high-risk inputs
* Structured JSON validation of AI outputs
* Deterministic generation pipeline

### 🗄 Persistent Conversation Storage

* PostgreSQL relational schema
* Conversation-to-user mapping
* Timestamp-based conversation resurfacing
* Secure ownership validation at DB level

### 🛡 Zero-Trust Architecture

* Route-level conversation access validation
* Cross-user data isolation
* Controlled LLM integration
* Environment-based configuration (.env)

---

## 🏗 System Architecture

```
User
  ↓
Flask Backend
  ↓
Crisis Analysis Engine
  ↓
LLM Service (Llama 3.x via HuggingFace Router)
  ↓
Structured JSON Validation
  ↓
PostgreSQL Storage
```

Every request is validated against authenticated user ownership before accessing conversation data.

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

This structured schema ensures relational integrity and secure multi-user isolation.

---

## 🛠 Technology Stack

| Layer          | Technology                         |
| -------------- | ---------------------------------- |
| Backend        | Flask                              |
| Authentication | Flask-Login                        |
| ORM            | Flask-SQLAlchemy                   |
| Database       | PostgreSQL                         |
| AI Model       | Llama 3.x (via HuggingFace Router) |
| Configuration  | python-dotenv                      |
| Frontend       | HTML, CSS, Vanilla JavaScript      |

---

## 📦 Installation

```bash
git clone https://github.com/imrcoder07/MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant.git
cd MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant

python -m venv venv
venv\Scripts\activate   # Windows
# or
source venv/bin/activate  # Mac/Linux

pip install -r requirements.txt
```

---

## ⚙ Environment Configuration

Create a `.env` file in the root directory:

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

Visit:

```
http://127.0.0.1:5000
```

---

## 🔎 Application Flow

1. User registers and logs in.
2. A new conversation session is created.
3. User message is analyzed for crisis signals.
4. Risk score is computed.
5. If high risk:

   * Crisis override response is returned.
6. Otherwise:

   * Conversation history is structured.
   * Sent to LLM.
   * JSON response validated and cleaned.
7. Message stored securely in PostgreSQL.
8. Conversation updated for dynamic resurfacing.

---

## ⚠ Crisis Handling Strategy

MindGuard AI includes a dedicated crisis detection layer that:

* Evaluates emotional signals
* Assigns risk levels
* Prevents unsafe LLM responses
* Enforces controlled support replies

This ensures responsible AI behavior and safety alignment.

---

## 🔐 Security Considerations

* Password hashing using secure cryptographic methods
* Environment-variable secret isolation
* Strict conversation ownership validation
* No direct database exposure
* LLM output sanitation
* Defensive JSON parsing
* High-risk response override protection

---

## 📈 Future Enhancements

* Emotional trend analytics dashboard
* Admin monitoring panel
* AI model fine-tuning
* Docker deployment
* End-to-end encryption
* Activity logging & audit trail

---

## 👤 Author

**Islam**
GitHub: [https://github.com/imrcoder07](https://github.com/imrcoder07)
LinkedIn: [https://linkedin.com/in/islam07](https://linkedin.com/in/islam07)

---

## ⭐ Support

If you found this project helpful, consider giving it a ⭐.

---

## ⚠ Disclaimer

MindGuard AI provides AI-assisted conversational support and is not a substitute for licensed medical or psychological professionals.

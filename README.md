# 🧠 MindGuard AI

### Secure Crisis-Aware Mental Health Assistant

<p align="center">
  <img src="https://img.shields.io/badge/version-v1.2.0-blue" />
  <img src="https://img.shields.io/badge/backend-Flask-red" />
  <img src="https://img.shields.io/badge/database-PostgreSQL-blue" />
  <img src="https://img.shields.io/badge/ai-Meta--Llama--3.2--3B--Instruct-purple" />
  <img src="https://img.shields.io/badge/deployment-Render-success" />
  <img src="https://img.shields.io/badge/container-Docker-blue" />
  <img src="https://img.shields.io/badge/security-Zero--Trust-brightgreen" />
</p>

---

## 🌐 Live Deployment

🚀 **Production URL:**
[https://mindguard-ai-a-secure-crisis-aware.onrender.com](https://mindguard-ai-a-secure-crisis-aware.onrender.com)

Deployed on **Render Cloud** using Docker, Gunicorn, and managed PostgreSQL.

---

# 🖼 Application Preview

## Welcome Screen

<p align="center">
  <img src="images/Welcome.png" width="900" alt="Welcome Overlay"/>
</p>

---

## 💬 Chat Interface

<p align="center">
  <img src="images/Chatbot.png" width="900" alt="Chat Interface"/>
</p>

---

## 🔐 Authentication Interface

<p align="center">
  <img src="images/login.png" width="700" alt="Login and Registration Interface"/>
  <img src="images/Register.png" width="700" alt="Login and Registration Interface"/>
</p>


---

## 📌 Overview

MindGuard AI is a cloud-deployed, crisis-aware conversational AI system designed to provide empathetic mental health support while enforcing strict security controls and structured AI safety boundaries.

The platform integrates:

* Secure multi-user authentication
* Crisis risk analysis before LLM invocation
* Controlled LLM response validation
* PostgreSQL-backed conversation memory
* Zero-trust data isolation
* Dockerized production deployment

---

## 🏗 System Architecture

<p align="center">
  <img src="images/system-architecture.png" width="950" alt="System Architecture Diagram"/>
</p>

### High-Level Processing Flow

```
User → Authentication → Crisis Engine → 
LLM (Meta-Llama-3.2-3B-Instruct via HuggingFace) → 
JSON Validation → PostgreSQL → Response
```

---

## 🚀 Core Features

### 🔐 Secure Authentication

* Flask-Login session management
* Email-based registration
* Secure password hashing (Werkzeug)
* Conversation ownership validation
* Zero-trust route protection

---

### 🧠 Crisis-Aware AI Processing

* Message risk scoring
* Crisis override gate (LLM bypass on high risk)
* Structured prompt construction
* Inference via Meta-Llama-3.2-3B-Instruct
* JSON schema validation
* Safe fallback mechanism

---

### 🗄 Persistent Conversation Storage

* Managed PostgreSQL (Render Cloud)
* User-to-conversation relational mapping
* Emotion classification tracking
* Risk score metadata
* Timestamp-based resurfacing

---

### ☁ Cloud-Native Deployment

* Docker containerization
* Gunicorn production WSGI server
* Render managed hosting
* GitHub auto-deployment integration
* 12-Factor environment configuration

---

## 🗄 Database Schema

### Users

* id
* username
* email
* password_hash
* created_at

### Conversations

* id
* user_id (Foreign Key → Users)
* created_at
* updated_at

### Messages

* id
* conversation_id (Foreign Key → Conversations)
* sender (user / assistant)
* content
* emotion
* risk_score
* created_at

---

## 🛠 Technology Stack

| Layer            | Technology                 |
| ---------------- | -------------------------- |
| Backend          | Flask                      |
| Authentication   | Flask-Login                |
| ORM              | Flask-SQLAlchemy           |
| Database         | PostgreSQL (Render)        |
| AI Model         | Meta-Llama-3.2-3B-Instruct |
| AI Provider      | HuggingFace Router API     |
| WSGI             | Gunicorn                   |
| Containerization | Docker                     |
| Hosting          | Render Cloud               |
| Version Control  | GitHub                     |

---

## ⚙ Environment Configuration

Create a `.env` file:

```env
DATABASE_URL=postgresql://user:password@host:5432/dbname
HF_TOKEN=your_huggingface_token
SECRET_KEY=your_secure_secret_key
PORT=10000
```

Secrets are never hardcoded and follow 12-Factor principles.

---

## ▶ Local Development

```bash
git clone https://github.com/imrcoder07/MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant.git
cd MindGuard-AI-A-Secure-Crisis-Aware-Mental-Health-Assistant

python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Visit:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🐳 Docker Deployment (Local)

Build:

```bash
docker build -t mindguard-ai .
```

Run:

```bash
docker run -p 10000:10000 --env-file .env mindguard-ai
```

Access:
[http://localhost:10000](http://localhost:10000)

---

## 🔎 Application Workflow

1. User authenticates securely.
2. Conversation ownership validated.
3. Message passes through Crisis Risk Engine.
4. Risk score is calculated.
5. High risk → LLM bypass → Safe crisis response.
6. Low/medium risk → Structured prompt → LLM inference.
7. JSON response validated.
8. Data persisted in PostgreSQL.
9. Clean response returned to UI.

---

## 🔐 Security Principles

* Secure password hashing
* Email normalization & validation
* Zero-trust conversation ownership
* Environment-based secret isolation
* AI response validation guard
* Managed cloud database security

---

## 👤 Author

**Islam**
B.Tech – Computer Science & Engineering

GitHub: [https://github.com/imrcoder07](https://github.com/imrcoder07)
LinkedIn: [https://linkedin.com/in/islam07](https://linkedin.com/in/islam07)

---

## ⚠ Disclaimer

MindGuard AI provides AI-assisted conversational support and does not replace licensed medical or psychological professionals. For serious mental health concerns, consult qualified healthcare professionals or emergency services.


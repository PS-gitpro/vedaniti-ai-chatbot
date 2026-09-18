---
title: Vedaniti AI Chatbot
emoji: 🤖
colorFrom: indigo
colorTo: yellow
sdk: streamlit
sdk_version: 1.52.2
app_file: app.py
pinned: false
---

# 🤖 Vedaniti AI Chatbot

An intelligent AI-powered customer support assistant built using **Groq GPT-OSS 120B** and **Streamlit**, designed for Vedaniti Technologies to provide instant, accurate, and context-aware responses about software development services, solutions, and business inquiries.

🚀 **Live Demo:** https://huggingface.co/spaces/PS-gitpro/vedaniti-ai-chatbot

---

## ✨ Features

- 🧠 **Advanced AI Responses** — Powered by Groq LLaMA 3.3 70B for fast and intelligent conversations
- ⚡ **High Performance** — Optimized response handling with retry logic and smooth interaction flow
- 🎯 **Context-Aware Assistance** — Trained with Vedaniti Technologies service-related knowledge
- 💬 **Persistent Chat Memory** — Maintains conversation history for better user experience
- 📱 **Responsive UI** — Clean and mobile-friendly Streamlit interface
- 🔒 **Secure API Handling** — API keys managed securely using Hugging Face Space Secrets
- 🌐 **Cloud Deployable** — Easily deployable on Hugging Face Spaces or local systems
- 🛠️ **Production Ready** — Structured architecture with scalable deployment support

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit
- **Backend AI Model:** Groq LLaMA 3.3 70B
- **Language:** Python
- **Deployment:** Hugging Face Spaces
- **API Integration:** Groq API

---

## 📂 Project Structure

```bash
├── app.py                # Main Streamlit application
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── assets/               # Static resources (if any)
```

---

## 🚀 Quick Start

### 📌 Prerequisites

Before running the project, make sure you have:

- Python 3.10+
- Groq API Key
- Git installed
- Hugging Face account (optional for deployment)

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/ps-gitpro/vedaniti-ai-chatbot.git
cd vedaniti-ai-chatbot
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

```env
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

After running, open:

```bash
http://localhost:8501
```

---

## 🌐 Deployment on Hugging Face Spaces

1. Create a new Streamlit Space on Hugging Face
2. Upload project files
3. Add your `GROQ_API_KEY` inside **Space Secrets**
4. Deploy and enjoy 🚀

---

## 📸 Live Application

🔗 Hugging Face Space: https://huggingface.co/spaces/PS-gitpro/vedaniti-ai-chatbot

---

## 🎯 Use Cases

- AI Customer Support Assistant
- Company Service Inquiry Bot
- Business Automation Chatbot
- AI FAQ Assistant
- Lead Engagement System

---

## 🤝 Contributing

Contributions, feature suggestions, and improvements are welcome!

```bash
# Fork the repository
# Create a new branch
git checkout -b feature-name

# Commit your changes
git commit -m "Added new feature"

# Push to GitHub
git push origin feature-name
```

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Developer

Developed by **Prateek Singh**

- GitHub: https://github.com/ps-gitpro
- Hugging Face: https://huggingface.co/PS-gitpro

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub!

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

# 🤖 Ask Me - Vedaniti AI Assistant

A production-ready AI chatbot powered by **Groq LLaMA 3.3 70B**, built for Vedaniti Technologies to answer customer inquiries about software development services.

## Features

✨ **Intelligent Responses** - Powered by Groq LLaMA 3.3 70B
⚡ **Fast & Reliable** - Exponential backoff retry logic (3 attempts)
🎯 **Contextual Answers** - Knowledge base about Vedaniti services
🔒 **Secure** - API keys stored in HF Space secrets
📱 **Mobile-Friendly** - Responsive Streamlit UI
💬 **Chat History** - Persistent conversation memory

## Quick Start

### Prerequisites
- Python 3.10+
- Groq API Key
- Hugging Face Space (or local deployment)

### Installation

```bash
# Clone repo
git clone https://github.com/ps-gitpro/vedaniti-ai-chatbot.git
cd vedaniti-ai-chatbot

# Install dependencies
pip install -r requirements.txt

# Create .env file
echo "GROQ_API_KEY=your_api_key_here" > .env

# Run app
streamlit run app.py

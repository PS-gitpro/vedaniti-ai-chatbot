import os
import time
import streamlit as st
from groq import Groq

# --- 1. SECURE CONFIGURATION ---
api_key = os.getenv("GROQ_API_KEY") or st.secrets.get("GROQ_API_KEY")

if not api_key:
    st.error("⚠️ API Key missing! Add GROQ_API_KEY to your Secrets.")
    st.stop()

client = Groq(api_key=api_key)

MODEL_ID = "llama-3.3-70b-versatile"

# --- 2. UPDATED VEDANITI STATS (from screenshot) ---
VEDANITI_CONTEXT = """
Vedaniti Technologies (https://vedaniti.com/) - Custom software solutions.

📊 LATEST STATS:
- 70+ Projects Completed
- 63+ Happy Clients  
- 27+ Team Members

CONTACT:
- 📞 +91 9529350977
- 📧 info@vedaniti.com

SERVICES:
- Custom Software Development
- Website Design  
- Mobile Apps (iOS/Android)
- UI/UX Design
- Edtech Solutions
- AI/ML Integration & Chatbots

MISSION: 'Innovate. Build. Grow.'

COMMON QUERIES:
- Pricing: Flexible. Free consult: +91 9529350977
- Timeline: 2-12 weeks
- Portfolio: https://vedaniti.com/#portfolio
- Contact: +91 9529350977 | info@vedaniti.com
"""

SYSTEM_PROMPT = f"""Ask Me - Vedaniti AI Assistant (vedaniti.com)

KNOWLEDGE: {VEDANITI_CONTEXT}

RULES:
1. Use ONLY this knowledge.
2. Mention updated stats: 70+ projects, 63+ clients, 27+ team.
3. Include contacts for pricing/contact.
4. 2-4 sentences. End: "📞 +91 9529350977"
5. Off-topic: "Software agency! 70+ projects delivered 📧 info@vedaniti.com"

Friendly, professional.
"""

# --- 3. ENHANCED UI ---
st.set_page_config(page_title="Vedaniti AI", page_icon="🤖", layout="wide")

st.title("🤖 Vedaniti AI Assistant")
st.caption("📞 +91 9529350977 | 📧 [info@vedaniti.com](mailto:info@vedaniti.com)")

# Welcome + Updated Stats + Try Asking
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown("### 👋 Welcome!")
    st.markdown("**📊 Latest Stats**")
    st.info("**70+** Projects\n**63+** Clients\n**27+** Team")
    
with col2:
    st.markdown("### 💡 Try Asking")
    suggestions = [
        "What services?", "Website pricing?", "App timeline?", 
        "Contact number?", "Your portfolio?"
    ]
    for i, suggestion in enumerate(suggestions):
        if st.button(suggestion, key=f"sug_{i}", use_container_width=True):
            st.session_state.suggested = suggestion
            st.rerun()

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "👋 Hi! Vedaniti: 70+ projects, 63+ happy clients, 27+ team. Ask about services or 📞 +91 9529350977"}]

# Chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# --- 4. CHAT INPUT ---
prompt = st.chat_input("Ask anything...")

if "suggested" in st.session_state:
    prompt = st.session_state.suggested
    del st.session_state.suggested

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    
    with st.chat_message("assistant"):
        with st.spinner("⚡ Thinking..."):
            success = False
            for attempt in range(3):
                try:
                    response = client.chat.completions.create(
                        model=MODEL_ID,
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT},
                            {"role": "user", "content": prompt}
                        ],
                        temperature=0.3, max_tokens=256, top_p=0.95
                    )
                    response_text = response.choices[0].message.content
                    st.markdown(response_text)
                    st.session_state.messages.append({"role": "assistant", "content": response_text})
                    success = True
                    break
                except Exception as e:
                    if "429" in str(e):
                        time.sleep(5 * (attempt + 1))
                    else:
                        st.error(f"❌ Error: {str(e)[:100]}")
                        break
            if not success:
                st.error("⚠️ Service busy.")

# --- 5. UPDATED SIDEBAR ---
with st.sidebar:
    st.markdown("### 🎛️ Controls")
    
    if st.button("🧹 Clear Chat", use_container_width=True):
        st.session_state.messages = [{"role": "assistant", "content": "👋 Chat cleared! Vedaniti: 70+ projects delivered 📞 +91 9529350977"}]
        st.rerun()
    
    st.divider()
    st.markdown("### 📊 Latest Stats")
    st.metric("Projects", "70+")
    st.metric("Clients", "63+")
    st.metric("Team", "27+")
    
    st.divider()
    st.markdown("### 📞 Contact")
    st.info("**+91 9529350977**\n**info@vedaniti.com**")
    
    st.markdown("### ⚡ Powered By")
    st.info("Groq LLaMA 3.3 70B")

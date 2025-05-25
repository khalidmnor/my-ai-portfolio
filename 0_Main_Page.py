import streamlit as st
from utils.ai_chat import ask_bot

st.set_page_config(
    page_title="Main Page",  # This sets the sidebar menu name
    page_icon="🏠",
    layout="centered",
    initial_sidebar_state="expanded"
)
st.title("👋 Welcome to My AI Portfolio")
st.write("Ask me anything about my work!")

# Suggestions section in the sidebar (always visible)
st.sidebar.write("#### 💡 Suggestions:")
suggestions = [
    "What is Khalid's skills?",
    "Khalid's previous experiences?",
    "What projects has Khalid worked on?",
    "What technologies does Khalid use?"
]

suggestion_clicked = None
for s in suggestions:
    if st.sidebar.button(s, key=f"sidebar_suggestion_{s}"):
        suggestion_clicked = s

# Chat history section (main area)
if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

user_input = st.chat_input("Type your question...")

# Prioritize suggestion button click over manual input
if suggestion_clicked:
    user_input = suggestion_clicked

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    response = ask_bot(user_input)
    st.session_state.messages.append({"role": "ai", "content": response})
    with st.chat_message("ai"):
        st.write(response)
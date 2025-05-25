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

# Inject JavaScript to scroll to bottom after chat messages
st.markdown(
    """
    <script>
        window.scrollTo(0, document.body.scrollHeight);
    </script>
    """,
    unsafe_allow_html=True,
)

user_input = st.chat_input("Type your question...")

# Prioritize suggestion button click over manual input
if suggestion_clicked:
    user_input = suggestion_clicked

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)
    # Stream the AI response with loading indicator
    with st.chat_message("ai"):
        response_container = st.empty()
        loading_container = st.empty()
        loading_container.markdown(
            """
            <div style="display: flex; align-items: center;">
                <span class="loader" style="margin-right: 8px;"></span>
                <span>Thinking...</span>
            </div>
            <style>
            .loader {
                border: 4px solid #f3f3f3;
                border-top: 4px solid #3498db;
                border-radius: 50%;
                width: 18px;
                height: 18px;
                animation: spin 1s linear infinite;
                display: inline-block;
            }
            @keyframes spin {
                0% { transform: rotate(0deg);}
                100% { transform: rotate(360deg);}
            }
            </style>
            """,
            unsafe_allow_html=True,
        )
        full_response = ""
        for chunk in ask_bot(user_input, stream=True):
            full_response += chunk
            response_container.write(full_response)
        loading_container.empty()
    st.session_state.messages.append({"role": "ai", "content": full_response})
    st.rerun()
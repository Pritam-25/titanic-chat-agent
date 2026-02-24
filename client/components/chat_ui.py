import streamlit as st
from api import ask_backend
from utils.helper import decode_base64_image


def render_chat():
    st.title("🚢 Titanic Dataset Chat Agent")
    st.caption("Ask questions about the Titanic dataset and get insights with visualizations.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Input box
    user_input = st.chat_input("Ask a question about the Titanic dataset...")

    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        with st.spinner("Analyzing data..."):
            response = ask_backend(user_input)

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.get("answer"),
            "image": response.get("image_base64")
        })

    # Render chat history
    for msg in st.session_state.messages:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.write(msg["content"])
        else:
            with st.chat_message("assistant"):
                st.write(msg["content"])

                if msg.get("image"):
                    decode_base64_image(msg["image"])
                    st.image(msg["image"], width="stretch")
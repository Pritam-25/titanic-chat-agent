import streamlit as st
from api import ask_backend

SUGGESTIONS = {
    "What percentage of passengers were male on the Titanic?": "What percentage of passengers were male on the Titanic?",
    "Show me a histogram of passenger ages": "Show me a histogram of passenger ages",
    "What was the average ticket fare?": "What was the average ticket fare?",
    "How many passengers embarked from each port?": "How many passengers embarked from each port?",
}

def render_chat():
    st.title("🚢 Titanic Dataset Chat Agent")
    st.caption("Ask questions about the Titanic dataset and get insights with visualizations.")

    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Suggestions at the top
    selected_suggestion = st.pills(
        label="Example Questions",
        label_visibility="visible",
        options=list(SUGGESTIONS.keys()),
        key="selected_suggestion"
    )

    # Render existing history FIRST (before processing new input)
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])
            if msg.get("image"):
                st.image(msg["image"], width="stretch")

    # Determine new input
    if selected_suggestion:
        user_input = SUGGESTIONS[selected_suggestion]
    else:
        user_input = st.chat_input("Ask a question about the Titanic dataset...")

    if user_input:
        # Append and render user message 
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.write(user_input)

        #  Append and render assistant message 
        with st.chat_message("assistant"):
            with st.spinner("Analyzing data..."):
                response = ask_backend(user_input)
            st.write(response.get("answer"))
            if response.get("image_base64"):
                st.image(response.get("image_base64"), width="stretch")

        st.session_state.messages.append({
            "role": "assistant",
            "content": response.get("answer"),
            "image": response.get("image_base64")
        })
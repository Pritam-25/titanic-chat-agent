import streamlit as st
from components.chat_ui import render_chat

st.set_page_config(
    page_title="Titanic Chat Agent",
    page_icon="🚢",
    layout="centered"
)

render_chat()
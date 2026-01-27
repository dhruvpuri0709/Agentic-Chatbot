import streamlit as st
from langchain_groq import ChatGroq


@st.cache_resource  # 🔥 THIS IS THE KEY FIX
def _create_model(model_name, groq_api_key):
    import hashlib

    print("RAW KEY repr:", repr(groq_api_key))
    print("KEY LENGTH:", len(groq_api_key))
    print("KEY HASH:", hashlib.sha256(groq_api_key.encode()).hexdigest())

    return ChatGroq(model=model_name, groq_api_key=groq_api_key)
    
class Groq_llm:
    
    def __init__(self, user_control_input: dict):
        self.user_controls_input = user_control_input

    def get_llm_model(self):
        groq_api_key = (
            self.user_controls_input.get('GROQ_API_KEY') or 
            st.session_state.get('GROQ_API_KEY')
        )

        model_name = self.user_controls_input["selected_groq_model"]

        if not groq_api_key:
            st.error("Please enter groq api key")
            return None

        print("MODEL:", model_name)
        print("KEY:", groq_api_key[:10])

        return _create_model(model_name, groq_api_key)

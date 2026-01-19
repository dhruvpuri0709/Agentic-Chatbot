from langchain_groq import ChatGroq
import os
import streamlit as st

class Groq_llm:
    
    def __init__(self, user_control_input: dict):
        self.user_controls_input = user_control_input
    
    def get_llm_model(self):
        
        try:
            groq_api_key = self.user_controls_input['GROQ_API_KEY']
            model_name = self.user_controls_input["selected_groq_model"]
            if groq_api_key == "" and os.environ['GROQ_API_KEY'] == "":
                st.error("Please enter groq api key")
                
            llm = ChatGroq(model = model_name, groq_api_key = groq_api_key)
        except Exception as e:
            raise ValueError(f"Error occured with exception: {e}")
        
        return llm
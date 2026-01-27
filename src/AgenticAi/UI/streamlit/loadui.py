import streamlit as st 
import os
from src.AgenticAI.UI.uiconfigfile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}
        if "IsFetchButtonClicked" not in st.session_state:
            st.session_state.IsFetchButtonClicked = False

        st.session_state.timeframe = False
    
    def load_streamlit_ui(self):
        
        st.set_page_config(page_title= "🤖 " + self.config.get_page_title(), layout="wide")
        st.header("🤖 " + self.config.get_page_title())
        
        with st.sidebar:
            # Get options from config file
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()
            
            # LLM Selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM",options=llm_options)
            
            if self.user_controls["selected_llm"] == "Groq":
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Model",model_options)
                st.session_state["GROQ_API_KEY"] = st.text_input("Groq API Key", type="password")
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"]
              
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠️ Please enter your GROQ API key to proceed. Don't have? refer : https://console.groq.com/keys ")
            
            # Usecase Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Usecase",usecase_options)
            
            # Tavily API Key
            if self.user_controls["selected_usecase"] == "Chatbot With Web" or self.user_controls['selected_usecase'] == "AI News":
                os.environ["TAVILY_API_KEY"]=self.user_controls["TAVILY_API_KEY"] = st.session_state["TAVILY_API_KEY"] = st.text_input("Tavily API Key",type = "password")
                
                # Validate the key
                if not self.user_controls["TAVILY_API_KEY"]:
                    st.warning("⚠️ Please enter your Tavily API key to proceed. Don't have? refer : https://app.tavily.com/home")
                
            if self.user_controls["selected_usecase"] == "AI News":
                st.subheader("📰 AI News Explorer ")
                
                with st.sidebar:
                    time_frame = st.selectbox(
                        "📅 Select Time Frame",
                        ["Daily","Weekly","Monthly"],
                        index = 0
                    )
                    
                    self.user_controls["frequency"] = time_frame
                    
                if st.button("Fetch Latest AI News",use_container_width=True):
                    st.session_state.IsFetchButtonClicked = True
                    st.session_state.timeframe = time_frame
                    
            
        return self.user_controls
        
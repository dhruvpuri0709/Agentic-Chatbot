from src.AgenticAI.UI.streamlit.loadui import LoadStreamlitUI
import streamlit as st
from src.AgenticAI.LLMS.Groqllm import Groq_llm
from src.AgenticAI.Graph.GraphBuilder import GraphBuilder
from src.AgenticAI.UI.streamlit.display_result import DisplayResultsSreamlit
import os

def load_agentic_ai_app():
    """
    Loads and runs the LangGraph agentic ai application with streamlit UI.
    This function initilaizes the UI, handles user input, configures the LLM model,
    sets up the graph based on the selected use case, and displays the output while
    implementing exception handling for robustness
    
    """
    
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()
   
    if not user_input:
        st.error("Error: Failed to load user input section from the UI")
        return
    
    print(f"GROQ_API_KEY {user_input['GROQ_API_KEY']}")
        
    if st.session_state.IsFetchButtonClicked:
        user_message = st.session_state.timeframe
    else:
        user_message = st.chat_input("Enter your message:")
    
    if user_message:
        try:
            # Loading the LLM
            model = Groq_llm(user_input).get_llm_model()
            try:
                print(model.invoke("hi"))
            except Exception as e:
                st.error(f"GROQ ERROR: {e}")
                print("FULL ERROR:", e)

            if not model:
                st.error("Error: Model could not be loaded")
                return
            
            usecase = user_input.get("selected_usecase")
            
            if not usecase:
                st.error("Error: usecase was not selected")
                return
            
            # Loading the graph
            graph_builder = GraphBuilder(model)
            
            try:
                graph = graph_builder.setup_graph(usecase)
                print(f"User message is {user_message}")
                DisplayResultsSreamlit(usecase,graph,user_message).display_result_on_ui()
            except Exception as e:
                st.error(f"Error: Graph set up failed - {e}")
                return
            
        except Exception as e:
            st.error(f"Error: Project setup failed - {e}")
            return
            
        
    
    
            
    
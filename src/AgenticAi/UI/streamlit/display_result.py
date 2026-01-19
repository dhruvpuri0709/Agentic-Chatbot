import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultsSreamlit:
    
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
        # 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
    def display_result_on_ui(self):
        
        if self.usecase == "Basic Chatbot":
            print('Inside basic chatbot display')
            thread = {"configurable":{"thread_id":"1"}}
            try:
                for event in self.graph.stream( {"messages": [HumanMessage(content=self.user_message)]}, config = thread):
                    print("reached event streamming")
                    print(f"Event is {event}")
                    print(f"event.values: {event.values}")
                    for value in event.values():
                        if "messages" not in value:
                            continue
                        print(f"Value: {value}")
                        print(f"value['messages']: {value['messages']}")
                        with st.chat_message("user"):
                            st.write(self.user_message)
                        with st.chat_message("assistant"):
                            st.write(value["messages"].content)
                    print("--------------")
            except Exception as e:
                st.error(f"Error: display failed with error as {e}")
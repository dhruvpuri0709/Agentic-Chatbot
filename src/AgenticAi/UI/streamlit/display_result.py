import streamlit as st
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import json

class DisplayResultsSreamlit:
    
    def __init__(self,usecase,graph,user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message
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
        
        elif self.usecase == "Chatbot With Web":
            # Prepare state and invoke the graph
            print("reached chatbot with web display usecase")
            initial_state = {"messages":[self.user_message]}
            res = self.graph.invoke(initial_state)
            
            for message in res["messages"]:
                if type(message) == HumanMessage:
                    with st.chat_message("user"):
                        st.write(message.content)
                elif type(message) == ToolMessage:
                    with st.chat_message("ai"):
                        st.write("Tool Call Start")
                        st.write(message.content)
                        st.write("Tool Call End")
                elif type(message) == AIMessage and message.content:
                    with st.chat_message("assistant"):
                        st.write(message.content)
        
        elif self.usecase == "AI News":
            print("Inside AI news display ui usecase")
            
            frequency = self.user_message
            with st.spinner("Fetching and summarizing news... ⏳"):
                result_state = self.graph.invoke({"messages":frequency})
                print(f"The result sate is {result_state}")
                
                try:
                    # Read the markdown file
                    AI_NEWS_PATH = f"./AINews/{frequency.lower()}_summary.md"
                    with open(AI_NEWS_PATH,"r") as file:
                        markdown_content = file.read()
                        
                        # Display the markdown content inn streamlit
                        st.markdown(markdown_content,unsafe_allow_html=True)
                except FileNotFoundError:
                    st.error(f"News not generated or file now found {AI_NEWS_PATH}")
                
                except Exception as e:
                    st.error(f"Process failed with error {e}")
                            
            
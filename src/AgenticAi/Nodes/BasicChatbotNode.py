from src.AgenticAI.State.State import State
from langchain_core.messages import SystemMessage

class BasicChatbotNode():
    """
    Basic chatbot node implementation
    """
    def __init__(self,model):
        self.llm = model
    
    def process(self,state:State):
        """
        Processes the input state and generates a chatbot response.
        """
        sys_message = SystemMessage(content = "You are an helpful assistant, asnwer all questions to the best of your ability if you donot know the answer to a question then say that you don't know")
        
        return {"messages": self.llm.invoke([sys_message] + state["messages"])}
        
        
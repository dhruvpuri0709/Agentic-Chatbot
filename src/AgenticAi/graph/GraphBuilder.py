from langgraph.graph import START, END, StateGraph
from src.AgenticAI.State.State import State
from src.AgenticAI.Nodes.BasicChatbotNode import BasicChatbotNode
from langgraph.checkpoint.memory import MemorySaver

class GraphBuilder:
    
    def __init__(self,model):
        self.llm = model
        self.graph_builder = StateGraph(State)
    
    def basic_chatbot_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the "BasicChatbotNode" class
        and integrates it into the graph.
        """
        # Load the basic chatbot node
        self.basicchatbot = BasicChatbotNode(self.llm)
        
        # Adding node
        self.graph_builder.add_node("Chatbot",self.basicchatbot.process)
    
        # Adding edges
        self.graph_builder.add_edge(START,"Chatbot")
        self.graph_builder.add_edge("Chatbot",END)
        
        # Memory Checkpointer
        memory = MemorySaver()
        
        graph = self.graph_builder.compile(checkpointer=memory)
        return graph
        
    
    def setup_graph(self,usecase:str):
        
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_graph()
    
         
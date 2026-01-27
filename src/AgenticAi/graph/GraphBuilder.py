from langgraph.graph import START, END, StateGraph
from src.AgenticAI.State.State import State
from src.AgenticAI.Nodes.BasicChatbotNode import BasicChatbotNode
from langgraph.checkpoint.memory import MemorySaver
from src.AgenticAI.Tools.tools import create_tool_node, get_tools
from langgraph.prebuilt import tools_condition
from src.AgenticAI.Nodes.ChatbotWithTools import ChatbotWithTools
from src.AgenticAI.Nodes.AI_News_Node import AI_News_Node

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
    
    def chatbot_with_tools_graph(self):
        """
        Builds an advanced chatbot with tool integrations.
        This method creates a chatbot graph that included both a chatbot node
        and a tool node. 
        """
        # Getting the tools
        tools = get_tools()
        tool_node = create_tool_node(tools)
        
        # Get the chatbot tool node
        chatbot_with_tools_node = ChatbotWithTools(self.llm,tools).create_chatbot()
        
        # Add Nodes
        self.graph_builder.add_node("SuperBot",chatbot_with_tools_node)
        self.graph_builder.add_node("Tools",tool_node)
        
        # Add Edges
        self.graph_builder.add_edge(START, "SuperBot")
        self.graph_builder.add_conditional_edges("SuperBot",tools_condition,{"tools":"Tools",END:END})
        self.graph_builder.add_edge("Tools","SuperBot") # Following the ReAct architecture 
        self.graph_builder.add_edge("SuperBot",END)
        
        return self.graph_builder.compile()
    
    def ai_news_graph(self):
        """
        Builds an AI News summarizer chatbot which uses tavily search to search latest AI news 
        and then formats and saves it as a markdown file.
        """
        
        # Getting the AI_News_Node
        ai_news_node = AI_News_Node(self.llm)
        
        # Add Nodes
        self.graph_builder.add_node("Fetch_News",ai_news_node.fetch_news)
        self.graph_builder.add_node("Summarize_News",ai_news_node.summarize_news)
        self.graph_builder.add_node("Save_Result",ai_news_node.save_result)
        
        # Add Edges
        self.graph_builder.add_edge(START,"Fetch_News")
        self.graph_builder.add_edge("Fetch_News","Summarize_News")
        self.graph_builder.add_edge("Summarize_News","Save_Result")
        self.graph_builder.add_edge("Save_Result",END)
        
        return self.graph_builder.compile()
    
    def setup_graph(self,usecase:str):
        
        if usecase == "Basic Chatbot":
            return self.basic_chatbot_graph()
        
        elif usecase == "Chatbot With Web":
            return self.chatbot_with_tools_graph()
        
        elif usecase == "AI News":
            return self.ai_news_graph()
    
         
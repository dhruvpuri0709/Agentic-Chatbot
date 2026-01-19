from typing_extensions import Annotated, TypedDict
from langgraph.graph.message import add_messages

class State(TypedDict):
    """
    Represents the structure of the state used in the graph
    """
    messages: Annotated[list,add_messages]
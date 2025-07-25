from langgraph.graph import StateGraph, END

from nodes.query_parser import query_parser_node
from state import AgentState


graph = StateGraph(AgentState)

graph.add_node("query_parser", query_parser_node)

graph.set_entry_point("query_parser")

graph.set_finish_point("query_parser")

app = graph.compile()

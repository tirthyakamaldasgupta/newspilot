from langgraph.graph import StateGraph, END
from nodes.query_parser import query_parser_node
from nodes.search import search_node
from nodes.email import email_node
from state import AgentState


def route_action_from_parser(state: AgentState) -> str:
    if state.action in ("search_and_email", "search_only"):
        return "search_node"
    elif state.action == "email_only":
        return "email_node"
    else:
        return END


def route_after_search(state: AgentState) -> str:
    if state.action == "search_and_email":
        return "email_node"
    else:
        return END


graph = StateGraph(AgentState)

graph.add_node("query_parser_node", query_parser_node)
graph.add_node("search_node", search_node)
graph.add_node("email_node", email_node)

graph.set_entry_point("query_parser_node")

graph.add_conditional_edges(
    "query_parser_node",
    route_action_from_parser,
    {
        "search_node": "search_node",
        "email_node": "email_node",
        END: END
    }
)

graph.add_conditional_edges(
    "search_node",
    route_after_search,
    {
        "email_node": "email_node",
        END: END
    }
)

graph.add_edge("email_node", END)

app = graph.compile()

print(app.get_graph().draw_mermaid())

from dotenv import load_dotenv
from state import AgentState
from langchain_google_community import GoogleSearchAPIWrapper


load_dotenv()


search_wrapper = GoogleSearchAPIWrapper()


def search_node(state: AgentState) -> AgentState:
    print("Searching the web for the latest updates ...")

    query = state.web_search_query

    results = search_wrapper.results(query, num_results=state.number_of_results or 5)

    formatted_results = [{"title": f"{res['title']}", "link": f"{res['link']}"} for res in results]

    print(f"I found {len(results)} results. Let me prepare them for you.")

    return state.model_copy(update={"results": formatted_results})

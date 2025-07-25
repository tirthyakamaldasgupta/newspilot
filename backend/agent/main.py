from graph import app
from state import AgentState

state = AgentState(user_query="Send me all technology articles from Hindustan Times and Indian Express")

final_state = app.invoke(state)

print(final_state)

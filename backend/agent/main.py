from graph import app
from state import AgentState

query = input(
    "I can help you search news articles from Indian publishers and send them to your email.\n"
    "Example queries:\n"
    "  - Send me all technology articles from Hindustan Times and Indian Express\n"
    "  - Email me today’s top headlines from Times of India\n"
    "Enter your request: "
)

state = AgentState(query=query)

for step in app.stream(state):
    print("Current state snapshot: ", step)

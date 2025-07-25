from langchain_core.prompts import PromptTemplate


query_parser_prompt = PromptTemplate.from_template("""
You are an intelligent assistant that extracts structured data from natural language queries about news.

Given a user query, extract the following as JSON:
- sites: List of websites or news sources (e.g., "hindustantimes.com", "toi.in", "Times of India")
- topics: List of topics the user is interested in (e.g., "technology", "sports")
- number_of_results: Approximate number of news articles requested. Default to 5 if unclear.
- web_search_query: A smart Google search query combining the topics and site filters.
- action: "search_only" if the user only wants to view the results, or "search_and_email" if they want them emailed.

User query: {user_query}
Respond in pure JSON.
""")

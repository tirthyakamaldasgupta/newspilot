from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser
from langchain_mistralai.chat_models import ChatMistralAI
from state import AgentState
from prompts.query_parser import query_parser_prompt
from output_schema import ParsedQuery


load_dotenv()

llm = ChatMistralAI(model_name="mistral-medium-2505")

parser = PydanticOutputParser(pydantic_object=ParsedQuery)

chain = query_parser_prompt | llm | parser


def query_parser_node(state: AgentState) -> AgentState:
    parsed = chain.invoke({"user_query": state.user_query})

    return AgentState(**parsed.dict(exclude_unset=True), user_query=state.user_query)

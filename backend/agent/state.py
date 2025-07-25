from pydantic import BaseModel
from typing import Optional, List


class AgentState(BaseModel):
    user_query: str
    web_search_query: Optional[str] = None
    sites: Optional[List[str]] = None
    topics: Optional[List[str]] = None
    number_of_results: Optional[int] = 5
    action: Optional[str] = None
    results: Optional[str] = None
    email_message: Optional[str] = None

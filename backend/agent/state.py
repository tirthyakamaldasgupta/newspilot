from pydantic import BaseModel
from typing import Optional, List, Dict


class AgentState(BaseModel):
    query: str
    web_search_query: Optional[str] = None
    sites: Optional[List[str]] = None
    topics: Optional[List[str]] = None
    number_of_results: Optional[int] = 5
    action: Optional[str] = None
    results: Optional[List[Dict[str, str]]] = None
    email_message: Optional[str] = None

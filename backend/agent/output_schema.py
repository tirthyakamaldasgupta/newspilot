from pydantic import BaseModel
from typing import Optional, List


class ParsedQuery(BaseModel):
    web_search_query: Optional[str] = None
    sites: Optional[List[str]] = None
    topics: Optional[List[str]] = None
    number_of_results: Optional[int] = 5
    action: Optional[str] = None

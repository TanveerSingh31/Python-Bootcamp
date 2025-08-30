from pydantic import BaseModel
from typing import Dict, List, Optional

# Mixing types from Pydantic & typing module 
# typing -> module in-built in python

class User(BaseModel):
    id: int
    name: str
    address: List[str]
    additionalInfo: Dict[str, str] 


u = User(id=1, name="Tanveer", address=["122001", "Sector 22"], additionalInfo={"phone": "8360763689", "gender":"M"})


print(u)
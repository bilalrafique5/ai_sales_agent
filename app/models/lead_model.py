from pydantic import BaseModel

class Lead(BaseModel):

    company_name: str
    website: str
    decision_maker: str
    role: str
    email: str
    industry: str
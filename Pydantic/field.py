from pydantic import BaseModel, Field

class User(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=1,
        max_length=50,
        description="Name of the person"
    )
    age: int = Field(
        ...,
        ge=1,
        le=100,
        description="Age of the person"
    )

userData = {"id": 1, "name":"", "age": 12}
userData2 = {"id": 1, "name":"Tanveer", "age": 12}

# Will give err 
# u = User(**userData)

u = User(**userData2)
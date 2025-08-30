from pydantic import BaseModel, field_validator, model_validator

class User(BaseModel):
    id: int
    name: str
    age: int

    # Validates specific field on the model
    @field_validator('name')
    def validate_name(cls, v):
        if(v == "Tanveer"):
            raise ValueError("Name cannnot be Tanveer")
        else:
            return v
        

    # validates all fields of the model
    @model_validator(mode="after")
    def validate_model(cls, values):
        if values.age > 20 and values.name == "":
            raise ValueError("This is not valid")
        else:
            return values




userData2 = {"id": 1, "name":"Singh", "age": 12}
userData3 = {"id": 1, "name":"", "age": 122}

# Will give err 
# u = User(**userData)

u = User(**userData2)
# u = User(**userData3) -> gives error
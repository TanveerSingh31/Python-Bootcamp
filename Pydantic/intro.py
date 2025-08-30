# **Steps to use Pydantic**

# 1. pip install pydantic
# 2. from pydantic → import BaseModel class
# BaseModel class → contains the pydantic functionalities
# 3. Inherit the BaseModel class to your class
# 4. Define the properties on the class, along with datatypes
# 5. Use keyword args while creating objects from the class
# 6. Automatic validations work by Pydantic

from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    isActive: bool

# pydantic will try to convert your data to applied datatype 

u = User(id=1, name="Tanveer", isActive=True)
u2 = User(id='1', name="Tanveer", isActive=True) # this works as well !




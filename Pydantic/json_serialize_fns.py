from pydantic import BaseModel

class Address(BaseModel):
    address1: str
    address2: str
    postalCode: int


class Person(BaseModel):
    name: str
    age: int
    address: Address


p = Person(
    name="Tanveer",
    age=23,
    address=Address(
        address1="abc",
        address2="cde",
        postalCode=122001
    )
)

print(p.model_dump()) # returns dictionary from object
print(p.model_dump_json()) # returns JSON encoded string from object
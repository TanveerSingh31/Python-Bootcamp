from pydantic import BaseModel, computed_field

class User(BaseModel):
    fname: str
    lname: str

    @computed_field
    @property
    def fullName(self) -> str:
        return self.fname + ' ' + self.lname

u = User(fname="Tanveer", lname="Singh")

print(u.fullName)

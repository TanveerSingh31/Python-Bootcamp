# classmethod -> returns object of the class
# "cls" -> provides reference to the class itself, used to create objet of the class

class Person: 
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    # returns object from dictionary 
    def getPersonFromDict(cls, personData):
        return cls(personData.get('name'), personData.get('age'))
    
    @classmethod
    # returns object from string 
    def getPersonFromString(cls, personDataStr):
        [name, age] = personDataStr.split('-')
        return cls(name, age)
    
p1 = Person.getPersonFromDict({"name": "Tanveer", "age": 23 })
p2 = Person.getPersonFromString("Tanveer-24")


print(p1.name, p1.age)
print(p2.name, p2.age)


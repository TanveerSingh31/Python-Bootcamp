class Person:
    name="Tanveer"
    age=23

    def getName(self):
        return self.name

    def getAge(self):
        return self.age
    

p1 = Person()

print(p1.getName())
print(p1.getAge())



# Calling via the Class -> need to pass the object reference
name = Person.getName(p1)
age = Person.getAge(p1)

print(f"From Class Person - {name, age}")


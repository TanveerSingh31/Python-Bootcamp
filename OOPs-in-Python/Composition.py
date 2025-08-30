# Composition - concept wherein the reference of a class is stored directly in a property of another class, for later use

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    


class SuperPerson:
    per = Person

    def __init__(self, name, age, role):
        # Storing object of Person inside SuperPerson obj
        self.person = self.per(name, age)
        self.role = role


sp = SuperPerson("Tanveer", 23, "Admin")

print(sp.person.name, sp.person.age, sp.role)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getSummary(self):
        return f"Hello, {self.name} ! You are {self.age} old"


p1 = Person("Tanveer", 23)

print(p1.getSummary())
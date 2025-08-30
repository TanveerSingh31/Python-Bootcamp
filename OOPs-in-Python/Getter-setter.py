class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    

    # Getter
    @property
    def age(self):
        print("returned from Getter")
        return self._age
    
    #Setter
    @age.setter
    def age(self, age):
        print("inside setter")
        self._age = age


p1 = Person("Tanveer", 23)

print(p1.age)
p1.age = 100

print(p1.age)
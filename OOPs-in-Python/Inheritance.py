class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def getName(self):
        print(f"Name is {self.name}")




class Child(Parent):
    def __init__(self, name, age, gender):

        # invoking parent constructor from child constructor
        super().__init__(name, age)
        
        self.gender = gender
    
    def getAllData(self):
        print(f"name = {self.name} , age = {self.age} , gender = {self.gender}")



c1 = Child("Tanveer", 24, "Male")

c1.getName()
c1.getAllData()
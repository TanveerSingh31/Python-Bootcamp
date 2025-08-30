class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        print(self.name)

    @staticmethod
    def getData():
        print("here I am in normal method")
    
    # Will get error , if we did not use @staticmethod annotation
    # When accessing this fn. from object, python would pass the "self" to the fn. but it doesnot expect any args.!! ->Error 
    def normalMethod():
        print("non-static method")


p1 = Person("Tanveer", 23)

Person.getData()
p1.getData()

Person.normalMethod()
# p1.normalMethod()
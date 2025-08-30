class Person:
    name="Tanveer"
    age=23


p1 = Person()
p2 = Person()


p1.name = "Singh"
print(p1.name)

del p1.name

# fallbacks to value in the class -> Attribute shadowing
print(p1.name)


p1.gender = "male"
del p1.gender

# Error - 'Person' object has no attribute 'gender'
# print(p1.gender)
# Class
class Person: 
    # Data members
    name = "Tanveer"
    age = 23


# Objects
p1 = Person()
p2 = Person()


print(type(Person))
print(type(p1))

print(type(p1) is Person)



p1.name = "Singh"
p1.age = 24


print(Person.name, Person.age)
print(p1.name, p1.age)
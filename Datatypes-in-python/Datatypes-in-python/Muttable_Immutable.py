# numbers, string -> immutable

num = 100
print(f"before id of num = ${id(num)}")

num = 200
# id of num will changes -> as it points to new memory location
print(f"after id of num = ${id(num)}") 


# set -> mutable

MySet = set()
print(f"before id of set = ${id(MySet)}")
MySet.add("first")
MySet.add("Second")
MySet.add("Third")

print(MySet)
print(f"after id of set = ${id(MySet)}")


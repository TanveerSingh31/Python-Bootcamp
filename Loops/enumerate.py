# enumerate fn. returns List of tuples 
# - each tuple containing (index, item)

fruits = ["apple", "orange", "banana"]

# enumerate(fruits) -> [(0, "apple"), (1, "orange"), (2, "banana")]

for index, fruit in enumerate(fruits):
    print(f" index : {index} , fruit : {fruit}")
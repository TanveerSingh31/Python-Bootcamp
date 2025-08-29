# zip() function is used to iterate on multiple lists at the same time
# It returns List(Tuple), each tuple containing item from each list at same index 

fruits = ["apple", "orange", "banana", "papaya"]
quantityList = [10, 20, 30]

for fruit, qua in zip(fruits, quantityList):
    print(f" {fruit} - quantity - {qua}")
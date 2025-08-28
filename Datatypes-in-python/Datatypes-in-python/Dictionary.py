

# 2 ways to initialize / create dictionaries
dict1 = dict(name= "Tanveer", age = 23, gender = "male")

dict2 = {"name": 1, "age": 2}

dict2['name'] = "Tanveer"

print(dict1)
print(dict2)


# safe way to access key from dictionary
print(dict2.get('random_key'))



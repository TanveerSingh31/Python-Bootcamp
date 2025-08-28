# String - Immutable

str = "Hello World"

# Indexing --> 
# str[startIndex: endIndex+1: noOfElementsToSkip] 
print(f"{str[0:5]}")
print(f"{str[0:5:2]}")


print(f"{str[:5]}") # Hello
print(f"{str[6:]}") # World


# Reversing a string
print(f"{str[::-1]}")
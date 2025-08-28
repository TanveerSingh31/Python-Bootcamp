# Mutable - Data type

myList = ["abc", "def", "ghi"]

# methods

myList.append("xyz")
print(myList)


myList.remove("abc")
print(myList)


myList.extend(["1", "2"])
print(myList)


myList.insert(2, "insertWord")
print(myList)


poppedElement = myList.pop()
print(poppedElement)


myList.reverse()
print(myList)

numList = [5,4,3,2,1] 
numList.sort()
print(numList)


print(f"max of the list = {max(myList)}")
print(f"max of the list = {min(myList)}")




# Operator Overloading

numList2 = [1,2,3,4,5]
numList3 = [7,8,9]

numListSum = numList2 + numList3

print(numListSum)


numList4 = numList2 * 3
print(numList4) 


# Bytearray (return mutable list from immutables types - number, string...)
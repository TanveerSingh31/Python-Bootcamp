# Only stores unique values
# - Unordered
# - Immutable


myset = {"apple", "banana", "cherry", "apple"}
myset2 = {"apple", "papaya"}

print(myset)


# Operations

# Union
print(myset | myset2)

# Intersection
print(myset & myset2)

# Substracting set from intersection
print(myset - myset2)

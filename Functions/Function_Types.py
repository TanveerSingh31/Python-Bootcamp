
# Different types of functions

# 1. Pure fn.
def pureFn(name):
    return name



# 2. Impure fn.

count = 0
def impureFn(name):
    global count
    count += 1

    return count




# 3. Lambda - used lambda keyword
# Note: Lambda can be only 1 line fn. -> doesnot include explicit "return" keyword
myFn = lambda age : age = 100 

print(myFn(100))

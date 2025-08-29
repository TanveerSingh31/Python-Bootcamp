def getName(name, age):
    print(name, age)


# Different ways to call function
# 1. Same order
getName("Tanveer", 23)

# 2. passing arg. name , in this order doesnot matter !
getName(age=23, name="Tanveer")



# *args, **kwargs

def getName2(*args, **kwargs):
    print(args)
    print(kwargs)

getName2("Tanveer", "Singh", age=23, gender="male")

# *args (Tuple) -> will store all unnamed args
# **kwargs (Dictionary) -> will store all named arg's

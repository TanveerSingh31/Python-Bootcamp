

name = "Global - Tanveer"

def fun1():
    name = "Local 1 - Tanveer"

    # nested fn
    def fun2():
        # nonlocal keyword -> references the outer scope variable
        # Any changes to this will also change the outer variable's value 
        nonlocal name
        name = "Inner 1 - Tanveer"

        # we can access the outer variable using - "nonlocal" keyword
        print(name)

    fun2()
    print(name)


fun1()
print(name)


# O/P

# "Inner 1 - Tanveer"
# "Inner 1 - Tanveer" -> due to "nonlocal" keyword used 
# "Global - Tanveer"




data = ["tanveer", "singh"]

for name in data:
    if(name == "xyz"):
        print("name found")
        break
else: # treated as fallback, if nothing breaks the loop
    print("name not found")


if(xyz := 1+2):
    pass
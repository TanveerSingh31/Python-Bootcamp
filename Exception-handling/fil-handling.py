file = open("sample.txt", "w")
file.write("sample text 2")

file.close()


# using "with" statement - automatically handles any exceptions + closing of the file
with open("sample.txt", "a") as file:
    for i in range(0, 100):
        file.write(f"sample text {i} \n")
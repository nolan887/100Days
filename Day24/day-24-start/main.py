# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# The below code will automaticlaly close the file when the indented changes are complete

# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# mode "a" will append, mode "w" will write (erase & replace)
with open("my_file.txt", mode="a") as file:
    file.write("\nNew text.")
    # print(contents)
# # FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # IndexError
# fruit_list = ["Apples", "Bananas", "Pears"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# # Handling Exceptions
# try:
#     # try to run this code that might have an error
#     pass
# except:
#     # execute this code if 'try' DID NOT work
#     pass
# else:
#     # execute this if 'try' DID work
#     pass
# finally:
#     # execute this code no matter if there was or was not an error (always fires)
#     pass



# # FileNotFound Handling Exceptions
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key":"value"}
#     # print(a_dictionary["fake"])
#     print(a_dictionary["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")


# Using the "raise" error to create my own error types
height = float(input("height (m): "))
weight = int(input("weight (kg): " ))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)
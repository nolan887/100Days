# List Comprehension
numbers = [1,2,3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = "Charles"
letters_list = [letter for letter in name]
print(letters_list)

range_list = [num * 2 for num in range(1,5)]
print(range_list)

# new_list = [new_item for item in list if test]
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = [name for name in names if len(name) <= 4]
print(short_names)

long_loud_names = [xyz.upper() for xyz in names if len(xyz) > 4]
print(long_loud_names)
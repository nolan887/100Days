numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# Do Not Change the code above

# Video 233:
# Write your 1 line code below:
squared_numbers = [n ** 2 for n in numbers]
print(squared_numbers)

# Video 234:
even_numbers = [num for num in numbers if num % 2 == 0]
print(even_numbers)

# Video 235:
# Using file1.txt and file2.txt, create a variable "results" that is a list of numbers that appear in both files
file1_nums = []
file2_nums = []

with open("file1.txt") as f1:
    file1 = f1.readlines()
    for num in file1:
        file1_nums.append(num.strip())

with open("file2.txt") as f2:
    file2 = f2.readlines()
    for num in file2:
        file2_nums.append(num.strip())

print(file1_nums)
print(file2_nums)
results = [new_numb for new_numb in file1_nums if new_numb in file2_nums]
print(results)
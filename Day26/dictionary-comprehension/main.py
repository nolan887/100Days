import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanro", "Freddie"]

# Goal - cycle through list and assign random score to each
# students_scores = {new_key:new_value for item in list}
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)

# Goal - cycle through prior list to create new dictionary for students who scored over 60 and their scores
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)
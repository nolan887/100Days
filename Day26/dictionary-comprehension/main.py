import random

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanro", "Freddie"]

# Goal - cycle through list and assign random score to each
# new_dictionary = {new_key:new_value for item in list if test}
students_scores = {student:random.randint(1,100) for student in names}
print(students_scores)


# Goal - cycle through prior list to create new dictionary for students who scored over 60 and their scores
passed_students = {student:score for (student, score) in students_scores.items() if score > 60}
print(passed_students)


# 26.4, Goal: take the sentence, convert it into a list of words, and create a dictionary of each word and its length
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# my code start
words_list = sentence.split()
print(words_list)
result = {word:len(word) for word in words_list}
print(result)
# my code end


# Goal 26.5, Goal: Create a new dictionary of temperatures in deg F
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {day:(deg_c * 9/5 + 32) for (day, deg_c) in weather_c.items()}

print(weather_f)
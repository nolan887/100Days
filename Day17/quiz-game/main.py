from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

question_bank = []

for entry in question_data:
    question_text = entry["text"]
    question_answer = entry["answer"]
    new_question = Question(q = question_text, a = question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_questions():
    quiz.next_question()

print("\nGame Over.")
print(f"Your final score was {quiz.score} / {quiz.question_number}.")
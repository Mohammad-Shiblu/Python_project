import question_model
from data import question_data
from quiz_brain import Quiz_Brain

question_bank = []

for x in question_data: 
    question_text = x["text"]
    question_answer = x["answer"]
    new_question = question_model.Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print(f"Your final score is {quiz.score}/{quiz.question_number} . Good work!")

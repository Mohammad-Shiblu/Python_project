from locale import currency
from tkinter.messagebox import QUESTION

from anyio import current_effective_deadline


class Quiz_Brain:
    def __init__(self, list):
        self.question_number = 0
        self.question_list = list
        self.score = 0

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user = input(f"Q.{self.question_number} {current_question.text} (True/false)  ")
        self.check_answer(user, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, correct_answer):
        if answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right")
        else:
            print("That's wrong")
            print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}")
        print("\n")

    


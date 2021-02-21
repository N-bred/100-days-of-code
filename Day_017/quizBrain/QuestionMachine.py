import random
from InputHandler import InputHandler


class QuestionMachine:
    def __init__(self, questions):
        self.questions = questions
        self.points = 0
        self.current_question = None
        self.asked_questions = []
        self.next_question()

    def next_question(self):
        self.current_question = random.choice(self.questions)
        self.questions.remove(self.current_question)
        self.asked_questions.append(self.current_question)
        self.handle_question()

    def handle_question(self):
        answer = InputHandler.get_input(self.current_question.text + " ")
        self.validate_answer(answer)

    def validate_answer(self, answer):
        if answer.lower() == self.current_question.answer.lower():
            self.handle_correct_answer()
        else:
            self.handle_incorrect_answer()

    def get_score(self):
        return f"{self.points}/{len(self.asked_questions)}"

    def handle_correct_answer(self):
        self.points += 1
        print("You got it right!")
        print(f"The correct answer was {self.current_question.answer}")
        print(f"Your current score is: {self.get_score()}")
        self.next_question()

    def handle_incorrect_answer(self):
        return print(f"Incorrect answer, your total score was: {self.get_score()}")
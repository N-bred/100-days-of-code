from data import questions_data
from Question import Question
from QuestionMachine import QuestionMachine


def make_questions(questions):
    return [Question(question["text"], question["answer"]) for question in questions]


def main():
    if __name__ == "__main__":
        print("Welcome to the QuizBrain Project.")
        questions = make_questions(questions_data)
        questionMachine = QuestionMachine(questions)


main()
class Question:
    def __init__(self, question, answer):
        self.text = question
        self.answer = answer

    def __str__(self):
        return f"Question: {self.text}"
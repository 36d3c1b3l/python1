class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
    
    def ask(self):
        print(self.question)

    def check_answer(self, answer):
        if answer.lower() == self.answer:
            return True
        else:
            return False
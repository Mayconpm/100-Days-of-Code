class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list

    def next_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {new_question.text} (True/False)?:")
        self.check_answer(user_answer, new_question.answer)

    def still_has_question(self):
        question_list_length = len(self.question_list)
        if question_list_length > self.question_number:
            return True
        else:
            return False

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")
        print(f"Your current score is: {self.score}/{self.question_number}.\n")

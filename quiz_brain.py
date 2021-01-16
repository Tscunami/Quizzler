import html


class QuizBrain:

    def __init__(self, q_list):
        """
        :param q_list: list of all questions
        """
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """
        :return: bool, True, if there is any question left
        """
        return self.question_number < len(self.question_list)

    def next_question(self):
        """
        :return: list of all data of concrete question
        """
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return q_text

    def check_answer(self, user_answer):
        """
        compares user answer with right answer
        :param user_answer: string, "True" if user pressed green check, "False" if pressed rec cross
        :return: bool, True, if he answered right
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

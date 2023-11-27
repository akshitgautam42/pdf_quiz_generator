class QuizEvaluator:
    def evaluate_quiz(self, quiz: Quiz, user_answer: str) -> bool:
        """
        Evaluates the user's answer for a quiz.

        Parameters:
        quiz (Quiz): The quiz to evaluate.
        user_answer (str): The user's answer.

        Returns:
        bool: True if the user's answer is correct, False otherwise.
        """
        return quiz.answer == user_answer

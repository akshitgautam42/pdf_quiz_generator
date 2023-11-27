from typing import List
import requests

class Quiz:
    def __init__(self, question: str, options: List[str], answer: str):
        """
        Initializes a Quiz object.

        Parameters:
        question (str): The question for the quiz.
        options (List[str]): The options for the quiz.
        answer (str): The answer for the quiz.
        """
        self.question = question
        self.options = options
        self.answer = answer

class QuizGenerator:
    def __init__(self):
        """
        Initializes a QuizGenerator object.
        """
        self.quizzes = []

    def generate_quiz(self, content: str) -> List[Quiz]:
        """
        Generates quizzes from the given content.

        Parameters:
        content (str): The content to generate quizzes from.

        Returns:
        List[Quiz]: The generated quizzes.
        """
        # Here we assume that there is an API endpoint that generates quizzes from the given content
        response = requests.post('http://api.example.com/generate_quiz', json={'content': content})
        quizzes_data = response.json()

        for quiz_data in quizzes_data:
            quiz = Quiz(quiz_data['question'], quiz_data['options'], quiz_data['answer'])
            self.quizzes.append(quiz)

        return self.quizzes

import streamlit as st
from pdf_reader import PDFReader
from quiz_generator import QuizGenerator
from quiz_evaluator import QuizEvaluator

def main():
    st.title("PDF Quiz Generator")

    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    if uploaded_file is not None:
        pdf_reader = PDFReader()
        content = pdf_reader.read_pdf(uploaded_file)

        quiz_generator = QuizGenerator()
        quizzes = quiz_generator.generate_quiz(content)

        quiz_evaluator = QuizEvaluator()
        for quiz in quizzes:
            st.markdown(f"**{quiz.question}**")
            user_answer = st.selectbox("Choose an answer", quiz.options)
            if st.button("Submit"):
                if quiz_evaluator.evaluate_quiz(quiz, user_answer):
                    st.success("Correct answer!")
                else:
                    st.error("Wrong answer!")

if __name__ == "__main__":
    main()

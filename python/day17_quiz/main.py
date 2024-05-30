from question_model import Question
from data import question_data
from quiz_brain import Quizbrain

question_bank = []
# new_question = Question(question['text'], question['answer'])
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank[0].text)

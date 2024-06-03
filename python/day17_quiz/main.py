from question_model import Question
from data import question_data
from quiz_brain import Quizbrain


question_bank = []
# new_question = Question(question['text'], question['answer'])
for question in question_data:
    # question_text = question['text']
    question_text = question['question']
    # question_answer = question['answer']
    question_answer = question['correct_answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank[0].text)
quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was {quiz.score}/{quiz.question_number}")

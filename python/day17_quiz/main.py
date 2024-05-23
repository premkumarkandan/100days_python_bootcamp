from data import question_data


class Question:

    def __init__(self, q_text, q_answer):
        self.text = q_text
        self.answer = q_answer


# new_q = Question("aardf", "False")
# new_q = []
# print(new_q.text)
# print(new_q.answer)
question_bank = []


for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

print(question_bank)
# print(new_q)

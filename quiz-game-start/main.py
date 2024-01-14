from question_model import Question
from  data import question_data
from quiz_brain import  QuizBrain
question_bank =[]

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)
r = QuizBrain(question_bank)

while r.still_has_question():
    r.next_question()
print("You've completed the quiz")
print(f"your final score was {r.score}/{r.question_number}")
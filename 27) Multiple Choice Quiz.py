from Class_Definition import Question

question_prompts = [
    "What colour are apples? \n(a) Red\n(b) Purple \n(c) Blue \n(d) Green\n",
    "How many members in BTS? \n(a) 6\n(b) 7 \n(c) 8 \n(d) 9\n"
]

questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
            print("Correct!")
    print("You got " + str(score) + "/" + str(len(questions)) + " correct!")

run_test(questions)
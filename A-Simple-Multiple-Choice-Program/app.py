from question import Question

#an array of questions
questions_prompt = ["What color is the sky?\n(a) Blue\n(b) Red\n(c)Yellow\n",
                    "Which vehicle has 4 wheels?\n(a) Bicycle\n(b) Car\n(c) Train\n",
                    "Are you enjoying this?\n(a) No\n(b) Neutral\n(c) Yes\n"
                    ]

#an array of questions and their answers
questions = [
    Question(questions_prompt[0], "a"),
    Question(questions_prompt[1], "b"),
    Question(questions_prompt[2], "c")
]

#runner to run the program
def runner(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

runner(questions)
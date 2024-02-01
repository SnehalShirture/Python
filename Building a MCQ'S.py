from Question import Question

question_prompts = [
     "What color are apples? \n (a) Red/Green \n(b) Purple\n(c) orange\n\n",
     "What color are banana?\n (a) Teal\n(b) Magenta\n(c) Yellow\n\n",
     "What color are Strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n",

]

questions = [

    Question(question_prompts[0],"a")
    Question(question_prompts[1],"c")
    Question(question_prompts[2],"b")
]
def run_test(questions):
    score = 0
    for question in question:
        answer = input(question.prompt)
        if answer == question.answer:
            score +=1
    print("You got "+ str (score)+"/"+str(len(question))+"correct")
    
run_test(questions)
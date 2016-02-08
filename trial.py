from selenium import webdriver

browser = webdriver.Firefox()

sky_questions = 'Sky Questions'
water_questions = 'Water Questions'
planet_questions = 'Planet Questions'

questions = [sky_questions, water_questions, planet_questions]

quiz = {sky_questions: [("The sky is blue", True),
                        ("The sky is the entire atomsphere", False),
                        ("For the longest time people thought the sky was infinite", True)],

        water_questions: [("People live in water", False),
                         ("Water is completely eatible", False),
                         ("Most food comes from water", True)],

        planet_questions: [("There are 9 planets in the solar system", True),
                     ("We live in the milky way galaxy", True),
                     ("There are 4 planets covered in ice and 2 planets that are extremely hot", False)]
}

result = {"Correct": 0, "Incorrect": 0}

def get_quiz_choice():
    while True:
        try:
            quiz_number = int(raw_input(
                'Choose the quiz you like\n1 for {}\n2 for {}\n3 for {}\nYour choice:'.format(sky_questions,
                                                                                          water_questions,
                                                                                          planet_questions)))
        except ValueError: 
            print "Not a number, please try again\n"
        else:
            if 0 >= quiz_number or quiz_number > len(quiz):
                print "Invalid value, please try again\n"
            else:
                return quiz_number


def get_answer(question, correct_answer):
    while True:
        try:
            print "Q: {}".format(question)
            answer = int(raw_input("1 for True\n0 for False\nYour answer: "))
        except ValueError:
            print "Not a number, please try again\n"
        else:
            if answer is not 0 and answer is not 1:
                print "Invalid value, please try again\n"
            elif bool(answer) is correct_answer:
                result["Correct"] += 1
                return True
            else:
                result["Incorrect"] += 1
                return False

choice = get_quiz_choice()
quiz_name = questions[choice - 1]
print "\nYou chose the {}\n".format(quiz_name)
quiz_questions = quiz[quiz_name]
for q in (quiz_questions):
    print "Your answer is: {}\n".format(str(get_answer(q[0], q[1])))
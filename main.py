# from colorama import Fore
# import pyfiglet
# from Questions import question_quiz
from logic_functions import *

# def scores():
#     try:
#         quiz_questions = []
#         scores = 'scores.json'
#         with open(scores) as f:
#             json.dump(quiz_questions, f)
#     except:
#         print("This didn't work")



def main_quiz():
        quiz_header()
        quiz_table()
        menu_choice()

main_quiz()
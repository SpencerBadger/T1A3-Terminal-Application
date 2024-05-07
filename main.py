"""
This module contains the main code to execute the quiz.
"""
import pyfiglet, colorama, os
from Questions import *
from userclass import *
from rich.console import Console
from rich.table import Table


def main_quiz():
    os.system('cls' if os.name == 'nt' else 'clear')
    """
    Function for the starting of the quiz. This function will call other functions as required.
    """
    quiz_header()
    quiz_table()
    menu_choice()

def quiz_header():
    """
    (1) Feature - This header being created through use of an external library imported and utilized correctly to display the 'header' for the quiz.
    This utilizes ASCII art.
    """
    result = pyfiglet.figlet_format("Quiz",font= 'sub-zero')
    console.print((result),justify="center")

def quiz_table():
    """
    (2) Feature - This is the generation of a table to display the main menu for the quiz.
    """
    table = Table()
    table.add_column("Option (1)", justify="center")
    table.add_column("Option (2)", justify="center")
    table.add_column("Option (3)", justify="center")
    table.add_row(" Play Quiz","View Highscores"," Exit Game")
    console = Console()
    console.print(table, justify="center")

def menu_choice():
    """
    (3) Feature - This function is for the main menu logic tree. Depending on the user choice a further function will be called accordingly.
    """

    choice = int(input("Please input your choice: "))
    if choice == 1:
        choice_one()
    elif choice == 2:
        choice_two()
    elif choice == 3:
        choice_three()

def choice_one():
    """
    (Choice One) This function when invoked will clear the previous screen and then the player will navigate to 
    the main menu of the game and perform a function call on question_quiz_warcraft()
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    question_quiz_warcraft()
        # os.system('cls' if os.name == 'nt' else 'clear')
        # print("Please select which quiz you would like to play:")
        # print("(1) Warcraft ", "(2) Fallout ","(3) Emptiness")
        # quiz_selection = int(input("Which quiz would you like to play?"))
        # if quiz_selection == 1:
            
        # elif quiz_selection == 2:
        #     print("Option 2")
        # elif quiz_selection == 3:
        #     print("Option 3")

def choice_two():
    '''
    (Choice Two) This function when invoked will clear the previous screen and then the player will navigate to 
    the View the highscores and the function call will load the scoredboard from csv.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You have chosen to view highscores!")
    # insert code to display the highscore board.  
    escape = input("Would you like to exit the program? (y/n)")
  

def choice_three():
    """
    (Choice Three) When invoked this function will exit the game.
    """
    os.system('cls' if os.name == 'nt' else 'clear')
    print("You have chosen to exit the game!")
    exit()


main_quiz()
"""
Here I am invoking the main_quiz function to start the quiz.
"""
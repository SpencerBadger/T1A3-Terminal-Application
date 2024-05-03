import quiz_Header
import pyfiglet
import os
import colorama

from quiz_Header import quiz_header
from colorama import Fore

def main_quiz():
    try:
        quiz_header()
        print(Fore.BLUE + "\n(1) Play Quiz", "\n(2) View Highscores", "\n(3) Register User", "\n(4) Exit Game")
        choice = int(input("Please input your choice: "))
        if choice == 1:
            print("You have chosen to play the quiz!")
            # quiz_selection()
        elif choice == 2:
            print("You have chosen to view highscores!")
            # view_highscores()
        elif choice == 3:
            print("You have chosen to register a user!")
            # register_user()
        elif choice == 4:
            print("You have chosen to exit the game!")
            exit()

    except ValueError as e:
            error_response = pyfiglet.figlet_format("\n You have entered an invalid choice! \n", justify="center")
            print(Fore.RED + error_response)
            print("Please Enter a valid choice.")
            return(main_quiz())

main_quiz()

from colorama import Fore
from quizSelection import quiz_selection
import pyfiglet
import csv

def quiz_header():
    from pyfiglet import figlet_format
    from colorama import Fore

    result = pyfiglet.figlet_format("Quiz",font= 'slant', justify="center")
    return (print(Fore.BLUE + result))

def main_quiz():
    try:
        quiz_header()
        print(Fore.BLUE + "\n(1) Play Quiz", "\n(2) View Highscores","\n(3) Exit Game")
        choice = int(input("Please input your choice: "))
        if choice == 1:
            print("You have chosen to play the quiz!")
            quiz_selection()
        elif choice == 2:
            print("You have chosen to view highscores!")
            def view_highscores():
                    try:
                        with open('scores.csv') as f:
                            for line in csv.DictReader(f, fieldnames=()):
                                print(line)
                    except:
                        print("This didn't work")
            view_highscores()
            main_quiz()

        elif choice == 3:
            print("You have chosen to exit the game!")
            exit()
        else:
            main_quiz()
    except ValueError:
        error_response = pyfiglet.figlet_format("\n You have entered an invalid choice! \n", justify="center")
        print(Fore.RED + error_response)
        print("Please Enter a valid choice.")
        return(main_quiz())


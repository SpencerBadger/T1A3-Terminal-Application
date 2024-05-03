# import pyfiglet module 
import pyfiglet
import colorama

def quiz_header():
    from pyfiglet import figlet_format
    from colorama import Fore

    result = pyfiglet.figlet_format("Quiz",font= 'slant', justify="center")
    return (print(Fore.BLUE + result))
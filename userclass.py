"""
This module contains various classes related to a user data for the the quiz scoreboard.
"""
import Questions
import csv
import os
from rich.console import Console

console = Console()

class UserClass:
    """
    A class to represet the user.

    ...

    Attributes
    ----------
    first_name : str
        first name of the user.
    last_name : str
        family name of the user.
    score : int
        the user's score.

    Methods
    ----------
    show():
        Prints the users name and score once completing the quiz.
    save_highscores():
        Saves the users name and score to a csv file.
    """
    def __init__(self, first_name: str, last_name: str, score: int):
        """
        Constructs all the necessary attributes for the person object.

        Parameters
        ----------
        first_name : str
            first name of the user.
        last_name : str
            family name of the user.
        score : int
            the user's score
        """
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        
    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        (console.print(f"Hi", self.first_name, self.last_name,"congratulations!!! your score is:", self.score))
        """
        Prints the users name and score once completing the quiz.

        Parameters
        ----------
        None
        
        Returns
        ----------
        None
        """

    def save_highscores(self):
        with open ('highscores.csv', 'a',newline='') as f:
            write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            write.writerow([self.first_name, self.last_name, self.score])
        """
        This method saves the users data to the highscores.csv

        Parameters
        ----------
        None
        
        Returns
        ----------
        None
        """ 
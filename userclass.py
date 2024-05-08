"""
This module contains various classes related to a user data for the the quiz scoreboard.
"""


import Questions, csv, os

class UserClass:
    """This is the documentation for the __init__ method."""

    def __init__(self, first_name: str, last_name: str, score: int):
        """
        Parameters
        ----------
        first_name : str
        last_name : str
        score : int
        """
        self.first_name = first_name
        self.last_name = last_name
        self.score = score
        
    def show(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        (print(f"Hi", self.first_name, self.last_name,"congratulations!!! your score is:", self.score))
        """
        This method generates a message when called providing the users 
        Parameters
        ----------
        first_name : str
        last_name : str
        score : int
        """

    def save_highscores(self):
        with open ('highscores.csv', 'a',newline='') as f:
            write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
            # write.writerow(["First Name", "Last Name", "Score"])
            write.writerow([self.first_name, self.last_name, self.score])
            
        """
        This method is for when the user saves their data to the scoreboard.
        """        

    def view_highscores(self):
        with open ('highscores.csv','r') as f:
                 csvreader = csv.reader(f)
                 rows = []
                 for row in csvreader:
                    rows.append(row)
                    print(rows)
        """
        This method is for when the user wants to see the scoreboard.
        """          


import Questions
import csv

class UserClass:
    def __init__(self, first_name: str, last_name: str, score: int):
        self.first_name = first_name
        self.last_name = last_name
        self.score = score

    def show(self):
        (print(f"Hi", self.first_name, self.last_name, "your score is:", self.score))

    def view_highscores(self):
            with open ('highscores.csv', 'a',newline='') as f:
                write = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
                write.writerow(["First Name", "Last Name", "Score"])
                write.writerow([self.first_name, self.last_name, self.score])





        # except FileNotFoundError:
        #     print("File not found")
        # finally:   
        #     with open ('highscores.csv','a', newline='') as my_file:
        #         csv_writter = csv.writer(my_file)
        #         my_data = [[randint(0, 9) for _ in range(10)] for _ in range(10)]
        #         #for each row append it to our CSV file
        #         for row in my_data:
        #         csv_writter.writerow(row)
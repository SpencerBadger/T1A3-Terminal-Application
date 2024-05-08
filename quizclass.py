import Questions
import csv



class Quizzes:
    def __init__(self, quiz_filename):
        self.quiz_filename = quiz_filename

    def file_open(self):
        with open(self.quiz_filename, 'r') as f:
            csv_reader = csv.reader(f,delimiter=",")
            return(csv_reader)

    # def file_reader(self): 
    #     with open(self.quiz_filename, 'r') as f:
    #         csv_reader = csv.reader(f,delimiter=",")
    #         csv_header = next(csv.reader)
    #         for row in csv_reader:
    #             print(csv_header)
    #             print(f[0][0])

warcraft = "warcraft.csv"
file_path = Quizzes(warcraft)
file_path.file_open()

            


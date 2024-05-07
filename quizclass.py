import Questions
import csv



class Quizzes:
    def __init__(self, quiz_filename):
        self.quiz_filename = quiz_filename

        

    # def file_open(self):
    #     with open(self.filename, 'r') as f:
    #         csv_reader = csv.reader(f, delimiter=',')
    #         column_names = []
    #         for row in csv_reader:
    #               column_names.append(row)
    #             print(column_names[0])
                
    def file_open(self):
        with open(self.quiz_filename, 'r') as f:
        csv_reader = csv.reader(f)
            # header = next(csv_reader)
            # rows = []
            # for row in csv_reader:
            #     rows.append(row)
            #     # print(header)
            #     # print(rows[1])
            # i = 0
            # while (i<5):
            #     print(header)
            #     print(rows[i][0])
            #     print(rows[i])
            #     i = i + 1
            print(f[0][0])

warcraft = "warcraft.csv"

file_path = Quizzes(warcraft)
file_path.file_open()
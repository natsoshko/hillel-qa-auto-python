class Student:
    def __init__(self, first_name, second_name, age, avg_score):
        self.first_name = first_name
        self.second_name = second_name
        self.age = age
        self.avg_score = avg_score

    def set_avg_score(self, score_value):
        self.avg_score = score_value

    def show_info(self):
        print(f"Student card: {stud1.first_name} {stud1.second_name}. Age = {stud1.age} and average score = {stud1.avg_score}")



stud1 = Student("Mark", "Tilbury", 21, 65)
stud1.show_info()
#print(f"student: {stud1.first_name} {stud1.second_name}. His age = {stud1.age} and average score = {stud1.avg_score}")

stud1.set_avg_score(80)
stud1.show_info()
#print(f"student: {stud1.first_name} {stud1.second_name}. His age = {stud1.age} and average score = {stud1.avg_score}")
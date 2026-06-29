class Student:
    def __init__(self, first_name, second_name, age, avg_score):
        self.__first_name = first_name
        self.__second_name = second_name
        self.__age = age
        self.__avg_score = avg_score

    def set_avg_score(self, score_value):
        self.__avg_score = score_value

    def get_avg_score(self):
        return self.__avg_score

    def get_first_name(self):
        return self.__first_name

    def get_second_name(self):
        return self.__second_name

    def get_age(self):
        return self.__age

    def show_info(self):
        print(f"Student card: {self.__first_name} {self.__second_name}. Age = {self.__age} and average score = {self.__avg_score}")

stud1 = Student("Mark", "Tilbury", 21, 65)
stud1.show_info()

print("average score is:", stud1.get_avg_score())
stud1.set_avg_score(80)
print("average score updated:", stud1.get_avg_score())
stud1.show_info()
from abc import ABC, abstractmethod
from functools import wraps

class TooManyStudentsError(BaseException):
    def __init__(self, instance):
        super().__init__()
        self.instance = instance
        self.error_msg = self.get_error_msg()

    def get_error_msg(self):
        return f"To many students in {self.instance.number}! Max: {self.instance.max_students_in_group}"

    def __str__(self):
        return self.error_msg


class Human(ABC):
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def __str__(self):
        return f"Name: {self.first_name}. Last name: {self.last_name}. Age: {self.age}. Gender: {self.gender}"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f" Record_book: {self.record_book}"


class Group:

    def __init__(self, number, max_students_in_group=10):
        self.max_students_in_group = max_students_in_group
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= self.max_students_in_group:
            raise TooManyStudentsError(self)
        else:
            self.group.add(student)

    @staticmethod
    def print_result(func):
        @wraps(func)
        def wrapper(group, last_name):
            func_result = func(group, last_name)
            if func_result:
                print(f"{last_name} was removed from {group.number}")
            else:
                print(f"{last_name} not in the group {group.number}!")
            return
        return wrapper

    @print_result
    def delete_student(self, last_name):
        target = None
        for student in self.group:
            if student.last_name == last_name:
                target = student
                break
        if target:
            self.group.remove(target)
        return target

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student

    def get_all_students_str(self):
        return "\n\t\t".join((str(student) for student in self.group))

    def __str__(self):
        all_students = self.get_all_students_str()
        return f'Number: {self.number}\n\t\t{all_students} '


gr = Group('PD1')
for i in range(11):
    student = Student('Male', 30, i, i, 'ANi142')
    gr.add_student(student)

# st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
# st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
# gr = Group('PD1')
# gr.add_student(st1)
# gr.add_student(st2)
# print(gr)
# assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
# assert gr.find_student('Jobs2') is None, 'Test2'
# assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
#
# gr.delete_student('Taylor')
# print(gr)  # Only one student
#
# gr.delete_student('Taylor')  # No error!
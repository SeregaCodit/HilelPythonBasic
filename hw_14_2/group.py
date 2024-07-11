from custom_exceptions import TooManyStudentsError
from functools import wraps


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

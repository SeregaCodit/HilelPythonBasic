from human import Human


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return super().__str__() + f" Record_book: {self.record_book}"

    def __hash__(self):
        return hash(self.__str__())

    def __eq__(self, other):
        return True if self.__dict__ == other.__dict__ else False








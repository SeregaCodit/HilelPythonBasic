from abc import ABC, abstractmethod


class Human(ABC):
    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    @abstractmethod
    def __str__(self):
        return f"Name: {self.first_name}. Last name: {self.last_name}. Age: {self.age}. Gender: {self.gender}"
class Greeting:
    def __init__(self):
        self.__greeting_text = "Hello"
        self.__name = ""

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self.__name = value
        else:
            print("Incorrect name!")

    @property
    def say_hello(self):
        return f"{self.__greeting_text}, {self.__name}!"


if __name__ == "__main__":
    hello = Greeting()
    hello.name = "World"
    print(hello.say_hello)


#
# print("Hello World!")

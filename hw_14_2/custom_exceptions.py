class TooManyStudentsError(BaseException):
    def __init__(self, instance):
        super().__init__()
        self.instance = instance
        self.error_msg = self.get_error_msg()

    def get_error_msg(self):
        return f"To many students in {self.instance.number}! Max: {self.instance.max_students_in_group}"

    def __str__(self):
        return self.error_msg

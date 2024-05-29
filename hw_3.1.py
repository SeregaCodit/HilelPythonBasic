"""
Програма має виконувати прості математичні дії (+, -, *, /). Користувачеві пропонується почерзі ввести числа та дію над
 цими числами, а програма, виходячи з дії, обчислює та друкує результат.

Зробити перевірку на те, що при діленні дільник не дорівнює 0!
"""

available_operations = ["+", "-", "*", "/"]

first_number = float(input("enter first number: "))
second_number = float(input("enter second number: "))
operation = input("enter the operation: ")

if operation not in available_operations:
    result = "Wow! I don`t know this operation!"
elif operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/" and not second_number:
    result = "division by zero!"
else:
    result = first_number / second_number

print(result)

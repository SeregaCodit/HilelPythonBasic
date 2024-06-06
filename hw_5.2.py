"""
Модифікувати калькулятор таким чином, щоб він працював доти, доки користувач цього хоче. Тобто, потрібно робити запит
до користувача на продовження роботи калькулятора після кожного обчислення - якщо користувач ввів yes (можна просто y),
то нове обчислення, інакше - закінчення роботи.
"""

available_operations = ["+", "-", "*", "/"]
while True:
    first_number = float(input("enter first number: ").replace(",", "."))
    second_number = float(input("enter second number: ").replace(",", "."))
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

    print(f"result = {result}")
    ask_user_to_continue = input("let`s do it one more time? (\"yes\", \"y\" \ any other input to exit): " )
    if ask_user_to_continue != "yes" and ask_user_to_continue != "y":
        print("End.")
        break

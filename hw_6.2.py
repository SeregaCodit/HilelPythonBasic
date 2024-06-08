"""
Ваше завдання — написати програму, яка переводить число у формат часу у читальному вигляді.

Користувач повинен ввести число більше або дорівнює 0 і менше ніж 8640000.

Число, яке є кількістю секунд, необхідно перевести в дні, години, хвилини та секунди.

Ну і додатковим завданням є турбота про виведення.

Слово "день" підбирається на основі кількості днів, а години, хвилини і секунди повинні заповнюватися нулями при
одноцифрових значеннях.

Підказка: одна хвилина - 60 сек. , В одній годині 60 * 60 сек, в одній добі 24 * 60 * 60 сек. Тобто використовуючи
функцію divmod або методи поділу // і % вам необхідно знайти відповідну кількість днів, годин, хвилин, а те що
залишиться - це секунди, які менше 60 ;)

"""



result = ""
time = dict(
    seconds={"value": None, "delimiter": 60},
    minutes={"value": None, "delimiter": 60},
    hours={"value": None, "delimiter": 24},
    days={"value": None, "delimiter": None, "text": {"1": "день", "2": "дні", "3": "дні", "4": "дні"}},

)

while True:
    user_input = input("type a number >= 0 and < 8640000, or type \"q\" for exit: ")
    if user_input.isdigit() and 0 <= int(user_input) < 8640000: # спочатку не зрозумів сенес обмеження діапазону вводу, тож написав для будь-якого діапазону
        value = int(user_input)
        break
    elif user_input.lower() == "q":
        print(">.<")
        exit()
    else:
        print(f'[-] "{user_input}" is incorrect value!')

for key in time.keys():
    if time[key]["delimiter"]:
        value, time[key]["value"] = divmod(value, time[key]["delimiter"])
        result = f'{str(time[key]["value"]).zfill(2)}:{result}'
    else:
        result = result[:-1]
        time[key]["value"], value = value, str(value),
        last_two = value[-2:]
        text = time[key]["text"].get(value[-2:] if len(value) > 1 and int(last_two) < 15  else value[-1], "днів")
        result = f'{str(time[key]["value"])} {text}, {result}'

print(result)

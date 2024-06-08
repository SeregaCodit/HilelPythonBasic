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
    # days={"value": None, "delimiter": None, "text": {"днів": (0, 5, 6, 7, 8, 9), "день": (1,), "дні": (2, 3, 4)}},
    days={"value": None, "delimiter": None, "text": {(0, 5, 6, 7, 8, 9): "днів", (1,): "день", (2, 3, 4): "дні"}},

)
while True:
    user_input = input("type a number >= 0 and < 8640000, or type \"q\" for exit: ")
    if user_input.isdigit():
        value = int(user_input)
        if 0 <= value < 8640000: # Користувач повинен ввести число більше або дорівнює 0 і МЕНШЕ ніж 8640000.
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
        time[key]["value"] = value
        # text = time[key]["text"].get(time[key]["value"] % 10, "день")
        text_key = [i for i in time[key]["text"].keys() if value % 10 in i][0]
        result = f'{str(time[key]["value"])} {time[key]["text"][text_key]}, {result}'

print(result)


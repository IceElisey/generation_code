import random


names_character = [
    "Елисей",
    "Татьяна",
    "Вадим",
    "Андрей",
    "Тагир",
    "Раяна",
    "Максим",
    "Николай",
    "Владимир",
    "Владислав"
]
num_pos = random.randint(0,9)
for number in range(10):
    if num_pos == number:
        print("облили игрока:", names_character[num_pos])
    else:
        print(names_character[number])
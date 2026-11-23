from random import choice 
from string import printable


number_password = int(input("какая длина пароля? укажите число "))
password = "".join([choice(printable) for number in range(number_password)])
password = password.replace(" ", choice(printable))
password = password.replace("\n", choice(printable))
password = password.replace("\t", choice(printable))
password = password.replace("\x0b", choice(printable))
password = password.replace("\x0c", choice(printable))
print("ваш новый пароль -- ", password)

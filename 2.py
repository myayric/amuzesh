import random

num_for_random = random.randint(1, 100)
num_from_user = int(input("Угадай число от 1 до 100:>>"))
print(num_for_random)
number_of_guesses = 0
while True:
    if num_for_random == num_from_user:
        print("Ваш номер правильный")
        print(f'Вы пытались угадать число [{number_of_guesses}] раза  ')
        break
    elif num_for_random > num_from_user:
        print("Ваше число меньше угаданного числа:")
        num_from_user = int(input("Попробуйте еще раз:"))
    elif num_for_random < num_from_user:
        print("Ваше число больше угаданного числа:")
        num_from_user = int(input("Попробуйте еще раз:"))
    number_of_guesses += 1

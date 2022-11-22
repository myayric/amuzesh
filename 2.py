import random


num_game = int(input("выбрите вид игр:\n"
                     "[1] Найдти нужное число, с помощью сложения или вычитания\n"
                     "[2] Найдти нужное число, угадав число\n>>"))

# print(num_for_random)
number_of_guesses = 0
while True:
    if not num_game == 1 or not num_game == 2:
        if num_game == 1:
            num_for_random = random.randint(1, 100)
            num_from_user = int(input("Угадай число от 1 до 100:>>"))
            while True:
                number_of_guesses += 1
                if num_for_random == num_from_user:
                    print(">Ваш номер правильный")
                    print(
                        f'>>Угаданное число было [{num_for_random}] \n>>>и вы пытались угадать число'
                        f' [{number_of_guesses}] раза  ')
                    break

                elif num_for_random > num_from_user:
                    print("Ваше число меньше угаданного числа, сколка хотите добовить?")
                    num_from_user = num_from_user + int(input('>>'))
                elif num_for_random < num_from_user:
                    print("Ваше число больше угаданного числа, сколка хотите уменшать?")
                    num_from_user = num_from_user - int(input('>>'))
        elif num_game == 2:
            num_for_random = random.randint(1, 100)
            num_from_user = int(input("Угадай число от 1 до 100:>>"))
            while True:
                number_of_guesses += 1
                if num_for_random == num_from_user:
                    print(">Ваш номер правильный")
                    print(
                        f'>>Угаданное число было [{num_for_random}] \n>>>и вы пытались угадать число'
                        f' [{number_of_guesses}] раза  ')
                    break
                elif num_for_random > num_from_user:
                    print("Ваше число меньше угаданного числа:")
                    num_from_user = int(input("Попробуйте еще раз:"))
                elif num_for_random < num_from_user:
                    print("Ваше число больше угаданного числа:")
                    num_from_user = int(input("Попробуйте еще раз:"))
                    number_of_guesses += 1
            break
        else:
            num_game = int(input(f"ты больной? тебе попросили выбрать между 1 и 2! Почему ты выбрал цифру "
                                 f"[{num_game}]?\n"
                                 "Еще раз прошу тебя, выбери число от 1 до 2!!\n>>"))


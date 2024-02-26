from random import *
#функция проверка условия
def is_valid(s):
    return s.isdigit() and 1<=int(s)<=100
#функция конверта.
def is_valid_num():
    while True:
        r=input()
        if is_valid(r):
            return int(r)
        else:
            print("А может всё-таки введем целое число от 1 до 100?")
            continue
#функции сравнения
def sravnenie():
    count=0
    ra = randint(1, 100)
    while True:
        r=is_valid_num()
        if r<ra:
            print("Ваше число меньше загаданного, попробуйте еще разок")
            count+=1
        elif r>ra:
            print("Ваше число больше загаданного, попробуйте еще разок")
            count+=1
        elif r==ra:
            print("Вы угадали, поздравляем!")
            print(f'Количество ваших попыток равно {count}')
            print("Спасибо, что играли в числовую угадайку. Еще увидимся...")
            break
def continue_game():
    n=input("Хотите продолжить игру?) \n")
    while True:
        if n in "да" or n in "yes":
            return True
        elif n in "нет" or n in "no":
            print("До новых встреч :)")
            return False
        else:
            return False
def game():
    print("Добро пожаловать в числовую угадайку \nВведите число в диапозоне от 1 до 100: ")
    r=sravnenie()
    while True:
        if continue_game() == True:
            ra = randint(1, 100)
            print("Окей, введите снова число в диапозоне от 1 до 100")
            sravnenie()
            continue
        else:
            print("Игра окончена")
            break
game()




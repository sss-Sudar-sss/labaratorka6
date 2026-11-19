import random
from tarfile import LENGTH_LINK


def get_valid_int(text, min_value=1):
    while True:
        try:
            value=int(input(text))
            if value < min_value:
                print("Число не может быть меньше 1")
                continue
            return value
        except ValueError:
            print("Ошибка, введите натуральное число!")


def task_1():
    print("Задание 1")
    N = get_valid_int("Введите количество строк N: ")
    M = get_valid_int("Введите количество столбцов M: ")
    matrix_A=[]
    for i in range(N):
        row=[]
        for j in range(M):
            row.append(random.randint(1,100))
        matrix_A.append(row)
    print("Исходный список А:")
    for row in matrix_A:
        print((row))
    list_S=[]
    for i in range(N):
        row_sum=0
        for j in range(M):
            row_sum+=matrix_A[i][j]
        list_S.append(row_sum)
    print("Список S:")
    print(list_S)
def task_2():
    print("Задание 2")
    colors_dict={  "red": "красный", "green": "зеленый", "blue": "синий", "yellow": "желтый", "black": "черный", "white": "белый", "orange": "оранжевый"}
    print("1) Весь вловарь:")
    for eng,rus in colors_dict.items():
        print(f"{eng}:{rus}")
    print("2) Вывод перевода последнего слова:")
    keys=list(colors_dict.keys())
    last_key=keys[-1]
    last_value=colors_dict[last_key]
    print(f"Последнее слово в словаре: {last_key} -> {last_value}")

def main():
    print("Добрый день! Лабораторная работа 6 (вариант 11)")
    while True:
        print("Меню:")
        print("1. Запустить задание 1")
        print("2. Запустить задание 2")
        print("0. Выход")
        choice=input("Выберите пункт меню (только цифра): ")
        if choice=="1":
            task_1()
        elif choice=="2":
            task_2()
        elif choice=="0":
            print("Работа завершена.")
            print("Хорошего дня!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")
main()
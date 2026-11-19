import random
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


def z_1():
    print("Задание 1")
    N = get_valid_int("Введите количество строк N:")
    M = get_valid_int("Введите количество столбцов M:")
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


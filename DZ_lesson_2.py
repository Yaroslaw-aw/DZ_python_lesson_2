
def zada4a1():
    for x in range(0, 2):
        for y in range(0, 2):
            print(f'{x} | {y} |', int(not x or y))

def zada4a2():
    substring = input('Введите строку: ')
    phrase = input('Введите фразу: ')
    count = 0
    length_substr = len(substring)
    length_phrase = len(phrase)
    for i in range(length_phrase): 
        if phrase[i: i+length_substr] == substring:
            count += 1
    print(count)

def zada4a3():
    n = int(input('Введите число: '))
    i = 1
    result = 1
    while i <= n:
        print(result, end=' ')
        result *= -3
        i += 1
    # numbers = []
    # for i in range(n):
    #     numbers.append(-3**i)
    # print(numbers)    

def zada4a4():
    col = 0
    for i in range(1, 10_001):
        if deliteli(i) == 10:
            col += 1
            print(f'{i}\t', end= '')
    print(f'\n\n{col}')

def deliteli(num: int):
    count = 0    
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count

# Задача 1. Напишите программу, которая принимает 
# на вход число N и выдает список факториалов для чисел от 1 до N.
# пусть N = 4 -> [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def dz1_factoriali():
    n = int(input('Введите число N: '))
    numbers = []
    for i in range(1, n + 1):
        fact = 1
        for j in range(1, i+1):
            fact *= j
        numbers.append(fact)
    print(numbers)

# Задача 2. Выведите таблицу истинности
# для выражения ¬(X ∧ Y) ∨ Z.

def dz2_truth():
    print('X | Y | Z | ¬(X ∧ Y) ∨ Z')
    for x in range(0, 2):
        for y in range(0, 2):
            for z in range(0, 2):
                print(f'{x} | {y} | {z} |', int(not(x and y) or z))

# Задача 3. Даны две строки. Посчитайте сколько раз
# каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

def dz3_srings():
    substring = input('Введите строку: ')
    phrase = input('Введите фразу: ')
    count = []
    simbols = []
    length_substr = len(substring)
    length_phrase = len(phrase)
    for i in range(length_substr):
        num = 0
        simbols.append(substring[i])
        for j in range(length_phrase): 
            if substring[i] == phrase[j]:
                num += 1
        count.append(num) 
        print(f'{simbols[i]} - {count[i]}', end=', ')


# Задача 4. Задайте список из N элементов,
# заполненных числами из промежутка [-N, N].
# Сдвиньте все элементы списка на 2 позиции вправо.
# 3 -> [2, 3, -3, -2, -1, 0, 1]

def dz5_indexes():
    n = int(input('Введите число: '))
    length = n * 2 + 1
    array = []
    for i in range(length):
        array.append(-n + i)
    print(array)
    shift = int(input('Введите число, на которое надо сдвинуть вправо: '))
    for j in range(shift):
        temp = array[-1]
        for k in range(length - 1):            
            array[-1-k] = array[-2-k]
        array[0] = temp
    print(array)




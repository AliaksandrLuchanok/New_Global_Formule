# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты
# вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
import random

import pickle
def task10():
    summ = int(input('Enter the number of coins, please: '))
    heads = 0
    tails = 0 
    smallNumber = 0
    for i in range(summ):
        variable = random.randint(0,2)
        if variable == 0:
            heads +=1
        else:
            tails +=1 
    smallNumber = min(heads, tails)
    print (f'You need to flip = {smallNumber} coins')


def task12():
    summ = float(input('Enter sum of your numbers: '))
    multipl = float(input('Enter multiplication of your numbers: '))
    number1 = summ/2 - ((summ/2)**2 - multipl)**(0.5)
    number2 = summ - number1
    print(f"number1 = {number1} \nnumber2 = {number2}")




def ConvertToDegree (useDegree: int):
    indexes = {"0": "\u2070",
            "1": "\u00B9",
            "2": "\u00B2",
            "3": "\u00B3",
            "4": "\u2074",
            "5": "\u2075",
            "6": "\u2076",
            "7": "\u2077",
            "8": "\u2078",
            "9": "\u2079",
            "-": "\u207B"
            }
    sum = ""
    strUseDegree = str(useDegree)
    for char in strUseDegree:
        sum += indexes[char]    
    return (sum)
    

def task14():
    useNumber = int(input('Enter your number, please: '))
    if useNumber < 2:
        print('Your degree is 0')
    else:
        degree = 1
        result = 0
        while True:
            degree +=1
            result = 2**degree
            if result > useNumber:
                degree -=1
                break              
    print(f'{2}{ConvertToDegree(degree)}')


task10()
task12()
task14()
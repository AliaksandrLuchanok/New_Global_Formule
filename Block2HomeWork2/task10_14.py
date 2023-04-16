def task10():
    summ = int(input('Enter the number of coins, please: '))

    
    multipl = float(input('Enter multiplication of your numbers: '))
    number1 = summ/2 - ((summ/2)**2 - multipl)**(0.5)
    number2 = summ - number1
    print(f"number1 = {number1} \nnumber2 = {number2}")

def task12():
    summ = float(input('Enter sum of your numbers: '))
    multipl = float(input('Enter multiplication of your numbers: '))
    number1 = summ/2 - ((summ/2)**2 - multipl)**(0.5)
    number2 = summ - number1
    print(f"number1 = {number1} \nnumber2 = {number2}")


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


def degree(a: int):
    degrees = ""
    temp = str(a)
    for char in temp:
        degrees += indexes[char] or ""
    return "a = " + temp + degrees


if __name__ == "__main__":
    print(degree(1024))
    print(degree(-1024))
    print(degree(int(input("Введите число: "))))





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

               
print(f'{}')


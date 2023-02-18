import math
def calc(x,y,operation):
    if operation == 1:
        return x+y
    elif operation == 2:
        return x-y
    elif operation == 3:
        return x*y
    elif operation == 4:
        return x/y
    elif operation == 5:
        return math.e**(x+y)
    elif operation == 6:
        return math.sin(x+y)
    elif operation == 7:
        return math.cos(x+y)
    elif operation == 8:
        return x**y
    else:
        print("Выберите число из диапазона!")

print("Введите переменную A: ", end = "")
x = float(input())
print("Введите переменную B: ", end = "")
y = float(input())
print("Список операций:" , "\n", "1. +", "\n", "2. -", "\n", "3. *", "\n", "4. /", "\n", "5. e^x+y", "\n", "6. sin(x+y)", "\n", "7. cos(x+y)", "\n", "8. x^y")
print("Выберите действие: ", end = "")
operation = int(input())
print("Результат операции: ", calc(x,y,operation))
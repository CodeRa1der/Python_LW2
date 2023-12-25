a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
symb = input("Введите знак (+, -, *, /): ")
result = 0

if symb == "+":
    result = a + b
    print("Результат:", result)
elif symb == "-":
    result = a - b
    print("Результат:", result)
elif symb == "*":
    result = a * b
    print("Результат:", result)
elif symb == "/":
    result = a / b
    print("Результат:", result)
else:
    print("Введён некорректный знак")

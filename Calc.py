a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
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

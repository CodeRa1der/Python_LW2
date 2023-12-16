a = int(input("Введите первое целое число: "))
b = int(input("Введите второе целое число: "))
symb = input("Введите знак (+, -): ")
result = 0

if symb == "+":
    result = a + b
    print("Результат:", result)
elif symb == "-":
    result = a - b
    print("Результат:", result)
else:
    print("Введён некорректный знак")

prodolzhit = 'y'
while prodolzhit == 'y': 
    a = float(input("Введите число a: "))
    op = input("Введите операцию (+, -, *, /): ")
    b = float(input("Введите число b: "))

    if op == "+":
        print("Результат: ", a + b)
        prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>>")
    elif op == "-":
        print("Результат: ", a - b)
        prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>>")
    elif op == "*":
        print("Результат: ", a * b)
        prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>>")
    elif op == "/":
        if b != 0:
            print ("Результат: ", a / b)
        else:
            print("Error: деление на 0!")
        prodolzhit = input("Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить>>")
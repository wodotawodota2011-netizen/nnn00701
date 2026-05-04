def calculator():
    print("Простой калькулятор")
    print("Операции: +  -  *  /")

    while True:
        try:
            a = float(input("Введите первое число: "))
            op = input("Введите операцию: ")
            b = float(input("Введите второе число: "))

            if op == "+":
                result = a + b
            elif op == "-":
                result = a - b
            elif op == "*":
                result = a * b
            elif op == "/":
                if b == 0:
                    print("Ошибка: деление на ноль")
                    continue
                result = a / b
            else:
                print("Неизвестная операция")
                continue

            print("Результат:", result)

        except ValueError:
            print("Ошибка: вводите только числа")

        again = input("Продолжить? (y/n): ").lower()
        if again != "y":
            break

calculator()

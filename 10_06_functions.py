def calc(a, op, b):
    if op == "+":
        return a + b    
    elif op == "-":
        return a - b     
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a/b 
        else:
            return "error"
            
result = calc(5, '+', 5)
print(result)



def register(name, last_name, phone, email):
    print("Зарегистрирован новый клиент ")
    print("Имя клиента", name)
    print("Фамилия", last_name)
    print("Телефон", phone)
    print("Почта", email)
client1 = register("Лариса", "Леопольдова", "+79001112233", "abc@abc.com")



def zabirat_zakaz_na_wb():
    print("Открываем приложение WB")
    print("Выбираем заказ")
    print("Оформляем выбранный тип заказа")
    print("Ожидаем получения")
    print("Забираем заказ")
instruction = zabirat_zakaz_na_wb()


def zabirat_zakaz_na_WB(step1, step2, step3, step4):
    print("Шаги использования приложения:")
    print(step1, "Выбираем заказ")
    print(step2, "Оформляем выбранный тип заказа")
    print(step3, "Ожидаем получения")
    print(step4, "Забираем заказ")
instruction = zabirat_zakaz_na_WB ("Шаг 1:", "Шаг 2:", "Шаг 3:", "Шаг 4:")


tovar_podoshel = input ("Товар подошел? нажмите любую клавишу" \
"")
def zabirat_zakaz_na_WB(step1, step2, step3, step4, tovar_podoshel = True):
    print("Шаги использования приложения:")
    print(step1, "Выбираем заказ")
    print(step2, "Оформляем выбранный тип заказа")
    print(step3, "Ожидаем получения")
    print(step4, "Забираем заказ")
instruction = zabirat_zakaz_na_WB ("Шаг 1:", "Шаг 2:", "Шаг 3:", "Шаг 4:")
if  tovar_podoshel: False
print ("Товар не подошел? Вы можете оформить возврат!")
if tovar_podoshel:True
print ("Товар подошел! Приятного пользования")

    

 
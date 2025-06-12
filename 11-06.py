def zabirat_zakaz_na_WB(step1, step2, step3, step4):
    print("Шаги использования приложения:")
    print(step1, "Выбираем заказ")
    print(step2, "Оформляем выбранный тип заказа")
    print(step3, "Ожидаем получения")
    print(step4, "Забираем заказ")
instruction = zabirat_zakaz_na_WB ("Шаг 1:", "Шаг 2:", "Шаг 3:", "Шаг 4:")
print("Для продолжения выберите нужную функцию: ")
while True:
    print ("1. Заказ подошел")
    print("2. Заказ не подошел")
    choise = input ("Выбор: ")
    if choise == "1":
        print ("Приятного пользования!")
    elif choise == "2":
        print ("Вы можете оформить возврат в Вашем пункте выдачи!")
    break

    
    
2
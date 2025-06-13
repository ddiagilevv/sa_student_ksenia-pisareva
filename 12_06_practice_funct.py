#1. функция для ввода имени ask_name(), возвращающая имя
#2. функция для ввода возраста ask_age(), возвращающая возраст
#3. функция для ввода города ask_city(), возвращающая город
#4. функция для ввода хобби ask_hobbies(), возвращающая hobbies (в виде list)

#5. Функция для вывода анкеты show_profile(name, age, city, hobbies)
#6. Главная функция
#main()



def ask_name():
    name = input("Введите имя: ")
    return name

def ask_surname():
    surname = input("Введите фамилию: ")
    return surname

def ask_age():
    age = input("Введите возраст: ")
    return age

def ask_city():
    city = input("Введите город: ")
    return city

def ask_hobbies():
    hobbies = []
    while True:
        hobby = input("Введите Ваше хобби/для выхода введите \".\"")
        if hobby == ".":
            break
        hobbies.append(hobby)
    return hobbies

def show_profile(initials, age, city, hobbies):
    print("Анкета")
    print("Фамилия, Имя:", initials)
    print("Возраст", age)
    print("Город:", city)
    print("Ваши хобби", hobbies)

def main():
    print("Привет, давай заполним анкету!")
    name = ask_name()
    surname = ask_surname()
    age = ask_age()
    city = ask_city()
    hobbies = ask_hobbies()
    name_and_surname = surname + " " + name 
    show_profile(name_and_surname, age, city, hobbies)

main()

    



        




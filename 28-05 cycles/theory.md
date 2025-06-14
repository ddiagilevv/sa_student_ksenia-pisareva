циклы в С++ и Python

Циклы - фундаментамельная конструкция, позыволяющая выполнять многократно один и тот же участок кода

# for
```c++
for (int i = 0; i <= 5; i++){
    cout << i << endl;
}
```
0
1
2
3
4
5

традиционный счетный цикл
инициализация; условие; шаг
часто используется с массивами

```python
for i in range(5):
    print(i)
```
цикл по итерируемым объектам
range(start, stop[, stop]) - аналог счетного for в С++

array a = [2, 4, 6, 7. 1];
list names = ["Саша", "Ваня", "Петя"]
```python
for name in names:
    print(name)
```
Саша
Ваня
Петя



# while - ЦИКЛ С ПРЕДУСЛОВИЕМ
одна из основных управляющих конструкций, предназначенная для повторения блока кода, 
ПОКА выполняется условие.
Идеально подходит для задач, где количество повторений заранее неизвестно.

```c++
while (условие){
    //тело цикла
}
```

```python
while условие:
    // тело цикла
```

как работает while:
1) проверяется условите
2) если условие true - выполняется тело цикла
3) после выполнениея тела цикла - снова проверяется условие
4) когда(если) условие становится false - цикл завершается

```c++
int i = 0;
while (i < 5) {
    cout << i << endl;
    i++; // i = i + 1. Инкремент 
}
```

```python
i = 1
while i < 5:
    print(i)
    i += 1
```

пример:
password = None;
while password != 1234:
    password = int(input("введите пароль: "))

Также, в python есть управляющие операторы
break - немедленно завершает цикл
continue - пропускает оставшуюся часть тела и переходит к след. итерации
else - выполняется если цикл завершен без break

```python
i = 0
while i < 10:
    i += 1
    if i == 5:
        continue
    if i == 8:
        break
    print(i)
```

сравнение в c++ и в python
В с++ требуется обязательно объявлять переменные. В python - нет, потому что в питоне - динамическая типизация
в с++ условие обязательно в круглых скобках. А В ПИТОНЕ НЕТ
тело цикла в с++ внутри {}
тело цикла в питоне "оформляется" через отступы
поддержка else - уникальная особенность python

бесконечный цикл
```c++
while(true){
    // тело цикла
}
```

```python
while True:
    // тело цикла
```

ВАЖНО не забывать делать инкрементацию/декрементацию
ПРИМЕР ОШИБКИ
```python
i = 0
while i < 5:
    print(i)
    # i += 1 забыто - будет бесконечный цикл!!!!!!!!!!!!!!!
```
в с++ тоже самое

также, можем делать не инкремент, а декремент
```c++
int i = 10;
while (i > 0){
    cout << i;
    i--; // i = i - 1
}
```
где используется цикл while?
- ожидание события (ввод с клавиатуры, отклик от сервера)
- чтение файла (while not file.eof())
- в играх: ПОКА игрок жив, пока не закончился уровень
- валидация данных

```python
while True:
    print("1. Start")
    print("2. Help")
    print("3. Exit")

    choise = input("Select: ")

    if choise == "1":
        print("Game started")
    elif choise == "2":
        print("Help menu")
    elif cloise == "3":
        break
    else:
        print("Invalid choise!")
```



# do-while ЦИКЛ С ПОСТУСЛОВИЕМ
Тело цикла выполняется минимум 1 раз, затем проверяется условие
В Python - ОТСУТСТВУЕТ
```c++
do{
    //тело цикла
} while (условие);
```

как работает do...while
1. сначала выполняется тело цикла
2. потом проверяется условие
3. если условие истинно - тело цикла выполняется снова
4. иначе - выходим из цикла

```c++
int i = 0;
while (i != 0){
    cout << i;
}
не выведет ничего
```

```c++
int i = 0;
do {
    cout << i;
} while  (i != 0)
вывод:
0
```

```c++
int number;
do {
    cout << "введите положительное число" << endl;
    cin >> number;
} while (number <= 0);

// ДАЖЕ ЕСЛИ пользователь сразу введет корректное число - тело цикла выполнится один раз!
// а затем цикл завершится
```
# Массивы

Массив - структура данных , представляющая собой набор однотипных элементов.
Элементы расположены в памяти последовательно. МАссив позволяет хранить, обрабатыват и быстро получать доступ к данным по индексу

```c++
#include <iostream>
using namespace std;

int main(){
    int massiv[5]; // объявление массива из 5-и элементов

    // инициализация
    massiv[0] = 10; // инициализация 1го элемента

    // инициализация при объявлении
    int arr[5] = {89, 245, 781, 1, -89};

    cout << arr[2]; // выведет 781
    

    return 0;
}

```

- размер должен быть известен во время компиляции (в статических массивах)
- хранится в непрерывной области памяти
- индексация с нуля
- нельзя напрямую изменить размер после создания

многомерные массивы:
```c++
int matrix[2][3] = {
    {76, 2, 5},
    {3, 92, 0}
}

cout << matrix[1][2]; // 0
cout << matrix[1][1]; //92
cout << matrix[0][0]; //76
```

---

В Python нет массивов, однако библиотека NumPy предоставляет массив ndarray
```В ТЕРМИНАЛЕ!
pip install numpy
```

```python
import numpy as np

massiv = np.array([89, 245, 781, 1, -89])
print(arr[0]) # 89
```

многомерные массивы:
```python
matrix = np.array(
    [
        [76, 2, 5],
        [3, 92, 0]
    ]
)
print(matrix[1][2]) # 0
print(matrix[1][1]) # 92
print(matrix[0][0]) # 76
```

---

сумма всех элементов массива

```c++
int arr[5] = {89, 245, 781, 1, -89};
int sum = 0;
for (int i = 0; i < 5; i++){
    sum = sum + arr[i];
}
cout << "сумма=" << sum << endl;
```

```python
massiv = np.array([89, 245, 781, 1, -89])
sum = np.sum(arr)
print(sum)

# ИЛИ print(np.sum(arr)) без создания переменной sum
```

---
Срезы
В С++ нет встроенной поддержки. Только вручную.
В Python:
```python
submassiv = arr[60:65]
```

numpy также предоставляет доп. средства по работе с массивами, в т.ч. для алгебры 

---

переборы
с++:
```c++
int arr[5] = {89, 245, 781, 1, -89};
for (int i = 0; i < 5; i++){
    cout << "arr[" << i << "] = " << arr[i] << endl;
}

int rows = 2;
int columns = 3
int matrix[rows][columns] = {
    {76, 2, 5},
    {3, 92, 0}
}

for (int i = 0; i < rows; i++){
    for (int j = 0; j < columns; j++){
        cout "matrix[" << i << "][" << j << "] = " << matrix[i][j] << endl;
    }
}
```

```python
import numpy as np
massiv = np.array([89, 245, 781, 1, -89])

// итерации по значениям
for value in massiv:
    print(value)

// итерации по индексам
for i in range(len(massiv)):
    print(f"massiv[{i}] = {massiv[i]}")

// перебор с enumerate (значение и индекс)
for i, value in enumerate(massiv)
    print(f"индекс: {i}, значение: {value}")
```

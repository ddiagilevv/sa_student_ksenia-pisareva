#include <iostream>
using namespace std;
int main () {
    cout << "введите 1ое число: ";
    сin >> a;

    cout << "введите операцию (+, -, *, /)";
    cin >> op;

    cout << "введите 2ое число: ";
    cin >> b;

    if (op == '+') {
        cout << "Результат сложения: " (a + b) << endl;
     } else if (op == '-') {
        cout << "Результат вычитания: " (a - b) << endl;
     } else if (op == '*') {
        cout << "Результат умножения: " (a * b) << endl;
     } esle if (op == /) {
        if (b = 0){
            cout << " Результат деления: " (a / b) << endl;
        } else {

            cout << " Ошибка: нельзя делить на 0!" << endl;
        }
        return 0;

  
#include <iostream>
using namespace std;
int main () {
    double a, b;
    char op, prodolzhit;
    string str;

    while (prodolzhit == 'y') {
    cout <<"введите 1ое число: ";
    cin >> a;
    

    cout <<"введите операцию (+, -, *, /)";
    cin >> op;

    cout <<"введите 2ое число: ";
    cin>>b;
    

    if (op == '+'){
        cout <<"Результат сложения: " << (a + b)<< endl;
    } else if (op == '-'){
        cout <<"Результат вычитания: "<< (a - b)<< endl;
    } else if (op == '*'){
        cout <<"Результат умножения: "<< (a * b)<< endl;
    } else if (op == '/'){
        if (b == 0){
            cout <<"Ошибка: деление на 0!"<< endl;
        } else {
            cout <<" Результат деления: "<< (a / b)<< endl;
         }
    }
    cout << "Введите 'y', чтобы продолжить, или любую клавишу, чтобы завершить" << endl;
    cin >> prodolzhit;

    }
return 0;
}
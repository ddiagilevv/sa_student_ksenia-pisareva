#include <iostream>
using namespace std;
int main () {
    double a, b;
    char op;
    string str;

    while (true) {
    cout <<"введите 1ое число: ";
    cin >> a;
    

    cout <<"введите операцию (+, -, *, /)";
    cin >> op;

    cout <<"введите 2ое число: ";
    cin>>b;
    if (op == 'x'){
        cout << "Выход из программы нажмите 'x'";
        break;
    }

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
    }
return 0;
}
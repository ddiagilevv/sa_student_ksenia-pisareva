//to do: доделать
#include <iostream>
#include <string>
#include <vector>
using namespace std;


string ask_name() {
    string name;
    cout << "Введите имя: ";
    getline(cin, name);
    return name;
}
string ask_surname(){
    string surname;
    cout << "Введите фамилию: " ;
    getline(cin, surname);
    return surname;
}
int ask_age(){
    int age;
    cout <<"";
    cin >> age;
    return age;
}
string ask_city(){
    string city;
    cout <<"Город: ";
    getline(cin, city);
    return city;
}
vector<string> ask_hobbies(){
    vector<string> hobbies;
    cout << "Укажите хобби: ";
    while (true) {
        string hobby;
        cin >> hobby;
        if (hobby == ".") break;
        hobbies.push_back(hobby); //while {...}
    }
    return hobbies;
}
void show_profile(string initials, int age, string city, vector<string> hobbies) {
    cout << "Привет, давай познакомимся!" << endl;
    cout << "ФИО: " << initials << endl;
    cout << "Возраст: " << age << endl;
    cout << "Город: " << city << endl;
    cout << "Хобби: " << hobbies << endl; 
}

int main() {
    cout << "Привет, давай заполним анкету!" << endl;
    string name = ask_name();
    string surname = ask_surname();
    int age = ask_age();
    string city = ask_city();
    vector<string> hobbies = ask_hobbies();
    string name_and_surname = surname + " " + name;
    show_profile(name_and_surname, age, city, hobbies);

return 0;
}


#include <iostream>
#include <string>
using namespace std;

int main() {
    std::string Initials;
    std::string Age;
    std:: string City;
    std::string hobby;

    std::cout << "Введите Ваши ФИО:";
    std::getline(std::cin, Initials);

    std::cout << "Введите Ваш возраст:";
    std::cin.ignore();
    std::getline(std:: cin, Age);

    std::cout << "Введите Ваш город:";
    std:: cin.ignore();
    std::getline(std:: cin, City);

    std::cout << "Введите Ваше хобби:";
    std:: cin.ignore();
    std::getline(std:: cin, hobby);

    std::cout << "ФИО: " << Initials << std::endl;
    std::cout << "Возраст: " << Age << std::endl;
    std::cout << "Город: " << City << std:: endl;
    std::cout << "Хобби: " << hobby << std::endl;

return 0;
}



  
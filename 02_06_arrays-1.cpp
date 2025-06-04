#include <iostream>
#include <limits>
using namespace std;

int main(){
    int matrix[5][5] = {
        {76, 2, 5, 19, 24},
        {3, 92, 0, 3, 4},
        {32, 48, 32, 16, 47},
        {1, 10, 64, 74, 84},
        {99, 88, 77, 66, 55}
    }; 

    //вывод массива на экран
    for (int i = 0; i < 5; i++){
        for (int j = 0; j < 5; j++){
            cout << "matrix[" << i <<"][" << j <<"] = " << matrix[i][j] << ", " << endl;
            
        } 
        cout << endl;
    }
    std::cout << "Нажмите Enter для выхода..." << std::endl;
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::cin.get();
    return 0;
}
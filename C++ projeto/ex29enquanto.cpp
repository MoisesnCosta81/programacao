#include <iostream>
#include <cstdlib>

using namespace std;

int main () {

    int num = 0;
    while (num <= 100) {
        cout << num << endl;
//        num = num + 1;
//        num +=1;
        num++;
    }

    int num2 = 100;
    while (num >= 0) {
        cout << num << endl;
//        num = num - 1;
//        num -=1;
        num--;
    }


std::cout << "\nPressione Enter para limpar o terminal...\n";
    std::cin.ignore(); // Limpa o buffer de entrada
    std::cin.get();    // Espera o Enter

    system("clear"); // Limpa o terminal no Linux
return 0;
}

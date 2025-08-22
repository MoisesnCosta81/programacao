#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    int i = 0;
    for(int i = 100; i >= 0; i--) {
        cout << i << endl;       
    }


    cout << "---->>>> ----- <<<<< -----" << endl;


    int i2 = 100;
    while (i2 >= 0) {
        cout << i2 << endl;
        i2--;
    }


std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux
return 0;
}

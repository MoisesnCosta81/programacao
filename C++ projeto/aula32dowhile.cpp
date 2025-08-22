#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    cout << "----- >>>>> Do While <<<<< -----" << endl;

    int i = 0;
    do{
        i++;
        cout << "O valor da variável i é: " << i << endl;

    }while(i>10);

    cout << "----- >>>>> While <<<<< -----";

    int i2 = 0;
    while (i2>=10) {
        i2++;
    cout << "O valor da variável é: " << i2 << endl;
    }

std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux
return 0;
}

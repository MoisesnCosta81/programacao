#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    int n1, n2, soma, sub, mult, div;

    cout << "Seja bem vindo a nossa calculadora!" << endl;
    cout << "Digite o primeiro número: ";
    cin >> n1;
    cout << "Digite o segundo número: ";
    cin >> n2;

  
    cout << "A soma é: " << n1 + n2 << endl;
    cout << "A subtração é: " << n1 - n2 << endl;
    cout << "A multiplicação é: " << n1 * n2 << endl;
    cout << "A divisão é: " << n1 / n2 << endl; 
    cout << "O resto da divisão é: "<< n1 % n2 << endl;
    

std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux

return 0;
}
 
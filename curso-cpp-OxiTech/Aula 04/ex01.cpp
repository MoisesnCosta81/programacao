/*AULA4 - EX01
Escreva um programa que solicite um número inteiro 
e imprima os 10 primeiros multiplos desse número:*/

#include <iostream>
#include <cstdlib>// bilbioteca para limpar o terminal
using namespace std;

int main() {

    
    int num;
    cout << "Digite um número inteiro: " ;
    cin >> num;

    cout << "Os 10 primeiros mútiplos de "<< num << " são: " << endl;

    for (int i = 1; i <= 10; ++i) {
        int multiplo = num * i;
        cout << num << " x " << i << " = " << multiplo << endl;
    } 

    
    
std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux


return 0;
}

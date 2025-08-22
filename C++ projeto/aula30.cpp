#include <iostream>
#include <cstdlib>

using namespace std;

/*
1 - Perguntar qual a tabuada para o usuário;
2 - Implementação de um laço de repetição FOR;
3 - Imprimir a tabuada na tela.*/

int main() {

cout << "Digite um número para ver a tabuada: ";
int n = 0;
cin >> n;

for (int i = 1; i <= 10; i++) {
    cout << i << " x " << n << " = " << i*n << endl;
}

std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux

return 0;
}

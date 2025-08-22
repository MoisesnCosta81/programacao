//Escreva um pograma que leia dois números  inteiros e informa qual é o maior. Se os números forem iguais imprima qualquer um deles.
// is = se / else if = se não, se / else = se não

#include <iostream>

using namespace std;

int main() {

float n;
float n2;

cout << "Digite um número inteiro: ";
    cin >> n;

cout << "Digite outro número inteiro: ";
    cin >> n2;

if (n > n2) {
        cout << "\nO número digitado (" << n << ")é maior que: " << n2 << ".\n";
    }
else if (n2 > n) {
        cout << "\nO número digitado (" << n2 << ") é maior que: " << n << ".\n";
    }
else {
        cout << "\nOs números são iguais:" << n << "=" << n2 << ".\n";
    }

cin.ignore();// Limpa o buffer de entrada para que cin.get() funcione
    // Espera o usuário pressionar Enter antes de limpar a tela
std::cout << "\n--- Pressione ENTER para continuar e limpar a tela ---" << std::endl;
std::cin.get();

    
system("clear");// Comando para limpar a tela do terminal

return 0;
}

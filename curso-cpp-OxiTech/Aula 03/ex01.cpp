// Faça um programa que leia o ano de nascimento do usuário e o ano atual, calcule a idade e informar:
// 1) Quantos anos terá no ano atual:
// 2) Se ele já pode tirar a habilitação(idade mínima: 18 anos)

# include <iostream>
#include <cstdlib> // Necessário para o comando system()

using namespace std;

int main () {

    int nascimento;
    int anoatual;

    cout << "Digite seu ano de nascimento: ";
    cin >> nascimento;

    cout << "Digite o ano atual: ";
    cin >> anoatual;

    int idade;
    idade = anoatual - nascimento;


    if (idade >= 18 ) {
        cout << "Em " << anoatual << ", você terá " << idade << " anos de idade e poderá tirar a habilitação! \n";
    }
    else {
        cout << "Em " << anoatual << ", você terá " << idade << " anos de idade e ainda não poderá tirar a habilitação! \n";
    }

    cin.ignore();// Limpa o buffer de entrada para que cin.get() funcione
    // Espera o usuário pressionar Enter antes de limpar a tela
std::cout << "\n--- Pressione ENTER para continuar e limpar a tela ---" << std::endl;
std::cin.get();

    
system("clear");// Comando para limpar a tela do terminal

    return 0;
}

//Crie um programa em C++ que solicite um número inteiro ao usuário e utilize o operador ternário para exibir se o número é par ou ímpar. 

#include <iostream>

using namespace std;

int main () {

    int numero;
    cout << "Digite um numero inteiro: ";
    cin >> numero;

    std::cout << std::string(75, '*') << std::endl;

    // Uso do operador ternário: Se a condição
    // for verdadeira? retorna o valor antes dos dois-pontos; senão, o valor depois.
    string mensagem = (numero % 2 == 0) ? "O número é PAR." : "O número é IMPAR."; 
    //o próprio operador ternário já contém uma criação de nova variável - mensagem
    cout << mensagem << endl;
    std::cout << std::string(75, '*') << std::endl;

        return 0;
}
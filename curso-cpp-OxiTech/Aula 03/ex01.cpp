// Faça um programa que leia o ano de nascimento do usuário e o ano atual, calcule a idade e informar:
// 1) Quantos anos terá no ano atual:
// 2) Se ele já pode tirar a habilitação(idade mínima: 18 anos)

# include <iostream>

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


    return 0;
}
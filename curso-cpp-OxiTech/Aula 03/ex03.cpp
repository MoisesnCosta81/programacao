/*
Ecreva um programa que leia o número de canal de televisão e escreva o nome da emissora correspondente.
Caso o usuário forneça um canal sem emissora exibir a mensagem "Canal inválido".
Considere as seguintes emissoras e seus respectivos canais:
* TV Ponta Verde: 5
* TV Gazeta: 7
* TV Pajuçara: 11
TV Farol:16
*/
#include <iostream>
using namespace std;

int main() {

int canal;
cout << "Digite um número de canal de TV: ";
cin >> canal;

if (canal == 5) {
    cout << "TV Ponta Verde \n";
}
else if (canal == 7) {
    cout << "TV Gazeta \n";
}
else if (canal == 11) {
    cout << "TV Pajuçara \n";
}
else if (canal == 16) {
    cout << "TV Farol \n";
}
else {
    cout << "Canal inválido \n";
}

    return 0;
}

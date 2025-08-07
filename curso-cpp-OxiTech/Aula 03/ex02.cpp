/*
Escrva um programa que, dada a idade de um nadador, classifique-o e um das seguintes categorias:
1) Infantil A: [5;7]
2) Infantil B: [8;10]
3) Juvenil A: [11;13]
4) Juvenil B: [14;17]
5) Adulto: [18;40]
6) Master: A partir de 41 e sem limite superior
Caso a idade informada esteja fora dos limites, emita uma mensagem de erro: "Idade inválida."
*/

#include <iostream>

using namespace std;

int main() {

int idade;

cout << "Idade do nadador: ";
cin >> idade;

if (idade >= 5 && idade <=7) {
    cout << "Infantil A \n";
}
else if (idade >=8 && idade <=10) {
    cout << "Infantil B \n";
}
else if (idade >= 11 && idade <=13) {
    cout << "Juvenil A \n";
}
else if (idade >=14 && idade <=17) {
    cout << "Juvenil B \n";
}
else if (idade >= 18 && idade <=40) {
    cout << "Adulto \n";
}
else if (idade >=41) {
    cout << "Master \n";
}
else {
    cout << "IDADE INVÁLIDA \n";
}

    return 0;
}
// Os blocos devem estar linkado ou haverá erro. o programa ignorará as condições.
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
        cout << "O número digitado (" << n << ")é maior que: " << n2 << ".\n";
    }
else if (n2 > n) {
        cout << "O número digitado (" << n2 << ") é maior que: " << n << ".\n";
    }
else {
        cout << "Os números são iguais:" << n << "=" << n2 << ".\n";
    }



return 0;
}

#include <iostream>
#include <string>
#include <iomanip> // biblioteca de manipulador para abaixo funcionar o << fixed << setprecision(2)
using namespace std;

int main() {

    string nome;
    //float nota1;
    //float nota2;
    //float nota3;
    float nota1, nota2, nota3, media;
    //media = (nota1 + nota2 + nota3) / 3; - pq dá erro se a linha ficar aqui?

    
    cout << "Nome: ";
    cin >> nome;
    cout <<"Nota 1: ";
    cin >> nota1;
    cout <<"Nota 2: ";
    cin >> nota2;
    cout << "Nota 3: ";
    cin >> nota3;

    media = (nota1 + nota2 + nota3) / 3;// a linha deve ficar aqui pois apenas nesta linha as variáveis estarão todas determinadas.

    cout << fixed << setprecision(2);// deixa só duas casas decimais
    cout << "A média final de " << nome << " é: " << media << endl;




    //cout <<"A memo da variável nome é: "<< sizeof(nome) << endl; mostra o uso de memoria

return 0;
}
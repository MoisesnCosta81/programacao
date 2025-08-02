#include <iostream>
using namespace std;
int main() {
    // devo indicar o ripo e o nome;
    // e atribuir um valor - tipo nome = valor;
    
    int vidas=5; // recebe numeros inteiros - 3, 10, 5
    char letra='m'; // recebe apenas 1 caracter - 'b'
    double decimal=5.2; // decimais 2.599999
    float decimal2=7.88; // menor precisão 2.6
    bool vivo=true; // true ou false / vdd ou falso 1 0
    string nome="moises"; // recebe textos"oi mundo!"

    cout << "Quantas vidas existem? ";
    cin >> vidas;
    cout << "Qual a letra? ";
    cin >> letra;
    cout << "Qual o decimal? ";
    cin >> decimal;
    cout << "Qual o decimal2? ";
    cin >> decimal2;
    cout <<"Qual o seu nome? ";
    cin >> nome;
    
    cout << vidas << "\n";
    cout << letra << "\n";
    cout << decimal << "\n";
    cout << decimal2 << "\n";
    cout << vivo << "\n";
    cout << nome << "\n";
    // cout << saida; imprime
    // cin >> entrada; input
    
    
    
    return 0;
}

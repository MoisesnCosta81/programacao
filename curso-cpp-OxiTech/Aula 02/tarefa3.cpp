#include <iostream>
#include <string>
#include <iomanip>// Necessário para std::fixed e std::setprecision

using namespace std;

int main() {
    string nome;
    float peso;
    float altura;

    cout << "Nome: ";
        cin >> nome;

    cout << "Peso: ";
        cin >> peso;

    cout << "Altura: ";
        cin >> altura;
        std::cout << std::string(75, '*') << std::endl;// para imprimir uma linha de asteriscos



    double imc = peso / (altura * altura);//double imc = peso * (altura) **2; não funcionou

        string resultado = (imc >= 18.5 && imc < 24.9) ? "Peso normal." : "Fora da faixa.";
        // Uso do operador ternário: Se a condição
        // for verdadeira? retorna o valor antes dos dois-pontos; senão, o valor depois.

        cout << fixed << setprecision(2);
        cout << nome <<", o seu IMC é: "<< imc << " - "<< resultado << endl;

        std::cout << std::string(75, '*') << std::endl;

    

return 0;
}

#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    char c;

    cout << "Por gentileza, digite uma letra entre A e G: ";
    cin >> c;

    switch(c) {
        case 'a':
        case 'A':
            cout << "Você digitou a letra 'A' ou 'a'." << endl;
            break;

        case 'b':
        case 'B':
            cout << "Você digitou a letra 'B' ou 'b'." << endl;
            break;

        case 'c':
        case 'C':
            cout << "Você digitou a letra 'C' ou 'c'." << endl;
            break;

        case 'd':
        case 'D':
            cout << "Você digitou a letra 'D' ou 'd'." << endl;
            break;

        case 'e':
        case 'E':
            cout << "Você digitou a letra 'E' ou 'e'." << endl;
            break;

        case 'f':
        case 'F':
            cout << "Você digitou a letra 'e' ou 'F'." << endl;
            break;

        case 'g':
        case 'G':
            cout << "Você digitou a letra 'G' ou 'g'." << endl;
            break;

        default:
            cout << "Letra inválida!\nPor gentileza, digitar uma letra dentro do intervalo solicitado.";

    }


std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux
return 0;
}

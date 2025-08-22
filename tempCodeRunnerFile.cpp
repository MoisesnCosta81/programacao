#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    cout << "Digite um número correspondente ao mês do ano: " << endl;
    int num = 0;
    cin >> num;

    switch (num) {
        case 1:
            cout << "Janeiro" << endl;
            break;
        case 2:
            cout << "Fevereiro" << endl;
            break;
        case 3:
            cout << "Março" << endl;
            break;
        case 4:
            cout << "Abril" << endl;
            break;
        case 5:
            cout << "Maio" << endl;
            break;
        case 6:
            cout << "Junho" << endl;
            break;
        case 7:
            cout << "Julho" << endl;
            break;
        case 8:
            cout << "Agosto" << endl;
            break;
        case 9:
            cout << "Setembro" << endl;
            break;
        case 10:
            cout << "Outubro" << endl;
            break;
        case 11:
            cout << "Novembro" << endl;
            break;
        case 12:
            cout << "Dezembro" << endl;
            break;
        default:
            cout << "Número inválido!\nPor gentileza inserir dentro do intervalo de 1 à 12." << endl;

    }







std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux
return 0;
}

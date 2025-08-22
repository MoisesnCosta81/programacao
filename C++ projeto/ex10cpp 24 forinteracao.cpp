//Aula 24 exxript
//Conectivos lógicos: &&, ||, ! -- e, ou, inverter valores !(x&&y)

#include <iostream>
#include <cstdlib>
using namespace std;

int main () {

    cout << "Digite um número entre 45 e 72: ";
    int i = 0;
    cin >> i;

    if(i == 45 || i == 72) {
        cout << "Eita, no limite do intervalo!!!\nQuase erra."; //"Obrigado por informar o número\ndentro do intervalo solicitado."
    }
        if(i >= 45 && i <= 72) {
            cout << "Obrigado por informar o número\ndentro do intervalo solicitado."; //"Eita, no limite do intervalo!!!/nQuase erra."
        }
    else
        cout << "O número digitado não está no intervalo solicitado;\nfavor digitar novamente conforme instruções." << endl;
       
    

    std::cout << "\nPressione Enter para limpar o terminal...\n";
    std::cin.ignore(); // Limpa o buffer de entrada
    std::cin.get();    // Espera o Enter

    system("clear"); // Limpa o terminal no Linux
return 0;
}

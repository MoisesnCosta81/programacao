/*
Nos parques de diversão, alguns brinquedos tem idade e altura para poderandar neles. O parque Ambrolândia  possui três brinquedos que possuem essa limitação:
* Barca Viking: 1,5m de altura e 12 anos.
* Elevador of Death: 1.4m de altura e 14 anos.
* Final Killer: 1.7m de altura ou 16 anos.
*/
#include <iostream>
using namespace std;

int main() {

float altura;
int idade;
int brinquedoslivres = 0;

cout << "Informe a sua altura: ";
cin >> altura;

cout << "Informe a sua idade: ";
cin >> idade;

cout << "\nVocê pode andar nos brinquedos:\n";

if (altura >= 1.5 && idade >=12) {
    cout << "- Barca Viking\n";
    brinquedoslivres++;
}
if (altura <= 1.4 && idade >= 14 ) {
    cout << "- Elevador of Death.\n";
    brinquedoslivres++;
}
else if (altura >= 1.7 || idade >= 16) { 
    cout << "- Final Killer.\n";
    brinquedoslivres++;
}

cout << "Um total de " << brinquedoslivres << " de 3 brinquedos.\n";





    return 0;
}
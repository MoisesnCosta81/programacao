 #include <iostream>
 #include <cstdlib>
 
 using namespace std;

 int main() {
    
    double n1, n2, n3, n4;
    cout << "Digite a primeira nota:  ";
    cin >> n1;
    cout << "Digite a segunda nota: ";
    cin >> n2;
    cout << "Digite a terceira nota: ";
    cin >> n3;
    cout << "Digite a quarta nota: ";
    cin >> n4;
cout << endl << endl;
    double soma = (n1 + n2 + n3 + n4) / 4;
    //double media = soma / 4;
    //cout << "A sua média é: " << media << endl;
    //soma = (soma/4);
    cout << "A sua media é: " << soma << endl << endl;

    if (soma
     >= 7) {
        cout << "Parabéns!!! Você está aprovado!" << endl;

    }else {
            cout << "Você foi reprovado!" << endl;
    }

std::cout << "\nPressione Enter para limpar o terminal...\n";
std::cin.ignore(); // Limpa o buffer de entrada
std::cin.get();    // Espera o Enter

system("clear"); // Limpa o terminal no Linux
    return 0;
}

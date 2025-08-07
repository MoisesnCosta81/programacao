// solicite o valor de um produto e calcule:
// * preço com 5% de desconto(pagamento à vista)
// * valor das 5 pascelas com 10% de desconto(parcamento parcelado)
// * comissão do vendedor para cada caso(6% sobre o valor da venda final)

#include <iostream>
#include <iomanip>
using namespace std;

int main() { // main é um ponto de entrada

    float preco;
     cout << "Digite o valor: R$";
        cin >> preco;
    


    float avista = preco - (preco * 0.05);
    //float parcelado = preco + (preco * 0.10);
    float dividido = (preco / 5) + ((preco * 0.10) / 5) ;

    float comissao1 = avista *(0.06);
    float comissao2 = preco * 0.06;
   

        cout << fixed << setprecision(2);
        cout << "À vista: R$ " << avista << endl;
        cout << fixed << setprecision(2);
        cout << "Parcelado (5x): R$ " << dividido << endl;
        cout << fixed << setprecision(2);
        cout << "Comissão à vista R$ " << comissao1 << endl;
        cout << fixed << setprecision(2);
        cout << "Comissão parcelado: R$ " << comissao2 << endl;



        return 0;
}
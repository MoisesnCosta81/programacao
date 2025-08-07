/*
José está prestes a  inaugurar seu supermercado. Ele acredita que o cidadão brasileiro é capaz de pagar suas compras sozinho sem precisar de um funcionário para conferir se o que ele está pagando corresponde aos produtos que ele está levando. Para isso ele vai precisar de um programa que irá ler o dia da semana(string), o preço do produto(float), a opção do produto(string: "prata" ou "ouro") e o nome(string).

* Se a compra estiver sendo realizada na segunda, terça ou quarta e a opção do produto for "ouro", o preço do produto ficará pela metade.
* Se a compra estiver sendo realizada na quinta ou sexta e o preço estiver entre R$ 10.00 e R$ 100.00, o preço será reduzido para um terço do valor original.
* Se a compra estiver sendo realizada no sábado e a opção for prata, o preço do produto será o triplo.
* Em qualquer outro caso, o preço será o dobro.

A saída  do programa deve ser uma frase no seguinte formato: "O reço do produto [nome do produto] no dia [dia da semana] é [preço do produto]"
*/

#include <iostream>
#include <cstdlib>// bilbioteca para limpar o terminal
using namespace std;

int main() {

string dia;
float preco;
string opcao;
string produto;

cout << "Informe o dia da semana: ";
    cin >> dia;

cout << "Informe o preço do produto: ";
    cin >> preco;

cout << "Informe a opção do produto(prata ou ouro): ";
    cin >> opcao;

cout << "Informe o nome do produto: ";
    cin >> produto;


if ((dia == "segunda" || dia == "terça" || dia == "quarta") && opcao == "ouro") {
    cout << "O preço do produto " << produto << " no dia " << dia << " é de R$" <<  preco / 2 << "\n";
}

else if ((dia == "quinta" || dia == "sexta") && preco >= 10.00 && preco <= 100.00) {
    cout << "O preço do produto " << produto << " no dia " << dia << " é de R$" <<  preco - (preco * 0.666) << "\n";
}

else if ((dia == "sábado") && opcao == "prata") {
    cout << "O preço do produto " << produto << " no dia " << dia << " é de R$" <<  preco * 3 << "\n";
}
else {
    cout << "O preço do produto " << produto << " no dia " << dia << " é de R$" <<  preco * 2 << "\n ";
}

std::cout << "\nPressione Enter para limpar o terminal...\n";
    std::cin.ignore(); // Limpa o buffer de entrada
    std::cin.get();    // Espera o Enter

    system("clear"); // Limpa o terminal no Linux

    // ... o código continua aqui
    return 0;
}
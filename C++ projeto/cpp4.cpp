#include <iostream>
using namespace std;

int n1, n2; // Declaração de variáveis - globais

int main() {

    // operadores matemáticos: +, -, /, *, % - mode dá o resto da divisão, ()
    int n3, n4; // Declaração de variáveis inteiras - locais do bloco

    int res, res1, res2;

    n1=11;
    n2=3;
    n3=5;
    n4=2;

    res=n1+n2+n3+n4;
    res=(n1+n2+n3+n4)-10;// o programa sempre considerará a linha mais atual
    res = n1 + n2 * n4;// a operação seguiirá a ordem de precedência, ou seja, primeiro multiplica e depois soma
    res = (n1 + n2) * n4; // se quiser mudar a ordem de precedência, use parênteses
    
    res1 = n1/n2;
    res2= n1%n2; // o operador % retorna o resto da divisão mod
    

    cout << "A soma das variáveis: " << res << "\n\n";
    cout << "Divisão: " << res1 << "\n";
    cout << "Resto: " << res2 << "\n\n";


    return 0;
}
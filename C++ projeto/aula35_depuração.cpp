
#include <iostream>
#include <cstdlib>

using namespace std;

int main() {

    cout << "Digite um número entre 1 e 3." << endl;
    int num = 0;
    cin >> num;

    if(num == 1) {
        for(int i = 0; i < 5; i++) {
            cout << "A variável da instrução FOR é: " << i << endl;
        }
    }else{
        if(num == 2) {
            int i2 = 0;
            while(i2 < 5) {
                i2++;
                cout << "O valor da variável WHILE é: " << i2 << endl;

            }
        }else{
            if(num == 3) {
                int i3 = 0;
                do{
                   i3++;
                   cout << "O valor da variável do DO-WHILE é: " << i3 << endl;
                }while(i3<5);
            }
        }
    }


return 0;
}

/*Fernanda tem um projeto de extensão e precisa selecionar alunos. Escreva um programa para que ela possa informar matrícula(int) e CRE(float) dos vários inscritos, e ver, ao final, a matrícula do aluno com menor CRE eo CRE médio de todos os candidatos.
*/

/*
Fernanda tem um projeto de extensão e precisa selecionar alunos. 
Escreva um programa para que ela possa informar matrícula(int) e CRE(float) dos vários inscritos, 
e ver, ao final, a matrícula do aluno com menor CRE e o CRE médio de todos os candidatos.
*/

#include <iostream>
#include <cstdlib>
#include <limits> // Para usar numeric_limits
#include <iomanip>

using namespace std;

int main() {
    int matricula, matriculaMenorCRE;
    float cre, menorCRE, somaCRE = 0.0, mediaCRE;
    int contadorAlunos = 0;
    char continuar = 'S'; // Inicia com 'S' para entrar no loop pela primeira vez

    // Inicializa o menor CRE com um valor muito alto
    menorCRE = numeric_limits<float>::max();

    cout << "--- Selecao de Alunos para o Projeto de Extensao ---\n\n";

    while (continuar == 'S' || continuar == 's') {
        cout << "Digite a matricula do aluno: ";
        cin >> matricula;
        cout << "Digite o CRE do aluno: ";
        cin >> cre;

        // Verifica se o CRE lido é o menor até agora
        if (cre < menorCRE) {
            menorCRE = cre;
            matriculaMenorCRE = matricula;
        }

        // Soma o CRE e conta o aluno
        somaCRE += cre;
        contadorAlunos++;

        // Pergunta se deseja continuar para a proxima iteracao do loop
        cout << "\nDeseja cadastrar outro aluno? (S/N): ";
        cin >> continuar;
        cout << "\n";
    }

    // --- Resultados ---
    if (contadorAlunos > 0) {
        mediaCRE = somaCRE / contadorAlunos;

        cout << "--- Resultados da Selecao ---\n";
        cout << "Matricula do aluno com o menor CRE: " << matriculaMenorCRE << endl;
        cout << fixed << setprecision(2);
        cout << "Menor CRE encontrado: " << menorCRE << endl;
        cout << "CRE médio de todos os candidatos: " << mediaCRE << endl;
    } else {
        cout << "Nenhum aluno foi cadastrado. O programa sera encerrado.\n";
    }

    return 0;
}

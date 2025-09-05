# A lista 'banco_de_dados' será o nosso armazenamento principal.
banco_de_dados = []


def cadastrar_funcionario():
    """Função para cadastrar um novo funcionário."""
    print("--- Cadastro de Novo Funcionário ---")
    funcionario = {}
    funcionario['nome'] = input("Nome completo: ")
    funcionario['data_nascimento'] = input("Data de nascimento (DD/MM/AAAA): ")
    funcionario['endereco'] = input("Endereço: ")
    funcionario['rg'] = input("RG: ")
    funcionario['cpf'] = input("CPF: ")
    funcionario['telefone'] = input("Telefone: ")
    funcionario['email'] = input("E-mail: ")
    funcionario['readaptado'] = input("Readaptado (s/n): ")
    funcionario['setor'] = input("Setor: ")
    funcionario['local_trabalho'] = input("Local de trabalho: ")
    funcionario['habilidades'] = input("Habilidades: ")
    banco_de_dados.append(funcionario)
    print("\n✅ Funcionário cadastrado com sucesso!")
    print("-" * 30)


def consultar_funcionario():
    """Função para consultar dados de um funcionário."""
    print("--- Consultar Funcionário ---")
    if not banco_de_dados:
        print("❌ Nenhum funcionário cadastrado.")
        print("-" * 30)
        return

    nome_busca = input("Digite o nome completo do funcionário para consulta: ").strip().lower()
    encontrado = False
    for funcionario in banco_de_dados:
        if funcionario['nome'].strip().lower() == nome_busca:
            print("\n✅ Funcionário encontrado!")
            for chave, valor in funcionario.items():
                print(f"🔹 {chave.replace('_', ' ').title()}: {valor}")
            encontrado = True
            break

    if not encontrado:
        print(f"❌ Funcionário '{nome_busca}' não encontrado.")

    print("-" * 30)


def apagar_funcionario():
    """Função para apagar um funcionário do cadastro."""
    print("--- Apagar Funcionário ---")
    if not banco_de_dados:
        print("❌ Nenhum funcionário cadastrado.")
        print("-" * 30)
        return

    nome_apagar = input("Digite o nome completo do funcionário que deseja apagar: ").strip().lower()
    encontrado = False
    for i, funcionario in enumerate(banco_de_dados):
        if funcionario['nome'].strip().lower() == nome_apagar:
            confirmacao = input(f"Tem certeza que deseja apagar {funcionario['nome']}? (s/n): ").strip().lower()
            if confirmacao == 's':
                del banco_de_dados[i]
                print(f"\n✅ Funcionário '{funcionario['nome']}' apagado com sucesso.")
            else:
                print(f"⛔ Operação cancelada.")
            encontrado = True
            break

    if not encontrado:
        print(f"❌ Funcionário '{nome_apagar}' não encontrado.")

    print("-" * 30)


# Loop principal do programa
while True:
    print("\n=== Menu Principal ===")
    print("1. Cadastrar novo funcionário")
    print("2. Consultar funcionário")
    print("3. Apagar funcionário")
    print("4. Sair")

    opcao = input("Escolha uma opção (1-4): ")

    if opcao == '1':
        cadastrar_funcionario()
    elif opcao == '2':
        consultar_funcionario()
    elif opcao == '3':
        apagar_funcionario()
    elif opcao == '4':
        print("\nPrograma finalizado. Até mais!")
        break
    else:
        print("\n⚠️ Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

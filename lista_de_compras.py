# =================================================================
# 1. Gerenciador de Lista de Compras
# Este programa permite adicionar, remover e visualizar itens de uma lista de compras.
# Ele usa um loop infinito (while True) para manter o menu ativo.
# =================================================================

def gerenciador_lista_compras():
    """Gerencia uma lista de compras."""
    lista_de_compras = []

    while True:
        print("\n--- Gerenciador de Lista de Compras ---")
        print("1. Adicionar item")
        print("2. Remover item")
        print("3. Visualizar lista")
        print("4. Sair")
        
        escolha = input("Digite sua escolha (1-4): ")

        if escolha == '1':
            item = input("Digite o item para adicionar: ")
            lista_de_compras.append(item)
            print(f"'{item}' foi adicionado à lista.")
        elif escolha == '2':
            item = input("Digite o item para remover: ")
            if item in lista_de_compras:
                lista_de_compras.remove(item)
                print(f"'{item}' foi removido da lista.")
            else:
                print(f"'{item}' não está na lista.")
        elif escolha == '3':
            print("\n--- Sua Lista de Compras ---")
            if not lista_de_compras:
                print("A lista está vazia.")
            else:
                for item in lista_de_compras:
                    print(f"- {item}")
        elif escolha == '4':
            print("Saindo do gerenciador de lista de compras.")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# =================================================================
# 2. Dicionário de Dados de Aluno
# Este programa demonstra como criar e acessar dados armazenados em um dicionário.
# =================================================================

def dados_aluno():
    """Cria e exibe dados de um aluno usando um dicionário."""
    print("\n--- Dados do Aluno ---")
    
    # Criação do dicionário com pares de chave-valor
    dados_aluno = {
        'nome': 'João',
        'idade': 20,
        'notas': [8.5, 9.0, 7.5]
    }

    # Acessando e exibindo os valores do dicionário
    print(f"Nome: {dados_aluno['nome']}")
    print(f"Idade: {dados_aluno['idade']}")
    print(f"Notas: {dados_aluno['notas']}")

# =================================================================
# 3. Separador de Números Pares e Ímpares
# Este programa usa um loop for e o operador módulo (%) para categorizar números.
# =================================================================

def separar_pares_impares():
    """Percorre uma lista de números e os separa em pares e ímpares."""
    print("\n--- Separador de Números Pares e Ímpares ---")

    numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    pares = []
    impares = []

    for num in numeros:
        # Se o resto da divisão por 2 for 0, o número é par
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)

    print(f"Números Pares: {pares}")
    print(f"Números Ímpares: {impares}")

# =================================================================
# 4. Desafio Extra: Sistema de Agenda de Contatos
# Um sistema completo para gerenciar contatos usando um dicionário.
# =================================================================

def agenda_contatos():
    """Gerencia uma agenda de contatos usando um dicionário."""
    contatos = {}

    while True:
        print("\n--- Agenda de Contatos ---")
        print("1. Adicionar contato")
        print("2. Remover contato")
        print("3. Buscar contato")
        print("4. Visualizar todos os contatos")
        print("5. Sair")

        escolha = input("Digite sua escolha (1-5): ")

        if escolha == '1':
            nome = input("Digite o nome do contato: ")
            telefone = input("Digite o número de telefone: ")
            contatos[nome] = telefone
            print(f"Contato '{nome}' adicionado/atualizado.")
        elif escolha == '2':
            nome = input("Digite o nome do contato para remover: ")
            if nome in contatos:
                # Usa a instrução 'del' para remover o item
                del contatos[nome]
                print(f"Contato '{nome}' removido.")
            else:
                print(f"Contato '{nome}' não encontrado.")
        elif escolha == '3':
            nome = input("Digite o nome do contato para buscar: ")
            if nome in contatos:
                print(f"Telefone de '{nome}': {contatos[nome]}")
            else:
                print(f"Contato '{nome}' não encontrado.")
        elif escolha == '4':
            print("\n--- Lista de Contatos ---")
            if not contatos:
                print("A agenda está vazia.")
            else:
                # Usa o método .items() para percorrer chaves e valores
                for nome_contato, telefone_contato in contatos.items():
                    print(f"- {nome_contato}: {telefone_contato}")
        elif escolha == '5':
            print("Saindo da agenda. Até mais!")
            break
        else:
            print("Escolha inválida. Por favor, tente novamente.")

# Execução de cada programa.
# Remova o '#' das linhas abaixo para executar cada função.

# gerenciador_lista_compras()
# dados_aluno()
# separar_pares_impares()
# agenda_contatos()


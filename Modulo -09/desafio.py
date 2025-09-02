def sistema_login():
    """Sistema de login com 3 tentativas."""
    credenciais = {"admin": "senha123", "usuario": "abc456"}
    tentativas = 3

    while tentativas > 0:
        print(f"\nVocê tem {tentativas} tentativa(s) restante(s).")
        usuario = input("Usuário: ")
        senha = input("Senha: ")

        try:
            if usuario in credenciais and credenciais[usuario] == senha:
                print("Login bem-sucedido!")
                return
            else:
                raise ValueError("Usuário ou senha inválidos.")
        except ValueError as e:
            print(f"Erro: {e}")
            tentativas -= 1
    
    print("\nNúmero de tentativas excedido. Tente novamente mais tarde.")

# Exemplo de uso:
sistema_login()
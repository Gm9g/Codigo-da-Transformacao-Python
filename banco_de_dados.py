def calculadora():
    """Realiza operações matemáticas com tratamento de erro de divisão por zero."""
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        operacao = input("Digite a operação (+, -, *, /): ")

        if operacao == '+':
            resultado = num1 + num2
        elif operacao == '-':
            resultado = num1 - num2
        elif operacao == '*':
            resultado = num1 * num2
        elif operacao == '/':
            resultado = num1 / num2
        else:
            print("Operação inválida.")
            return

        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Erro: Por favor, digite apenas números válidos.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

# Exemplo de uso
calculadora()

class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente em operações bancárias."""
    def __init__(self, saldo_atual, valor_saque):
        self.saldo_atual = saldo_atual
        self.valor_saque = valor_saque
        super().__init__(f"Saldo insuficiente. Saldo atual: R$ {saldo_atual:.2f}. Valor do saque: R$ {valor_saque:.2f}.")

class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
    
    def sacar(self, valor):
        if valor > self.saldo:
            raise SaldoInsuficienteError(self.saldo, valor)
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso. Saldo atual: R$ {self.saldo:.2f}")

# Simulação da conta
minha_conta = ContaBancaria("Gabriel", 500)

try:
    minha_conta.sacar(200)
    minha_conta.sacar(400) # Isso irá disparar a exceção
except SaldoInsuficienteError as e:
    print(f"Erro ao sacar: {e}") def pedir_idade():
    """Solicita e valida a idade do usuário, garantindo que seja um número positivo."""
    while True:
        try:
            idade_str = input("Por favor, digite sua idade: ")
            idade = int(idade_str)
            if idade <= 0:
                print("A idade deve ser um número positivo.")
            else:
                print(f"Sua idade é: {idade}")
                break  # Sai do loop se a idade for válida
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

# Exemplo de uso
pedir_idade()
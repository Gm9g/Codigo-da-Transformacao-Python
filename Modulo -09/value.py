class SaldoInsuficienteError(Exception):
    """Exceção para saldo insuficiente em operações bancárias."""
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
            # Lança a exceção personalizada
            raise SaldoInsuficienteError(self.saldo, valor)
        
        self.saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

# Simulação:
conta = ContaBancaria("Maria", 500)

try:
    conta.sacar(300)
    conta.sacar(300) # Isso vai gerar a exceção
except SaldoInsuficienteError as e:
    print(f"\nErro ao sacar: {e}")
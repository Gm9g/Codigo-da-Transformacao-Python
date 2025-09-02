# app.py
from faker import Faker
import random
from core import matematica

def mostrar_dados_falsos():
    """Gera e exibe dados falsos usando a biblioteca Faker."""
    fake = Faker('pt_BR')
    print("--- Dados Gerados ---")
    print(f"Nome: {fake.name()}")
    print(f"Endereço: {fake.address()}")
    print("-" * 30)

def jogar_adivinhacao():
    """Um jogo simples de adivinhação de números."""
    print("--- Jogo de Adivinhação ---")
    numero_secreto = random.randint(1, 20)
    tentativas = 0
    
    while True:
        try:
            palpite = int(input("Adivinhe o número (entre 1 e 20): "))
            tentativas += 1
            if palpite == numero_secreto:
                print(f"Parabéns! Você acertou em {tentativas} tentativas.")
                break
            elif palpite < numero_secreto:
                print("Tente um número maior.")
            else:
                print("Tente um número menor.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

def testar_matematica():
    """Testa as funções do módulo de matemática."""
    print("--- Testes Matemáticos ---")
    print(f"Soma de 5 e 3: {matematica.somar(5, 3)}")
    print(f"Divisão de 10 por 2: {matematica.dividir(10, 2)}")
    print(f"Divisão por zero: {matematica.dividir(10, 0)}")
    print("-" * 30)

# Início do programa
if __name__ == "__main__":
    testar_matematica()
    jogar_adivinhacao()
    mostrar_dados_falsos()

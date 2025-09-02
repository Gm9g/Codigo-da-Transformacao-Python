def calculadora():
    print("--- Calculadora Simples ---")
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
            print("Erro: Operação inválida.")
            return

        print(f"O resultado é: {resultado}")

    except ValueError:
        print("Erro: Entrada inválida. Por favor, digite apenas números.")
    except ZeroDivisionError:
        print("Erro: Não é possível dividir por zero.")

# Exemplo de uso:
calculadora() 
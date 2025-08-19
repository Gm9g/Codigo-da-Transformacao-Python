# 1. Função de Saudação Personalizada
def saudacao(nome):
  """
  Imprime uma saudação personalizada com o nome fornecido.
  """
  print(f"Olá, {nome}! Bem-vindo(a) à nossa plataforma.")
  print("-" * 30)

# 2. Função para Calcular Média e Aprovação
def calcular_media(nota1, nota2, nota3):
  """
  Calcula a média de três notas e informa se o aluno foi aprovado ou reprovado.
  """
  media = (nota1 + nota2 + nota3) / 3
  
  print(f"Sua média é {media:.2f}.")
  if media >= 7:
    print("Parabéns, você foi aprovado(a)!")
  else:
    print("Você foi reprovado(a).")
  print("-" * 30)

# 3. Função para Encontrar o Maior e o Menor Valor
def maior_menor(lista_numeros):
  """
  Retorna o maior e o menor número de uma lista.
  """
  if not lista_numeros:
    return None, None
  
  maior = max(lista_numeros)
  menor = min(lista_numeros)
  return maior, menor

# Desafio Extra: Sistema de Login Simples
def login_simples(usuario, senha):
  """
  Valida o usuário e a senha usando um dicionário de dados.
  """
  usuarios_db = {
      "joao123": "senha123",
      "ana_p": "4321senha",
      "pedro.s": "pedro@123"
  }

  if usuario in usuarios_db and usuarios_db[usuario] == senha:
    print("Login bem-sucedido!")
    return True
  else:
    print("Usuário ou senha inválidos. Tente novamente.")
    return False

# --- Exemplos de Uso das Funções ---

# Exemplo 1: Saudação
print("--- Teste da Função 'saudacao' ---")
saudacao("Carlos")

# Exemplo 2: Calcular Média
print("--- Teste da Função 'calcular_media' ---")
calcular_media(8.5, 7.0, 9.5)
calcular_media(5.0, 6.5, 4.0)

# Exemplo 3: Maior e Menor Valor
print("--- Teste da Função 'maior_menor' ---")
numeros = [12, 5, 23, 8, 19, 4]
maior, menor = maior_menor(numeros)
if maior is not None:
  print(f"A lista é: {numeros}")
  print(f"O maior número é: {maior}")
  print(f"O menor número é: {menor}")
else:
  print("A lista está vazia.")
print("-" * 30)

# Exemplo 4: Sistema de Login
print("--- Teste da Função 'login_simples' ---")
login_simples("joao123", "senha123")  # Login correto
login_simples("ana_p", "senha_errada")  # Login incorreto
print("-" * 30)
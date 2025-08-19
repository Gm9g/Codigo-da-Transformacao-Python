import os
import shutil
import json
import csv

# 1. Manipulação Básica de Arquivos .txt
def manipular_arquivo_txt():
    """Cria, escreve e lê de um arquivo .txt."""
    nome_arquivo = "meu_arquivo.txt"
    conteudo = "Olá, mundo!\nEste é um teste de gravação.\nEstamos aprendendo sobre arquivos em Python."
    
    # Gravando no arquivo
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        arquivo.write(conteudo)
    print(f"Informações gravadas com sucesso em '{nome_arquivo}'.")
    
    # Lendo o arquivo
    print("\n--- Conteúdo do arquivo ---")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo_lido = arquivo.read()
        print(conteudo_lido)
    print("-" * 30)

# 2. Salvando e Carregando Dados com JSON
def salvar_carregar_json():
    """Salva um dicionário em JSON e depois o carrega."""
    nome_arquivo = "clientes.json"
    clientes = {
        "101": {"nome": "Ana Silva", "email": "ana@email.com"},
        "102": {"nome": "Bruno Costa", "email": "bruno@email.com"},
        "103": {"nome": "Carla Dias", "email": "carla@email.com"}
    }
    
    # Salvando o dicionário em JSON
    with open(nome_arquivo, "w", encoding="utf-8") as arquivo:
        json.dump(clientes, arquivo, indent=4)
    print(f"Dicionário de clientes salvo em '{nome_arquivo}'.")
    
    # Carregando os dados de volta
    print("\n--- Dados carregados do arquivo JSON ---")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados_carregados = json.load(arquivo)
        print(dados_carregados)
    print("-" * 30)

# 3. Sistema de Notas com Arquivo CSV
def sistema_de_notas_csv():
    """Adiciona e exibe notas de alunos em um arquivo CSV."""
    nome_arquivo = "notas.csv"
    
    # Adicionando notas
    with open(nome_arquivo, "w", newline="", encoding="utf-8") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow(["Nome", "Materia", "Nota"]) # Cabeçalho
        writer.writerow(["João", "Matemática", 8.5])
        writer.writerow(["Maria", "Português", 9.0])
        writer.writerow(["Pedro", "Ciências", 7.8])
    print(f"Notas gravadas com sucesso em '{nome_arquivo}'.")

    # Exibindo as notas
    print("\n--- Notas dos alunos ---")
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        reader = csv.reader(arquivo)
        for linha in reader:
            print(linha)
    print("-" * 30)

# Desafio Extra: Sistema de Backup Automático com shutil
def sistema_backup():
    """Copia arquivos de uma pasta para outra, simulando um backup."""
    
    pasta_origem = "pasta_origem"
    pasta_destino = "pasta_destino_backup"
    
    # Cria as pastas se não existirem
    if not os.path.exists(pasta_origem):
        os.makedirs(pasta_origem)
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    # Cria arquivos fictícios na pasta de origem para o backup
    with open(os.path.join(pasta_origem, "documento.txt"), "w") as f:
        f.write("Este é o documento importante.")
    with open(os.path.join(pasta_origem, "foto.jpg"), "w") as f:
        f.write("Conteúdo da foto.")
        
    print(f"Arquivos criados em '{pasta_origem}' para o backup.")

    # Realiza o backup
    arquivos_para_backup = os.listdir(pasta_origem)
    
    print("\n--- Iniciando o backup ---")
    for arquivo in arquivos_para_backup:
        caminho_origem = os.path.join(pasta_origem, arquivo)
        caminho_destino = os.path.join(pasta_destino, arquivo)
        shutil.copy(caminho_origem, caminho_destino)
        print(f"Copiado: '{arquivo}' para '{pasta_destino}'")
    print("-" * 30)
    
# --- Execução de todas as funções ---
if __name__ == "__main__":
    print("Iniciando a execução das funções de manipulação de arquivos...")
    print("=" * 40)
    
    manipular_arquivo_txt()
    salvar_carregar_json()
    sistema_de_notas_csv()
    sistema_backup()
    
    print("=" * 40)
    print("Execução finalizada.").
print("minha Lista de Desejos para o Futuro\n")

NOME_ARQUIVO ="meus_desejos.txt"
desejos =[]

try: with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo: for linha in arquivo:
desejos.append(linha.strip())
print(f"Meus desejos foram carregados do arquivo '{NOME_ARQUIVO}'\n")
except FileNotFoundError:
print("parece que é sua primeira vez!Vamos criar sua lista de desejos.\n")
except Exception as e:
print (f"ocorreu um erro ao carregar os desejos: {e}")

    def salvar_desejos(Lista_de_Desejos):
try 
with open (NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:
    for desejo in (lista_de_desejos):
        arquivo.write(desejos + "\n")

        print ("\n Seus Desejos foram salvos com sucesso!")
except Exception as e:
print(f" Erro ao salvar os desejos:{e}")
while True:
    print("\n--- O que você quer fazer?---")
    print("1 - Adicionar um novo desejo")
    print("2 - ver meus desejos")
    print("3 - Sair")
    
    opcao= input("digite sua opção1,2 ou 3"): ")

if opcao== "1":
    novo_desejo= input("Qual é o seu novo desejo para o futuro?")
    if novo_desejo.strip()
    desejos.append(novo_desejo.strip())
    
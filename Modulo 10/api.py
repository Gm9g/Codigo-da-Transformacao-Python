import requests
import json

# Suas chaves de API
OPENWEATHER_API_KEY = "SUA_CHAVE_OPENWEATHER"
TMDB_API_KEY = "SUA_CHAVE_TMDB"

def obter_previsao_tempo(cidade):
    """
    Consome a API do OpenWeatherMap e exibe a previsão do tempo.
    """
    print(f"--- 1. Previsão do Tempo para {cidade} ---")
    url = f"http://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={OPENWEATHER_API_KEY}&units=metric&lang=pt_br"
    
    try:
        response = requests.get(url, timeout=10) # Timeout de 10 segundos para a requisição
        response.raise_for_status() # Lança um erro se a resposta HTTP for um erro
        
        dados = response.json()
        
        # 2. Exibindo informações específicas
        temperatura = dados['main']['temp']
        condicoes = dados['weather'][0]['description']
        umidade = dados['main']['humidity']
        
        print(f"Temperatura: {temperatura}°C")
        print(f"Condições: {condicoes.capitalize()}")
        print(f"Umidade: {umidade}%")
        
    except requests.exceptions.RequestException as e:
        # 3. Tratando erros de conexão
        print(f"Erro de conexão: {e}")
    except KeyError:
        print("Erro: A cidade não foi encontrada. Verifique o nome da cidade.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    print("-" * 40)

def buscar_filme(titulo_filme):
    """
    (Desafio Extra) Consome a API do TMDB e exibe informações sobre um filme.
    """
    print(f"--- Desafio Extra: Buscando informações sobre o filme '{titulo_filme}' ---")
    url_base = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": TMDB_API_KEY,
        "query": titulo_filme,
        "language": "pt-BR"
    }

    try:
        response = requests.get(url_base, params=params, timeout=10)
        response.raise_for_status()

        dados = response.json()
        
        if not dados['results']:
            print("Filme não encontrado.")
            return

        filme = dados['results'][0] # Pega o primeiro resultado

        # Exibindo informações relevantes
        titulo = filme['title']
        sinopse = filme['overview']
        data_lancamento = filme['release_date']
        
        print(f"Título: {titulo}")
        print(f"Lançamento: {data_lancamento}")
        print(f"Sinopse: {sinopse}")
        
    except requests.exceptions.RequestException as e:
        print(f"Erro de conexão: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
    
    print("-" * 40)

# --- Execução do Programa ---

if __name__ == "__main__":
    # Testando o consumo da API do OpenWeatherMap
    obter_previsao_tempo("São Paulo")
    
    # Testando um nome de cidade que não existe para ver o tratamento de erro
    obter_previsao_tempo("CidadeInexistente123")
    
    # Testando o consumo da API do TMDB (Desafio Extra)
    buscar_filme("Interestelar")
    
    # Testando um filme que não existe para ver o tratamento de erro
    buscar_filme("FilmeQualquerQueNaoExiste")

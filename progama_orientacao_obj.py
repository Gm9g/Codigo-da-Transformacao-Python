class Cachorro:
    def __init__(self, nome, raca, idade):
        self.nome = nome
        self.raca = raca
        self.idade = idade
        self.fome = 100

    def latir(self):
        print(f"{self.nome} da raça {self.raca} está latindo: Au Au!")
    
    def comer(self, quantidade_comida):
        self.fome -= quantidade_comida
        if self.fome < 0:
            self.fome = 0
        print(f"{self.nome} comeu. Nível de fome atual: {self.fome}")

cachorro1 = Cachorro("Guto", "Golden", 7)
cachorro2 = Cachorro("Luna", "Poodle", 2)

print(f"Informações do {cachorro1.nome}: Raça: {cachorro1.raca}, Idade: {cachorro1.idade} anos.")
cachorro1.latir()
cachorro1.comer(30)

print("\n")

print(f"Informações da {cachorro2.nome}: Raça: {cachorro2.raca}, Idade: {cachorro2.idade} anos.")
cachorro2.latir()
cachorro2.comer(50)


class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        """Inicializa um novo objeto Livro com título, autor e ano de publicação."""
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.disponivel = True  # Atributo para controlar a disponibilidade

    def __str__(self):
        """Retorna uma representação em string do objeto Livro."""
        status = "Disponível" if self.disponivel else "Emprestado"
        return f"'{self.titulo}' por {self.autor} ({self.ano_publicacao}) - Status: {status}"

# Criando um objeto da classe Livro
livro1 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954)
livro2 = Livro("1984", "George Orwell", 1949)

# Usando o método __str__ para imprimir os objetos
print(livro1)
print(livro2) 
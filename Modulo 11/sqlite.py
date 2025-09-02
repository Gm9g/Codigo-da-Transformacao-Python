import sqlite3

# --- Configuração do Banco de Dados ---

def criar_tabela_clientes():
    """Conecta ao banco e cria a tabela Clientes."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    # Cria a tabela Clientes com colunas id, nome e email
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    );
    """)
    
    conn.commit()
    conn.close()
    print("Tabela 'clientes' criada com sucesso.")

def criar_tabela_tarefas():
    """Cria a tabela Tarefas para o desafio extra."""
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        descricao TEXT NOT NULL,
        concluida INTEGER DEFAULT 0
    );
    """)
    
    conn.commit()
    conn.close()
    print("Tabela 'tarefas' criada com sucesso.")

# --- Operações CRUD para a tabela Clientes ---

def inserir_cliente(nome, email):
    """Insere um novo cliente na tabela."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    try:
        cursor.execute("INSERT INTO clientes (nome, email) VALUES (?, ?)", (nome, email))
        conn.commit()
        print(f"Cliente '{nome}' inserido com sucesso.")
    except sqlite3.IntegrityError:
        print(f"Erro: O email '{email}' já existe no banco de dados.")
    finally:
        conn.close()

def consultar_clientes():
    """Consulta e exibe todos os clientes."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    print("\n--- Clientes Cadastrados ---")
    cursor.execute("SELECT id, nome, email FROM clientes")
    clientes = cursor.fetchall()
    
    if not clientes:
        print("Nenhum cliente cadastrado.")
    else:
        for cliente in clientes:
            print(f"ID: {cliente[0]}, Nome: {cliente[1]}, Email: {cliente[2]}")
            
    conn.close()

def atualizar_cliente_email(id_cliente, novo_email):
    """Atualiza o email de um cliente existente."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    cursor.execute("UPDATE clientes SET email = ? WHERE id = ?", (novo_email, id_cliente))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Email do cliente com ID {id_cliente} atualizado para '{novo_email}'.")
    else:
        print(f"Erro: Cliente com ID {id_cliente} não encontrado.")
        
    conn.close()

def deletar_cliente(id_cliente):
    """Deleta um cliente pelo ID."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    cursor.execute("DELETE FROM clientes WHERE id = ?", (id_cliente,))
    conn.commit()
    
    if cursor.rowcount > 0:
        print(f"Cliente com ID {id_cliente} deletado com sucesso.")
    else:
        print(f"Erro: Cliente com ID {id_cliente} não encontrado.")
        
    conn.close()

# --- Consultas SQL Adicionais ---

def buscar_clientes_por_nome(nome_parcial):
    """Busca clientes cujo nome começa com uma determinada letra."""
    conn = sqlite3.connect('clientes.db')
    cursor = conn.cursor()
    
    print(f"\n--- Clientes com nome começando com '{nome_parcial}' ---")
    # A consulta usa o curinga % para encontrar nomes que começam com a string
    cursor.execute("SELECT nome, email FROM clientes WHERE nome LIKE ?", (nome_parcial + '%',))
    clientes = cursor.fetchall()
    
    if not clientes:
        print("Nenhum cliente encontrado.")
    else:
        for cliente in clientes:
            print(f"Nome: {cliente[0]}, Email: {cliente[1]}")
            
    conn.close()

# --- Desafio Extra: Gerenciador de Tarefas ---

def adicionar_tarefa(descricao):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    conn.commit()
    conn.close()
    print(f"Tarefa '{descricao}' adicionada.")

def listar_tarefas():
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, descricao, concluida FROM tarefas")
    tarefas = cursor.fetchall()
    conn.close()
    
    print("\n--- Lista de Tarefas ---")
    if not tarefas:
        print("Nenhuma tarefa pendente.")
        return
        
    for tarefa in tarefas:
        status = "Concluída" if tarefa[2] == 1 else "Pendente"
        print(f"ID: {tarefa[0]}, Descrição: {tarefa[1]}, Status: {status}")

def concluir_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Tarefa com ID {id_tarefa} concluída.")
    else:
        print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")

def excluir_tarefa(id_tarefa):
    conn = sqlite3.connect('tarefas.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tarefas WHERE id = ?", (id_tarefa,))
    conn.commit()
    conn.close()
    if cursor.rowcount > 0:
        print(f"Tarefa com ID {id_tarefa} excluída.")
    else:
        print(f"Erro: Tarefa com ID {id_tarefa} não encontrada.")

# --- Execução do Programa ---
if __name__ == "__main__":
    
    # Demonstração das atividades de clientes
    print("--- DEMONSTRAÇÃO DO SISTEMA DE CLIENTES ---")
    criar_tabela_clientes()
    
    inserir_cliente("Alice", "alice@email.com")
    inserir_cliente("Bruno", "bruno@email.com")
    inserir_cliente("Ana", "ana@email.com")
    inserir_cliente("Alice", "alice@email.com") # Tentativa de inserir email duplicado

    consultar_clientes()
    
    atualizar_cliente_email(2, "bruno_novo@email.com")
    
    deletar_cliente(1)
    
    consultar_clientes()
    
    buscar_clientes_por_nome("A")
    
    print("\n" + "="*50 + "\n")
    
    # Demonstração do desafio extra
    print("--- DEMONSTRAÇÃO DO GERENCIADOR DE TAREFAS ---")
    criar_tabela_tarefas()
    
    adicionar_tarefa("Estudar Python")
    adicionar_tarefa("Fazer exercícios")
    adicionar_tarefa("Planejar o projeto")
    
    listar_tarefas()
    
    concluir_tarefa(2)
    
    listar_tarefas()
    
    excluir_tarefa(1)
    
    listar_tarefas()
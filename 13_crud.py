import sqlite3

#conectar ao banco de dados (ou criar um novo, se não existir)
def conectar_banco() :
    conexao = sqlite3.connect('exemplo.db')
    return conexao

#criar a tabela
def criar_tabela() :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(

        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        idade INTEGER           
    )

    ''')
    conexao.commit()
    conexao.close()

#inserir usuário

def inserir_usuario(nome, idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(''' 
    INSERT INTO usuarios (nome, idade) VALUES (?, ?)
    ''', (nome, idade))
    conexao.commit()
    conexao.close()

#excluir dados

def excluir_usuario(id) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(''' 
    DELETE FROM usuarios WHERE id = ?
    ''', (id,))
    conexao.commit()
    conexao.close()

#atualizar usuario

def atualizar_usuario(id, novo_nome, nova_idade) :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(''' 
    UPDATE usuarios SET nome = ?, idade = ? WHERE id = ?
    ''', (novo_nome,nova_idade,id))

    conexao.commit()
    conexao.close()
    
# listar Usuários

def listar_usuarios() :
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    for usuario in usuarios :
        print (usuario)
    conexao.close()


#exemplo de uso das funções

criar_tabela()
inserir_usuario('Davi', 35)
inserir_usuario('João', 40)

print("Usuários cadastrados antes de atualizar:\n")
listar_usuarios()

atualizar_usuario(1, 'Davi', '50')
print("Usuários cadastrados após atualizar:\n")
listar_usuarios()

excluir_usuario(1)
print("Usuários cadastrados após excluir:\n")
listar_usuarios()

import sqlite3
import tkinter as tk #para interfaces gráficas
from tkinter import ttk #widget mais moderno do tkinter
from tkinter import messagebox #para  exibir alerta de erros

def conectar_banco():
    conexao = sqlite3.connect(r"C:\Users\davi.carneiro\Desktop\Python_EAD\lista_mercado.db")
    return conexao

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS itens (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        quantidade INTEGER,
        observacao TEXT
        )
        """
    )
    conexao.commit()
    conexao.close()

#==============================Funções Principais=============================

def adicionar_item():
    nome = entrada_nome.get().strip()
    quantidade = entrada_quantidade.get().strip()
    observacao = entrada_observacao.get().strip()

    #validacao simples
    if not nome:
        messagebox.showwarning("Atenção", "O campo de nome está vazio!")
        return
    if quantidade == "":
        quantidade = 1
    else:
        try:
            quantidade = int(quantidade)
        except ValueError:
            messagebox.showwarning("Atenção", "Digite um número válido na quantiidade!")
            return
        
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO itens (nome, quantidade, observacao) VALUES (?, ?, ?)",
                   (nome, quantidade, observacao))
    conexao.commit()
    conexao.close()

    #limpa o campo após salvar no banco de dados
    entrada_nome.delete(0, tk.END)
    entrada_quantidade.delete(0, tk.END)
    entrada_observacao.delete(0, tk.END)

    #atualiza a lista exibida na tela
    carregar_itens()

def carregar_itens():
    #limpar a tabela (TreeView) antes de recarregar
    for item in tabela_itens.get_children():
        tabela_itens.delete(item)
    #buscar todos os registros do banco
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, nome, quantidade, observacao FROM itens")
    registros = cursor.fetchall()
    conexao.close()
    #insere cada registro na tabela da interface gráfica (TreeView)
    for linha in registros:
        tabela_itens.insert("", tk.END, values=linha)

def excluir_item_selecionado():
    #pega o item selecionado na tabela
    item_selecionado = tabela_itens.selection()
    if not item_selecionado:
        messagebox.showinfo('Info', 'Selecione um item para excluir!')
        return
    
    #pega os valores da linha
    valores = tabela_itens.item(item_selecionado, "values")
    item_id = valores[0]

    #confirma se vai excluir
    confirmar = messagebox.askyesno("Confirmar", "Tem certeza de que deseja excluir este item?")
    if not confirmar:
        return

    #exclui do banco
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("DELETE FROM itens WHERE id = ?", (item_id,))
    conexao.commit()
    conexao.close()

    #atualiza a tabela
    carregar_itens()

def limpar_busca():
    entrada_busca.delete(0, tk.END)
    carregar_itens()

def buscar_itens():
    termo = entrada_busca.get().strip()
    
    #limpar a tabela antes de mostrar o resultado da busca

    for item in tabela_itens.get_children():
        tabela_itens.delete(item)
    
    conexao = conectar_banco()
    cursor = conexao.cursor()

    if termo == "":
        #não digitou nada, mostra tudo novamente
        cursor.execute("SELECT id, nome, quantidade, observacao FROM itens")
    else:
        #buscar item cujo nome contenha o termo digitado
        cursor.execute("SELECT id, nome, quantidade, observacao FROM itens WHERE nome LIKE ?", (f"%{termo}%",))

    registros = cursor.fetchall()
    conexao.close()

    #preenche a tabela com o resultado da busca

    for linha in registros:
        tabela_itens.insert("", tk.END, values=linha)

#=============================Interface Gráfica===============================

criar_tabela() #Garante que a tabela sempre vai existir antes de abrir a interface gráfica

janela = tk.Tk()

janela.title('Lista de Compras - Hemobrás')
janela.geometry('700x400')

#Frame para o formulário de cadastro

frame_formulario = tk.Frame(janela)
frame_formulario.pack(pady=10)

#Rótulos e campos de entrada

tk.Label(frame_formulario, text="Nome do Item: ").grid(row=0, column=0, sticky='w')
entrada_nome = tk.Entry(frame_formulario, width=30)
entrada_nome.grid(row=0, column=1, sticky='w', padx=5)

tk.Label(frame_formulario, text="Quantidade: ").grid(row=1, column=0, sticky='w')
entrada_quantidade = tk.Entry(frame_formulario, width=10)
entrada_quantidade.grid(row=1, column=1, sticky='w', padx=5)

tk.Label(frame_formulario, text="Observação: ").grid(row=2, column=0, sticky='w')
entrada_observacao = tk.Entry(frame_formulario, width=50)
entrada_observacao.grid(row=2, column=1, sticky='w', padx=5, pady=5)

botao_adicionar = tk.Button(
    frame_formulario,
    text="Adicionar Item",
    command=adicionar_item
)
botao_adicionar.grid(row=3, column=0, columnspan=2, pady=5)

#Área de busca
frame_busca = tk.Frame(janela)
frame_busca.pack(pady=5)
tk.Label(frame_busca, text='Buscar item: ').grid(row=0, column=0, padx=5)
entrada_busca = tk.Entry(frame_busca, width=30)
entrada_busca.grid(row=0, column=1, padx=5)

botao_buscar = tk.Button(
    frame_busca,
    text='Buscar',
    command=buscar_itens
)
botao_buscar.grid(row=0, column=2, padx=5)
botao_limpar = tk.Button(
    frame_busca,
    text="Limpar Busca",
    command=limpar_busca
)
botao_limpar.grid(row=0, column=4, padx=5)

#construindo a tabela (TreeView) de exibição dos itens da interface gráfica

colunas = ("id", "nome", "quantidade", "observacao")
tabela_itens = ttk.Treeview(janela, columns=colunas, show='headings')
tabela_itens.heading('id', text='ID')
tabela_itens.heading('nome', text='Nome')
tabela_itens.heading('quantidade', text='Quantidade')
tabela_itens.heading('observacao', text='Observação')

tabela_itens.column('id', width=40)
tabela_itens.column('nome', width=200)
tabela_itens.column('quantidade', width=90)
tabela_itens.column('observacao', width=250)

tabela_itens.pack(fill='both', expand=True, padx=10, pady=10)

#botões de ações abaixo da tabela

frame_botoes = tk.Frame(janela)
frame_botoes.pack(pady=5)

botao_recarregar = tk.Button(
    frame_botoes,
    text = "Recarregar Itens",
    command=carregar_itens
)

botao_recarregar.grid(row=0,column=0,padx=5)

botao_excluir = tk.Button(
    frame_botoes,
    text="Excluir selecionado",
    command=excluir_item_selecionado
)

botao_excluir.grid(row=0, column=1, padx=5)

carregar_itens()

#inicia o loop da interface gráfica
janela.mainloop()
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Exemplo de DataFrame com títulos de livros
data = {
    'nome_livro': ['Harry Potter', 'O Senhor dos Anéis', 'Dom Casmurro', '1984', 'A Revolução dos Bichos'],
}
biblioteca = pd.DataFrame(data)

# Função para filtrar os itens da lista suspensa
def filtrar_lista(event):
    filtro = entry_pesquisa.get().lower()  # Obtém o texto digitado em minúsculas
    opcoes_filtradas = [livro for livro in biblioteca['nome_livro'] if filtro in livro.lower()]
    
    # Atualiza as opções da combobox
    combo_nome['values'] = opcoes_filtradas
    if opcoes_filtradas:
        combo_nome.current(0)  # Seleciona o primeiro item da lista filtrada
    else:
        combo_nome.set('')  # Limpa a combobox se não houver correspondências

# Função para mostrar a seleção feita
def mostrar_selecao():
    selecionado = combo_nome.get()
    label_resultado.config(text=f"Você selecionou: {selecionado}")

# Criação da janela principal
root = tk.Tk()
root.title("Seleção de Livros")

# Campo de entrada para pesquisa
tk.Label(root, text="Pesquisar livro:").grid(row=0, column=0, padx=10, pady=10)
entry_pesquisa = tk.Entry(root)
entry_pesquisa.grid(row=0, column=1, padx=10, pady=10)

# Combobox para a lista suspensa
tk.Label(root, text="Selecione um livro:").grid(row=1, column=0, padx=10, pady=10)
combo_nome = ttk.Combobox(root, values=biblioteca['nome_livro'].tolist())
combo_nome.grid(row=1, column=1, padx=10, pady=10)

# Bind do evento de digitação (para atualizar a lista conforme o usuário digita)
entry_pesquisa.bind('<KeyRelease>', filtrar_lista)

# Botão para confirmar a seleção
btn_selecionar = tk.Button(root, text="Mostrar Seleção", command=mostrar_selecao)
btn_selecionar.grid(row=2, columnspan=2, pady=10)

# Label para mostrar o resultado
label_resultado = tk.Label(root, text="")
label_resultado.grid(row=3, columnspan=2, pady=10)

# Inicia a aplicação
root.mainloop()

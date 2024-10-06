#Importando Bibliotecas:

import pandas as pd
from datetime import datetime, timedelta
import tkinter as tk
from tkinter import ttk
pd.set_option('display.max_columns', None)

#lendo o banco de dados:
biblioteca = pd.read_excel(r"C:\Users\julio\Documents\Pasta GIT\Poo Estudos\biblioteca.xlsx")
clientes = pd.read_excel(r'C:\Users\julio\Documents\Pasta GIT\Poo Estudos\Clientes_cadastrados.xlsx')


#Funções para atualizar o locador:

def atualizar_usuario(nome_do_livro, locador):
    print(f"Atualizando locador para o livro: {nome_do_livro}")
    biblioteca['Nome do livro'] = biblioteca['Nome do livro'].str.strip().str.lower()
    nome_do_livro = nome_do_livro.strip().lower()
    biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'locador'] = locador


def atualizar_cpf(nome_do_livro, cpf):
    biblioteca['Nome do livro'] = biblioteca['Nome do livro'].str.strip().str.lower()
    nome_do_livro = nome_do_livro.strip().lower()
    biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'CPF'] = cpf


def atualizar_data_retirada(nome_do_livro, data_locada):
    biblioteca['Nome do livro'] = biblioteca['Nome do livro'].str.strip().str.lower()
    nome_do_livro = nome_do_livro.strip().lower()
    biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'data da locação'] = data_locada
    data_locada = datetime.strptime(data_locada,'%d/%m/%Y')
    data_devolver = data_locada + timedelta(days=5)
    data_devolver = data_devolver.strftime('%d/%m/%Y')
    biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Previsão de devolutiva'] = data_devolver


def Multa(nome_do_livro,devolveu):
    devolveu= datetime.strptime(devolveu,'%d/%m/%Y')
    biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Data devolvida'] = devolveu
            
    previsto= biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Previsão de devolutiva'].values 
    previsto =previsto[0]
    previsto = datetime.strptime(previsto,'%d/%m/%Y') 
    
    if previsto< devolveu:
        biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Multa'] = "SIM"
        dif = (devolveu - previsto).days
        biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Valor'] = dif * 5.00
        
    else:
        biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Multa'] = "NÂO"
        biblioteca.loc[biblioteca['Nome do livro'] == nome_do_livro, 'Valor'] = 0

## Cadastrando Clientes:

def Salva_Cadastro():
    clientes.to_excel(r'C:\Users\julio\Documents\Pasta GIT\Poo Estudos\Clientes_cadastrados.xlsx', index=False)

class cadastro:
    def __init__(self,nome,cpf,nascimento,telefone,endereco,bairro,cidade,cep,obs):
        self.nome=nome
        self.cpf=cpf
        self.nascimento=nascimento
        self.telefone=telefone
        self.Endereco= endereco 
        self.Bairro=bairro
        self.Cidade=cidade
        self.cep=cep
        self.obs=obs
        
    def linha_vazia(self,coluna):
        return clientes[clientes[coluna].isna()].index[0]
            
                
    def CPF_cadastro(self):
        if self.cpf not in clientes['CPF'].values: 
            clientes.at[self.linha_vazia('CPF'), 'CPF'] = self.cpf 
            return True
        else:
            return  False
        
    def cadastrar_atributo(self):
        if self.CPF_cadastro(): 
            clientes.at[self.linha_vazia('Nome'), 'Nome'] = self.nome
            clientes.at[self.linha_vazia('Data de nascimento'), 'Data de nascimento'] = self.nascimento
            clientes.at[self.linha_vazia('Telefone'), 'Telefone'] = self.telefone
            clientes.at[self.linha_vazia('Endereço'), 'Endereço'] = self.Endereco
            clientes.at[self.linha_vazia('Bairro'), 'Bairro'] = self.Bairro
            clientes.at[self.linha_vazia('Cidade'), 'Cidade'] = self.Cidade
            clientes.at[self.linha_vazia('CEP'), 'CEP'] = self.cep
            clientes.at[self.linha_vazia('Observações'), 'Observações'] = self.obs
        else:
            return "CPF já cadastrado"
        
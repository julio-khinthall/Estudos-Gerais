from tkinter import *
from tkinter import ttk
import sqlite3
import os

root=Tk()


class funcs():
    
    def Limpar_tela(self):
        self.codigo_entry.delete(0,END)
        self.telefone_entry.delete(0,END)
        self.nome_entry.delete(0,END)
        self.Cidade_entry.delete(0,END)
   
    def conecta_bd(self):
        caminho_bd = os.path.join(os.path.dirname(__file__), 'Base_de_Clientes')
        self.conn = sqlite3.connect(caminho_bd)
        self.cursor=self.conn.cursor(); print("Conectando ao banco de dados")
        
    def desconecta_bd(self):
         self.conn.close()         
         
    def montaTabela(self):
        self.conecta_bd()
        ##Criando Tabela##
        self.cursor.execute("""
                CREATE TABLE IF NOT EXISTS clientes(
                    cod INTEGER PRIMARY KEY,
                    Nome_cliente CHAR(40) NOT NULL,
                    telefone INTEGER (20),
                    cidade CHAR (40)
                );                
                """)
        self.conn.commit();print("Banco Criado")
        self.desconecta_bd();print("Desconectando ao banco de dados")
    
    def variaveis(self):
        self.conecta_bd() 
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.Cidade_entry.get()
   
    def add_cliente(self):
        self.variaveis()        
        self.cursor.execute("""
            INSERT INTO clientes(Nome_cliente, telefone, cidade)
            VALUES(?, ?, ?)
        """, (self.nome, self.telefone, self.cidade))
        
        self.conn.commit() 
        self.desconecta_bd() 
        self.select_lista()
        self.Limpar_tela()  
        
    def select_lista(self):
        self.lista.delete(*self.lista.get_children())
        self.conecta_bd()
        lista = self.cursor.execute("""
            SELECT cod, Nome_cliente, telefone, cidade 
            FROM clientes 
            ORDER BY cod ASC;
        """)
        for i in lista:
            self.lista.insert("", END, values=i)
                
        self.desconecta_bd()
   
    def Clique_duplo(self,event):
        self.Limpar_tela()
        self.lista.selection()
        
        for n in self.lista.selection():
            col1,col2,col3,col4=self.lista.item(n,'values')
            self.codigo_entry.insert(END,col1)
            self.nome_entry.insert(END,col2)
            self.telefone_entry.insert(END,col3)
            self.Cidade_entry.insert(END,col4)
   
    def Deleta_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute("""
                            DELETE FROM clientes WHERE cod= ?                                              
                            """,(self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.Limpar_tela()
        self.select_lista()
        
    def altera_cliente(self):
        self.variaveis()
        self.conecta_bd()
        self.cursor.execute(""" 
                            UPDATE clientes SET Nome_cliente=?, telefone=?, cidade=?
                            WHERE cod=?
                            """,(self.nome,self.telefone,self.cidade,self.codigo))
        self.conn.commit()
        self.desconecta_bd()
        self.select_lista()
        self.Limpar_tela()

    def busca_cliente(self):
        self.conecta_bd()
        self.lista.delete(*self.lista.get_children()) 
        self.nome_entry.insert(END,'%')
        nome=self.nome_entry.get()
        self.cursor.execute("""
                            SELECT cod, nome_cliente, telefone, cidade
                            FROM clientes
                            WHERE nome_cliente LIKE '%s'
                            ORDER BY nome_cliente ASC
                            """ % nome)
        buscanome=self.cursor.fetchall()
        for i in buscanome:
            self.lista.insert("",END,values=i)
        self.Limpar_tela()
        self.desconecta_bd()
        
class Cadastros(funcs):
    
    def __init__(self):
        self.root=root
        self.tela()
        self.subtelas()
        self.montaTabela()
        self.Descrição_Texto()
        self.Caixa_texto()
        self.botoes()
        self.Lista()
        self.select_lista()
        self.Menus()
        root.mainloop()           
        
    def tela(self):
        self.root.title("Cadastros")
        self.root.configure(background="#000000") #deixei a cor preta pq eu gosto ;)
        self.root.geometry("800x500")
        self.root.resizable(True,True)
        self.root.maxsize(width=1020,height=800)
        self.root.minsize(width=800, height=500)    
             
    def subtelas(self):
        self.subtela_1= Frame(self.root,bd = 4,bg ="#dfe3ee",highlightbackground="#759fe6",highlightthickness=2)
        self.subtela_1.place(relx=0.02,rely=0.02,relwidth=0.96,relheight=0.46)
        
        self.subtela_2= Frame(self.root,bd = 4,bg ="#dfe3ee",highlightbackground="#759fe6",highlightthickness=2)
        self.subtela_2.place(relx=0.02,rely=0.5,relwidth=0.96,relheight=0.46)
                 
    def botoes(self):
        self.bt_Limpar= Button(self.subtela_1,text="limpar",command=self.Limpar_tela)
        self.bt_Limpar.place(relx=0.15,rely=0.1,relheight=0.1,relwidth=0.15)
        
        self.bt_buscar= Button(self.subtela_1,text="Buscar",command=self.busca_cliente)
        self.bt_buscar.place(relx=0.30,rely=0.1,relheight=0.1,relwidth=0.15)
        
        self.bt_Novo= Button(self.subtela_1,text="Novo",command=self.add_cliente)
        self.bt_Novo.place(relx=0.55,rely=0.1,relheight=0.1,relwidth=0.15)
        
        self.bt_Alterar= Button(self.subtela_1,text="Alterar",command=self.altera_cliente)
        self.bt_Alterar.place(relx=0.70,rely=0.1,relheight=0.1,relwidth=0.15)        
        
        self.bt_Apagar= Button(self.subtela_1,text="Apagar",command = self.Deleta_cliente)
        self.bt_Apagar.place(relx=0.85,rely=0.1,relheight=0.1,relwidth=0.15)
                  
    def Descrição_Texto(self):
        self.lb_codigo= Label(self.subtela_1,text="Código",bg ="#dfe3ee")
        self.lb_codigo.place(relx=0.005,rely=0.01,relheight=0.1,relwidth=0.13)
        
        self.lb_codigo= Label(self.subtela_1,text="Nome",bg ="#dfe3ee")
        self.lb_codigo.place(relx=0.005,rely=0.4,relheight=0.1,relwidth=0.13)
        
        self.lb_codigo= Label(self.subtela_1,text="Telefone",bg ="#dfe3ee")
        self.lb_codigo.place(relx=0.005,rely=0.7,relheight=0.1,relwidth=0.13)       
        
        self.lb_codigo= Label(self.subtela_1,text="Cidade",bg ="#dfe3ee")
        self.lb_codigo.place(relx=0.5,rely=0.7,relheight=0.1,relwidth=0.13)        
                   
    def Caixa_texto(self):
        self.codigo_entry= Entry(self.subtela_1,)
        self.codigo_entry.place(relx=0.005,rely=0.1,relheight=0.1,relwidth=0.13)
        
        self.nome_entry= Entry(self.subtela_1,)
        self.nome_entry.place(relx=0.005,rely=0.5,relheight=0.1,relwidth=0.5)
        
        self.telefone_entry= Entry(self.subtela_1,)
        self.telefone_entry.place(relx=0.005,rely=0.8,relheight=0.1,relwidth=0.4)
             
        self.Cidade_entry= Entry(self.subtela_1,)
        self.Cidade_entry.place(relx=0.5,rely=0.8,relheight=0.1,relwidth=0.4)
                     
    def Lista(self):
        self.lista=ttk.Treeview(self.subtela_2,height=7,columns=("col 1","col 2","col 3","col 4"))
        
        self.lista.heading("#0",text="")
        self.lista.column("#0",width=1)
        
        self.lista.heading("#1",text="Codigo")
        self.lista.column("#1",width=50)
        
        self.lista.heading("#2",text="Nome")
        self.lista.column("#2",width=200)
        
        self.lista.heading("#3",text="Telefone")
        self.lista.column("#3",width=125)
        
        self.lista.heading("#4",text="Cidade")
        self.lista.column("#4",width=125)
               
        self.lista.place(relx=0.01,rely=0.01,relwidth=0.97,relheight=0.98)
        
        self.scroollista=Scrollbar(self.subtela_2,orient="vertical")
        self.scroollista.configure(command=self.scroollista.set)
        self.scroollista.place(relx=0.98,rely=0.01,relwidth=0.02,relheight=0.97)
    
        self.lista.bind("<Double-1>",self.Clique_duplo)
        
    def Menus(self):
        barra_menu=Menu(self.root)
        self.root.config(menu=barra_menu)  
        
        filemenu=Menu(barra_menu)
        filemenu2=Menu(barra_menu)
        filemenu3=Menu(barra_menu)
        def Quit():
            self.root.destroy()
        
        barra_menu.add_cascade(label="Opções",menu=filemenu)
        filemenu.add_command(label="Teste",command=Quit) 
        filemenu.add_command(label="Sair",command=Quit)
        
        barra_menu.add_cascade(label="Sobre",menu=filemenu2)
        filemenu2.add_command(label="Limpa Cliente",command=self.Limpar_tela)
        
        barra_menu.add_cascade(label="Outras Opções",menu=filemenu3)
        filemenu3.add_command(label="Em Desenvolvimento",command=self.Limpar_tela)
        
          
Cadastros()
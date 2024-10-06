#definindo Funções:



def incluir(lista, valor):
    lista.append(valor)

def excluir(lista,indice):
    if indice<len(lista):
        lista.pop(indice)
    else:
        print("Opção invalida. Tente novamente: ")

def ver(lista):
    if len(lista)>0:
        print(f"A sua lista tem os seguintes valores: {lista}." )
    else:
        print("lista vazia")
        
def organizar(lista,item1,item2):
    if len(lista)<=0:
        print("Lista Vazia, Tente novamente: ")
    elif item1<len(lista) and item2<len(lista) :
        lista[item1],lista[item2]=lista[item2],lista[item1]
    else:
        print("opção Invalida,tente novamente: ")

# Criando a lista de estudo:

lista1=[]

# Aplicando a estrutura de repetição com o as opções em IFs
while True:
    print("")
    print("")
    opcao= input("Digite a opcao que deseja: \n 1- Incluir item a lista; \n 2- Excluir item da lista; \n 3- Organizar Lista; \n 4-Ver Lista;\n 5-Sair;\n \nDigite o numero da opcao: " ).strip()
    if opcao.isdigit():
        opcao = int(opcao)
        if opcao not in [1,2,3,4,5]:
            print("Por favor selecione uma das opções acima: ")
            
        else:         
            if opcao == 1:
                
                item=str(input("Qual item você deseja incluir? ").strip())
                incluir(lista1,item)
                print(f"O item '{item}' foi incluido :)")
                
                
            elif opcao==2:
                if len(lista1)==0:
                    print("Lista Vazia")
                else:   
                    exclui = (input(f"Qual item você deseja retirar? dos {len(lista1)} itens da lista ").strip())-1
                    if exclui.isdigit():
                        exclui = int(exclui)
                        if opcao >len(lista1):
                            print("Por favor selecione uma das opções acima: ")
                        else:    
                            excluir(lista1,exclui)
                        
            elif opcao==3:
                
                if len(lista1)<=0:
                    print("lista Vazia")
                else:    
                    posicao1 = int(input("Qual item você deseja trocar a posição?"))-1
                    posicao2 = int(input(f"Em que posição você deseja colocar o item da posição {posicao1+1} ?").strip())-1
                    organizar(lista1,posicao1,posicao2)
                
                                
            elif opcao==4: 
                ver(lista1)
                
                
            elif opcao==5:
                print("Encerrando....")
                break
            
            
            else:
                print("Digite uma opção válida")
    
    else:
        print("Digite uma opção válida") 
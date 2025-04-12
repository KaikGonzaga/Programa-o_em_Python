## ***ATIVIDADE 1***
# 1 - Faça um programa, utilizando while, que mostre na tela os números de 0 a 1000.
Num = 0 

while Num <=100:
    print(Num)
    Num += 1 # Essa linha fica somando 1 a variavel 

## ***ATIVIDADE 1***
# 2 -  Faça um sistema, utilizando while e listas, que permita o usuário escrever o nome de 10 pessoas e os mostre na tela.

Nomes = [] 
QTDE_Nomes = 0

while QTDE_Nomes <10:
    Nome = input ("Digite o nome" + str(QTDE_Nomes + 1) + ": ")
    Nomes.append(Nome)
    QTDE_Nomes += 1

    print("\n Nomes digitados: ")
    for Nome in Nomes:
        print(Nome)
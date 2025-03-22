print ("Atividade 1")
print ("Boas-vindas!!")

print ("\nAtividade 2")
NUM1 = bool (1)
print ("NUM1",type(NUM1))

print ("\nAtividade 3")
NUM2 = 25.00
NUM3 = 10.00
print ("Resultado da multiplicação:", NUM2 * NUM3)

print ("\nAtividade 4")
print ("Resultado da divisão:", NUM2 / NUM3)

print ("\nAtividade 5")
print ("Resultado da subtração:", NUM2 - NUM3)

print ("\nAtividade 6")
div_int = int (NUM2/NUM3)
print ("Resultado da divisão inteira:", div_int)

print ("\nAtividade 7")
NUM4 = 13.00
NUM5 = 9.50
print ("Resultado da multiplicação de 4 números decimais:", NUM2 * NUM3 * NUM4 *NUM5)

print ("\nAtividade 8")
NUM6 = 8
print ("Dobro da Variavel: ", NUM6*2)

print ("\nAtividade 10")
print("Bem vindo!\n Preecha os dados abaixo para realizar o cadastro:")

print ("\n Dados pessoais:")
FIST_NAME = str (input("Digite seu primeiro nome:"))
SECOND_NAME = str (input("Digite seu sobrenome:"))
AGE = int (input("Digite sua idade:"))
EMAIL = str (input("Digite seu E-mail:"))

print ("\n Endereço:")
STATE = str (input("UF:"))
CITY = str (input("Cidade:"))
ADDRESS = str (input("Rua:"))
NUMBER = int (input("Numero:"))
print ("\nConfirme os Dados:","\nNome Completo: ",FIST_NAME, SECOND_NAME,"\nIdade atual:", AGE,"\nEmail para contato:",EMAIL,"\nEndereço:",CITY,STATE,"- Rua:",ADDRESS,"- Nº",NUMBER)

CONFIRM = str (input("\nOs dados estão corretos? (Sim ou Não)"))
if CONFIRM == 'Sim': print ("\nCadastro Finalizado!")
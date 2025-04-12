print('Desafio 2: Condicionais', "\n\nSistema de Reservas de Hotel:")
print("\n\nBem-vindo ao Hotel Senai!!", "\nPor favor, preencha os campos abaixo para realizar o cadastro")

# Cadastro de Cliente:
#O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.

nomes = []
idades = []
celulares = []
quartos = []
dias_estadia = []
valores_totais = []

# cadstrando o  primeiro cliente
nome_1 = input("Digite seu nome completo: ")
idade_1 = int(input("Digite sua idade: "))
celular_1 = input("Digite seu número de celular: ")
nomes.append(nome_1)
idades.append(idade_1)
celulares.append(celular_1)
print("Cadastro realizado!\n")

continuar = input("Deseja cadastrar outro visitante? (s/n): ")

if continuar == "s":

    # cadastrando o segundo cliente
    nome_2 = input("Digite o nome completo do segundo cliente: ")
    idade_2 = int(input("Digite a idade: "))
    celular_2 = input("Digite o número de celular: ")
    nomes.append(nome_2)
    idades.append(idade_2)
    celulares.append(celular_2)
    print("Cadastro realizado!\n")

    continuar = input("Deseja cadastrar outro visitante? (s/n): ")

    if continuar == "s":


        # cadastrando o terceiro cliente
        nome_3 = input("Digite o nome completo do terceiro cliente: ")
        idade_3 = int(input("Digite a idade: "))
        celular_3 = input("Digite o número de celular: ")
        nomes.append(nome_3)
        idades.append(idade_3)
        celulares.append(celular_3)
        print("Cadastro realizado!\n")

# Reservas de Quartos:
# O sistema deve oferecer 3 tipos de quartos:"Simples", "Duplo" e "Luxo".

print("\nTipos de quartos disponíveis:")
print("1 - Simples (R$ 100,00 por dia)")
print("2 - Duplo   (R$ 150,00 por dia)")
print("3 - Luxo    (R$ 250,00 por dia)\n")

# Cliente 1
print(f"{nomes[0]}, escolha seu tipo de quarto:")
quarto_1 = input("Digite Simples, Duplo ou Luxo: ")
dias_1 = int(input("Quantos dias de estadia? "))
quartos.append(quarto_1)
dias_estadia.append(dias_1)

if quarto_1 == "Simples":
    total_1 = dias_1 * 100
elif quarto_1 == "Duplo":
    total_1 = dias_1 * 150
elif quarto_1 == "Luxo":
    total_1 = dias_1 * 250
else:
    total_1 = 0
valores_totais.append(total_1)

# Cliente 2 
if len(nomes) > 1:
    print(f"\n{nomes[1]}, escolha seu tipo de quarto:")
    quarto_2 = input("Digite Simples, Duplo ou Luxo: ")
    dias_2 = int(input("Quantos dias de estadia? "))
    quartos.append(quarto_2)
    dias_estadia.append(dias_2)

    if quarto_2 == "Simples":
        total_2 = dias_2 * 100
    elif quarto_2 == "Duplo":
        total_2 = dias_2 * 150
    elif quarto_2 == "Luxo":
        total_2 = dias_2 * 250
    else:
        total_2 = 0
    valores_totais.append(total_2)

# Cliente 3 
if len(nomes) > 2:
    print(f"\n{nomes[2]}, escolha seu tipo de quarto:")
    quarto_3 = input("Digite Simples, Duplo ou Luxo: ")
    dias_3 = int(input("Quantos dias de estadia? "))
    quartos.append(quarto_3)
    dias_estadia.append(dias_3)

    if quarto_3 == "Simples":
        total_3 = dias_3 * 100
    elif quarto_3 == "Duplo":
        total_3 = dias_3 * 150
    elif quarto_3 == "Luxo":
        total_3 = dias_3 * 250
    else:
        total_3 = 0
    valores_totais.append(total_3)

# Carrinho:
print("\n--- RESERVAS ---")
if len(nomes) >= 1:
    print(f"{nomes[0]} - Quarto: {quartos[0]} - Dias: {dias_estadia[0]} - Total: R$ {valores_totais[0]:.2f}")
if len(nomes) >= 2:
    print(f"{nomes[1]} - Quarto: {quartos[1]} - Dias: {dias_estadia[1]} - Total: R$ {valores_totais[1]:.2f}")
if len(nomes) == 3:
    print(f"{nomes[2]} - Quarto: {quartos[2]} - Dias: {dias_estadia[2]} - Total: R$ {valores_totais[2]:.2f}")
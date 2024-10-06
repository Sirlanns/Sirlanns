#O codígo é basicamente uma classificação de compra de ingresso em:
#ingresso de estudante(mais barato por disconto) e ingresso normal(preço normal do ingresso)
# - caso o estudante confirme sua indetidade como estudante por meio do seu id ele vai ter o desconto
# - uma seleção especifica de numeros vai ser permitida, além de uma quantidade certa
# - vou tentar usar um metodo de lista de numeros pre difinidos como identidade estudantiu(uma lista de cadastros aceitaveis)

print(" - Bem vindo ao cinema North way! por favor escolha seu filme -\n ")
print(" ¹ ⁕[2019]Avengers Ultimato ~ R$ 30,00 ")
print(" ² ⁕[2024]Deadpool e Wolverine ~ R$ 20,00 ")
print(" ³ ⁕[2024]Duna 2 ~ R$ 50,00 ")
print(" ⁴ ⁕[2024]Alien : Romulos ~ R$ 30,00 ")
print(" ⁵ ⁕[2024]3° guerra mundial : o filme ~ R$ 50,00 ")
print(" ⁶ ⁕[2017]Guardiões da galaxia 2 ~ R$ 20,00 \n\n")

filmes = int(input("escolha os filmes pelos numeros nas laterais: "))
if filmes == 1:
    nome_filme = "Avengers Ultimato"
    valor_do_filme =  30.00
elif filmes == 2:
    nome_filme = "Deadpool e Wolverine"
    valor_do_filme =  20.00
elif filmes == 3:
    nome_filme = "Duna 2"
    valor_do_filme =  50.00
elif filmes == 4:
    nome_filme = "Alien : Romulos"
    valor_do_filme =  30.00
elif filmes == 5:
    nome_filme = "3° guerra mundial : o filme"
    valor_do_filme =  50.00
elif filmes == 6:
    nome_filme = "Guardiões da galaxia 2"
    valor_do_filme =  20.00
else:
    print("filme invalido, por favor escolha novamente")
    exit()

print("- Agora que o filme foi escolhido, voce quer algum alimento para acompanhar? -\n\n")

comida_confirmação = input("sim ou não? ").lower()
if comida_confirmação == "sim":
    print(" - Bem vindo ao menu de comida -\n ")
    print(" ¹ ⁕[pipoca grande] ~ R$ 15,00 ")
    print(" ² ⁕[pipoca media] ~ R$ 10,00")
    print(" ³ ⁕[pipoca pequena] ~ R$ 5,00")
    print(" ⁴ ⁕[refrigerante] ~ R$ 10,00")
    print(" ⁵ ⁕[Sorvete] ~ R$ 2,00")

    comida_tipo = input("escolha os alimentos pelos numeros nas laterais: ")
    comida_tipo_list = [int(x) for x in comida_tipo.split()] # dividir a entrada em uma lista de números

    valor_da_comida = 0
    for comida in comida_tipo_list:
        if comida == 1:
            nome_comida = "pipoca grande" 
            valor_da_comida += 15.00
        elif comida == 2:
            nome_comida = "pipoca media" 
            valor_da_comida += 10.00
        elif comida == 3:
            nome_comida = "pipoca pequena"
            valor_da_comida += 5.00
        elif  comida == 4:
            nome_comida = "refrigerante"
            valor_da_comida += 10.00
        elif  comida == 5:
            nome_comida = "sorvete"
            valor_da_comida += 2.00
        else:
            print("alimento invalido, por favor escolha novamente")
elif  comida_confirmação == "não":
    valor_da_comida = 0
else:
    print("resposta invalida, peça novamente")

print("\n\n- Você tem passe de estudante ou vai usar ingresso normal?")

resposta_ingresso = input("sim ou não? ").lower()
if resposta_ingresso == "sim":
    # Aplicar desconto de 10% para estudantes
    valor_do_filme *= 0.9  # 10% de desconto
    print("Você recebeu um desconto de 10%!")
elif resposta_ingresso == "não":
    # Não aplicar desconto
    pass
else:
    print("Resposta inválida, por favor escolha novamente")
# Soma os valores de todas as escolhas do usuário
valor_total = valor_do_filme + valor_da_comida

# Imprimir recibo
print("\n\n** Recibo **")
print("Filme: {} - R$ {:.2f}".format(nome_filme, valor_do_filme))
if comida_confirmação == "sim":
    print("Comida: ", end="")
    for comida in comida_tipo_list:
        if comida == 1:
            print("Pipoca Grande", end="")
        elif comida == 2:
            print("Pipoca Média", end="")
        elif comida == 3:
            print("Pipoca Pequena", end="")
        elif comida == 4:
            print("Refrigerante", end="")
        elif comida == 5:
            print("Sorvete", end="")
        print(", ", end="")
    print("\nValor da comida: R$ {:.2f}".format(valor_da_comida))
print("Valor total: R$ {:.2f}".format(valor_total))

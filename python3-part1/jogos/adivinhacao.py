print('*********************************')
print("Bem vindo no jogo de Adivinhação!")
print('*********************************')

numero_secreto = 42
total_de_tentativas = 3

while total_de_tentativas > 0:
    print("Tentativa: ", total_de_tentativas)
    chute_str = input("Digite o seu numero: ")

    print("Vc digitou ", chute_str)

    chute = int(chute_str)

    acertou = numero_secreto == chute
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if acertou:
        print("Vc acertou!")
        break
    else:
        if maior:
            print("Vc errou! Chute foi maior")
        elif menor:
            print("Vc errou! Chute foi menor")

    total_de_tentativas = total_de_tentativas - 1
print("Fim do jogo")
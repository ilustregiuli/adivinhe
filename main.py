import random as r

decoracao = "-" * 10;

print(f"{decoracao} Jogo de adivinhação. {decoracao} ")
print("Tente adivinhar o número sorteado!")

tentativas = 5
numero_sorteado = r.randint(1, 50)

while tentativas > 0:
    numero_user = int(input("Digite um número de 1 a 50: "))
    int(numero_user)
    print(numero_sorteado)
    if numero_user != numero_sorteado:
        print("Você errou! Tente novamente.")
        tentativas -= 1
        print(f"Tentativas restantes: {tentativas}")
    else:
        print("Você ACERTOOOU! PARABÉNS!!!")
        break 

    if tentativas == 0:
        print(f"Que pena, você perdeu! O número sorteado era: {numero_sorteado}")
        break

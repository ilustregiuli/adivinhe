import random as r

decoracao = "-" * 10

print(f"{decoracao} Jogo de adivinhação. {decoracao} ")
print("Tente adivinhar o número sorteado!")

tentativas = 5
numero_sorteado = r.randint(1, 50)

while True:
    numero_user = int(input("Digite um número de 1 a 50: "))
    print(numero_sorteado)
    if numero_user > 50 or numero_user < 1:
        print("Você digitou um número for do intervalo. Digite novamente.")
    else:    
        if numero_user != numero_sorteado:
            if tentativas == 1:
                print("Você errou!")
                print(f"O número sorteado era: {numero_sorteado}")
                print("Que pena, fim de jogo!")
                break
            print("Você errou! Tente novamente.")
            if numero_user > numero_sorteado:
                altura = "menor"
            else:
                altura = "maior"    
            print(f"Dica: o número sorteado é : {altura} que o número que você digitou!")
            tentativas -= 1 # tentativa = tentativa - 1 
            print(f"Tentativas restantes: {tentativas}")
        else:
            print("Você ACERTOOOU! PARABÉNS!!!")
            break

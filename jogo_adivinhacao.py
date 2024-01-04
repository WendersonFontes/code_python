import random

numero_secreto = random.randint(1, 100)
tentativas = 0
adivinhou = False

print("Adivinhe o número!")

while not adivinhou:
    tentativa = int(input("Digite um número: "))
    tentativas += 1

    if tentativa == numero_secreto:
        print(f"Parabéns! Você acertou em {tentativas} tentativas.")
        adivinhou = True
    elif tentativa < numero_secreto:
        print("Tente um número maior.")
    else:
        print("Tente um número menor.")

    continuar = input("Digite 'c' para continuar ou qualquer outra tecla para desistir: ")
    if continuar.lower() != 'c':
        print(f"Você desistiu! O número era {numero_secreto}.")
        break

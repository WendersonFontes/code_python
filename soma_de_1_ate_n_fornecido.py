numero_usuario = int(input("Digite um número para obter a soma de 1 até esse valor: "))
soma = 0

for i in range(1, numero_usuario + 1):
    soma += i

print(f"A soma dos números de 1 até {numero_usuario} é: {soma}")

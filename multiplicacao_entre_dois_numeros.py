while True:
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        calc = num1 * num2
        print(f"O resultado da multiplicação é: {calc}")
        break
    except ValueError:
        print("Por favor, digite números válidos.")

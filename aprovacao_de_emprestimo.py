valor_casa = float(input('Qual é o valor da casa? R$'))
salario_comprador = float(input('Qual é o salário do comprador? R$'))
anos_pagamento = int(input('Em quantos anos pretende pagar? '))
prestacao_mensal = valor_casa / (anos_pagamento * 12)
limite_percentual = 30

if prestacao_mensal <= (salario_comprador * limite_percentual / 100):
    print('Empréstimo APROVADO! Prestação mensal será de R${:.2f}'.format(prestacao_mensal))
else:
    print('Empréstimo NEGADO! A prestação excede 30% do salário.')

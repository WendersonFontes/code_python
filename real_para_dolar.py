real = float(input('Quanto dinheiro você tem na carteira?'))
cotacao_atual = float(input('qual é a cotação atual do dolar?'))
dolar = real / cotacao_atual
print('Com R$ {:.2f} você pode comprar US$ {:.2f}'.format(real, dolar))

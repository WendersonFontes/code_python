n = float(input('Uma distância em metros: '))
print('A medida de {}m corresponde a:'.format(n))
a = n / 1000
b = n / 100
c = n / 10
d = n * 100
e = n * 1000
print('\n{} km \n{} hm \n{} dam \n{:.0f} cm \n{:.0f} mm'.format(a, b, c, d, e))

Largura = float(input('Largura da parede: '))
Altura = float(input('Altura da parede: '))
Area = Largura * Altura
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área é de {:.2f} m².'.format(Largura, Altura, Area))
tinta = Area / 2
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format(tinta))


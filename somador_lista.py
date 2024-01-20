#CLASSE: SOMADOR
#PARÂMETRO: LISTA
#FUNÇÃO: SOMAR ELEMENTOS
#INSTÂNCIA: SOMADOR

class Somador:
    def __init__ (self, lista):
        self.lista = lista

    def somar_elementos(self):
        return sum(self.lista)
    
minha_lista = [1, 2, 3, 4, 5]
somador = Somador(minha_lista)

resultado = somador.somar_elementos()

print(resultado)

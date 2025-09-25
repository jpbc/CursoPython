# Se crea la Clase gelatina
class Gelatina:
# Se Define el metodo constructor
    def __init__(self, sabor, color, tamanio):
        self.sabor= sabor
        self.color = color
        self.tamanio = tamanio
# Se define el metodo impresión  
    def imprimir(self):
        print(f'La gelatina es de {self.sabor}')
        print(f'La gelatina se ve {self.color}')
        print(f'La gelatina es de {self.tamanio}')
# Se crean las instancias gel1, gel2, gel3    
gel1=Gelatina('Frutilla','Rojo','Grande')
gel2=Gelatina('Limon','Verde','mediana')
gel3=Gelatina('Piña','Amarilla','Pequeña')
# se crea una lista de gelatinas
gelatinas = [gel1,gel2,gel3]
# se recorre e imprime la lista usando el metodo imprimir
for gelatina in gelatinas:
    gelatina.imprimir()
    print('_________________________________')
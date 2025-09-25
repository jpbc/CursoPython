class Gelatina:
    def __init__(self, sabor, color, tamanio):
        self.sabor= sabor
        self.color = color
        self.tamanio = tamanio
    
    def imprimir(self):
        print(f'La gelatina es de {self.sabor}')
        print(f'La gelatina se ve {self.color}')
        print(f'La gelatina es de {self.tamanio}')
    
gel1=Gelatina('Frutilla','Rojo','Grande')

gel1.imprimir()
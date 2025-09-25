# se crea la clase Coche
class Coche:
    # se  crea metodo contrsuctor
    def __init__(self, marca, kilometros, anio):
        self.marca = marca
        self.kilometros= kilometros
        self.anio= anio
        print(f'Se ha creado un auto {self.marca} con {self.kilometros} y año {self.anio}')
# Se crea el metodo para borrar
    def __del__(self):
        print(f'Se ha vendido el auto {self.marca}')
    def __str__(self):
        return 'El auto es un {}. tiene {} kilometros y es del año {}'.format(self.marca, self.kilometros, self.anio)
miCoche=Coche('Audi', 200, 1997)
# Se borra la clase        

#del(miCoche)


print(str(miCoche))
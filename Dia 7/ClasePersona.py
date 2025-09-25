# Se crea la clase Persona
class Persona:
# Se crean los metodos contructor y datos personales
    def __init__(self, nombre, edad, sexo):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
    
    def datosPersonales(self):
        print(f'El nombre de la persona es {self.nombre}')
        print(f'La edad de la persona es {self.edad}')
        print(f'El sexo de la persona es {self.sexo}')
# se crean las instancias de la clase
persona1 = Persona ('Maria', 28, 'Femenino')
persona2 = Persona ('Juan', 19, 'Masculino')
persona3 = Persona ('Carmen', 54, 'Femenino')
# se crea la lista de personas
personas = [persona1,persona2,persona3]
# se recorre y se muestra las intancias de la clase persona
for persona in personas:
    persona.datosPersonales()
    print('__________________________')
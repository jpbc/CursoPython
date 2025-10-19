# Definición de la clase Persona
class Persona:
    def __init__(self, nombre, edad, sexo, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.nacionalidad = nacionalidad

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"Sexo: {self.sexo}")
        print(f"Nacionalidad: {self.nacionalidad}")

# Crear una instancia de la clase Persona
persona1 = Persona("Valery", 20, "Femenino", "Colombiana")

# Mostrar la información de la persona
persona1.mostrar_info()

class Auto:
    def __init__(self, marca, modelo, año, color):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.encendido = False
    def estado_auto(self):
        if self.encendido:
            return "El auto esta encendido."
        else:
            return "El auto esta apagado"
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
# instancia de  la clase auto
mi_auto= Auto("Chevrolet", "Sail", 2022, "Gris Arena")
# Ver estado Inicial 
print(mi_auto.estado_auto())
# Encender el Auto 
mi_auto.encender()
print(mi_auto.estado_auto())
mi_auto.apagar ()
print(mi_auto.estado_auto())

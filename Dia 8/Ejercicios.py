# Ejercicio 1 de Herencia
class Persona:
    def __init__(self, nombre, apellido, edad, sexo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo
#   def datosPersonales(self):
#        print (f'El colaborador {self.nombre} {self.apellido} con {self.edad} años y sexo {self.sexo} ')
#Clase Empleado que hereda a persona
class Empleado (Persona):
    def __init__(self, nombre, apellido, edad, sexo, antiguedad, salario):
        super().__init__(nombre, apellido, edad, sexo)  # Hereda atributos de Persona
        self.antiguedad = antiguedad
        self.salario = salario
    def DatosEmpleado(self):
        print(f'El empleado {self.nombre} {self.apellido} con {self.edad} años de edad y sexo {self.sexo} tiene una antiguedad de  {self.antiguedad} con un salario de {self.salario: ,.2f} pesos')
miEmpleado = Empleado('Valery', 'Hurtado', 20,'Femenino','2 años', 700000)
miEmpleado.DatosEmpleado()
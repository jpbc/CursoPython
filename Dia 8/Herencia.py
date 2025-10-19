# Creando Clase de Persona para aplicar concepto de herencia
class Persona:
    def __init__(self, nombre, edad, apellido, sexo):
        self.nombre = nombre
        self.edad = edad
        self.apellido = apellido
        self.sexo = sexo

    
    
    def DatosPersonales (self):
        print(f'El nombre de la persona es: {self.nombre} ')
        print(f'La edad de la persona es: {self.edad} ')
        print(f'El apellido de la persona es: {self.apellido} ')
        print(f'la edad de la persona es: {self.sexo} ')

miPersona = Persona('Ana', 48,'Hurtado','Femenino')
miPersona.DatosPersonales()

# Ocupando Herencia creando clase empleado, que tambien es persona

class Empleado(Persona):
    def DatosEmpleado (self, vacaciones, salario):
        print (f'Sus dias de vacaciones son: {vacaciones}')
        print (f'Su salario es: {salario: ,.2f}')
miEmpleado = Empleado('Valery',20,'Borrero', 'Femenino')
miEmpleado.DatosPersonales()
miEmpleado.DatosEmpleado('30 dias', 600000)
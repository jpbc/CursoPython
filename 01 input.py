from datetime import datetime
# Con el input podemos pedir por teclado información a un usuario
entrada = input('Por favor ingrese su nombre : ')
nacimiento = input('Ingrese su fecha de nacimiento : ')

# Convertir el texto a un objeto datetime
fecha_objeto = datetime.strptime(nacimiento, "%d-%m-%Y")

# Extraer el año
año = fecha_objeto.year

# Compara si el mes y el dia es menor al año de la fecha de nacimiento para hacer ajuste en la edad
if (datetime.now().month, datetime.now().day)<(fecha_objeto.month, fecha_objeto.day):
    diferencia = -1

# datetime.now().year trae la fecha actual
print('Hola ', entrada, 'su edad es', datetime.now().year-año +diferencia)

def restar (num1,num2):
    return num1-num2
def sumar (num1,num2):
    return num1+num2
def multiplicar (num1,num2):
    return num1*num2
def dividir (num1,num2):
    try:
        return num1/num2
    # Se captura el error y se devuelve un mensaje
    except ZeroDivisionError:
        print('No se puede dividir entre 0')
        # Se le indica al usuario que la operacion no es valida
        return 'Operacion no Valida'

op1 = int(input('Introduce el primer valor : '))
op2 = int(input('Introduce el segundo valor : '))

operacion = input('Introduce la operacion a realizar ---> \n\t\t Sumar \n\t\t Restar \n\t\t Multiplicar \n\t\t Dividir : \n\t\t \t\t ')
if operacion=='Sumar':
    print(sumar(op1,op2))
elif operacion=='Restar':
    print(restar(op1,op2))
elif operacion=='Multiplicar':
    print(multiplicar(op1,op2))    
elif operacion=='Dividir':
    print(dividir(op1,op2))
else:
    print ('NO SE ENCUENTRA DENTRO DE LAS OPCIONES')
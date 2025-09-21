def saludar():
    return 'Hola mundo'
print(saludar())


def saludar2():
    return print('Hola mundo')

saludar2()

# todo lo que se incluya en el return sera mostrado 
def saludar3():
    return ('Hola mundo',1,[4,5,6])
print(saludar3())
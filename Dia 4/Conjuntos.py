conjunto = set()
conjunto={2, 'Python', 'Bryan', True}

#agregar elementos con add
conjunto.add(False)


print (conjunto)

#eliminar un valor con discard
conjunto.discard('Bryan')

print (conjunto)

# limpiar un conjunto con clear
# conjunto.clear()

# Preguntando sy el valor Python se encuentra dentro del conjunto
print('Python' in conjunto)
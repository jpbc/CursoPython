usernames = ['andres', 'pedro', 'jean', 'luis']
passwords = ['1234','5678','9012','3456']

user = input("Ingrese el nombre de usuario: ")
password = input ("ingrese la clave :")

authenticated = False

for i in range(len(usernames)):
    if usernames[i] == user and  passwords [i] == password:
        authenticated = True
        break
if authenticated:
    print (f"Bienvenido {user.upper()}, ha iniciado sesión con exito")
else:
    print ("Lo sentimos requiere autenticación")
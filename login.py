#python3
#Pequeño programa de inicio de sesión, la información será guardada en un documento de texto

import sys

menu = """
Bienvenido a mi sistema de Login, en el podrás
crear un usuario y contraseña, iniciar sesion y
si lo deseas podrás borrar tu usuario y contraseña.

Estas estarán en un lugar seguro, no te preocupes

    1 - Iniciar sesión
    2 - Cerrar sesión
    3 - Crear cuenta
    4 - Eliminar cuenta
    5 - Salir
"""

usuario = ''
contrasenia = ''
sesion_iniciada = False


def inicio_sesion():
    usuario_file = open('D:\\vs_programs\\automatizar\\login\\login_info.txt', 'r')
    info_texto = usuario_file.read()
    info_texto = info_texto.split()
    
    usuario = input('Ingresa tu nombre de usuario: ')
    contrasenia = input('Ingresa tu contraseña: ')
    if usuario in info_texto and contrasenia in info_texto:
        print('=====Acceso concedido=====')
        sesion_iniciada = True
        main()
    else:
        print('Tu usuario o contraseña son incorrectas, vuelve a intentarlo')
        inicio_sesion()

#TODO cerrar sesion
def cerrar_sesion():
    sesion_iniciada = sesion_iniciada
    if sesion_iniciada == True:
        print('=====Sesion cerrada=====')
        sesion_iniciada = False
        main()
    else:
        print('Primero debes iniciar sesion!')
        main()
#TODO crear cuenta

#TODO eliminar cuenta

#TODO salir

def main():
    print(menu)
    eleccion = ''
    while eleccion != 5:
        eleccion = input('Ingrese la opción de su elección: ')
        if eleccion == 1:
            inicio_sesion()
        elif eleccion == 2:
            cerrar_sesion()
        elif eleccion == 3:
            pass
            #funcion crear cuenta
        elif eleccion == 4:
            pass
            #funcion eliminar cuenta
        else:
            sys.exit()
    
if __name__ == "__main__":
    main()
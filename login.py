#python3
#Pequeño programa de inicio de sesión, la información será guardada en un documento de texto

import sys

menu = """
Bienvenido a mi sistema de Login, en el podrás
crear un usuario y contraseña, iniciar sesion y
si lo deseas podrás borrar tu usuario y contraseña.

Estas estarán en un lugar seguro, no te preocupes

    1 - Iniciar sesión
    2 - Crear cuenta
    3 - Eliminar cuenta
    4 - Salir
"""

usuario = ''
contrasenia = ''

#TODO iniciar sesion
def inicio_sesion():
    usuario_file = open('D:\\vs_programs\\automatizar\\login\\login_info.txt', 'r')
    info_texto = usuario_file.read()
    info_texto = info_texto.split()
    
    usuario = input('Ingresa tu nombre de usuario: ')
    contrasenia = input('Ingresa tu contraseña: ')
    if usuario in info_texto and contrasenia in info_texto:
        print('=====Acceso concedido=====')
    else:
        print('Tu usuario o contraseña son incorrectas, vuelve a intentarlo')
        inicio_sesion()
#TODO crear cuenta

#TODO eliminar cuenta

#TODO salir

def main():
    print(menu)
    eleccion = ''
    while eleccion != 4:
        eleccion = input('Ingrese la opción de su elección: ')
        if eleccion == 1:
            pass
            #funcion inicio sesion
        elif eleccion == 2:
            pass
            #funcion crear cuenta
        elif eleccion == 3:
            pass
            #funcion eliminar cuenta
        else:
            sys.exit()
    
if __name__ == "__main__":
    inicio_sesion()
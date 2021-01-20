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
        global sesion_iniciada 
        sesion_iniciada = True
        main()
    else:
        print('Tu usuario o contraseña son incorrectas, vuelve a intentarlo')
        inicio_sesion()


def cerrar_sesion():
    global sesion_iniciada 
    if sesion_iniciada == True:
        print('=====Sesion cerrada=====')
        sesion_iniciada = False
        main()
    else:
        print('Primero debes iniciar sesion!')
        main()


def crear_cuenta():
    crear_usuario_archivo = input('Ingresa tu nombre de usuario: ')
    craer_contrasenia_archivo = input('Ingresa tu contraseña: ')
    escribir_archivo = open('D:\\vs_programs\\automatizar\\login\\login_info.txt', 'a')
    escribir_archivo.write('\n'+ crear_usuario_archivo + ' ' + craer_contrasenia_archivo)
    escribir_archivo.close()


def eliminar_cuenta():
    usuario_file = open('D:\\vs_programs\\automatizar\\login\\login_info.txt', 'r')
    info_texto = usuario_file.read()
    info_texto = info_texto.split()

    print(info_texto)


def main():
    print(menu)
    eleccion = 0
    while eleccion != 5:
        eleccion = int(input('Ingrese la opción de su elección: '))
        if eleccion == 1:
            inicio_sesion()
        elif eleccion == 2:
            cerrar_sesion()
        elif eleccion == 3:
            crear_cuenta()
        elif eleccion == 4:
            eliminar_cuenta()
        else:
            sys.exit()
    
if __name__ == "__main__":
    main()
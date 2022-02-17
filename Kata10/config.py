
#Al crear el directorio config.txt no me da el error mencionado en la documentación de la Kata

""" def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Could't find the config.txt file!")

def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("Couldn't find the config.txt file!")
    except IsADirectoryError:
        print("Found config.txt but it is a directory, couldn't read it")
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

    if __name__ == '__main__':
        main()
"""
def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontró el archivo")
    except IsADirectoryError:
        print('Se encontró config.txt pero es un directorio, no se puede leer')
    except PermissionError:
        print('No hay permisos suficientes')
    except (BlockingIOError, TimeoutError):
        print("Filesystem under heavy load, can't complete reading configuration file")

if __name__ == '__main__':
    main()

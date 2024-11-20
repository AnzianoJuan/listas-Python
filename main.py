#  Creamos 3 listas en Python. Las mismas deben contener:
#  lenguajes de programación
#  sistemas operativos
#  stacks tecnológicos
# Crea un ciclo while el cual, al ejecutarse, imprima un menú de opciones listando:
#  1. Visualizar lenguajes de programación
#  2. Visualizar sistemas operativos
#  3. Visualizar stacks tecnológicos
#  0. Salir


def main():
    try:
        lenguajes = ["Python", "Java", "JavaScript"]
        sistemas_operativos = ["Windows", "Linux", "macOS"]
        stacks_tecnologicos = ["MERN", "MEAN", "LAMP"]

        menu = 0  
        while menu != "0":  
            print("1. Mostrar lenguajes")
            print("2. Mostrar sistemas operativos")
            print("3. Mostrar stacks tecnológicos")
            print("0. Salir")
            
            menu = input("Seleccione una opción: ")
            
            if menu == "1":
                print("Lenguajes:", lenguajes)
            elif menu == "2":
                print("Sistemas Operativos:", sistemas_operativos)
            elif menu == "3":
                print("Stacks Tecnológicos:", stacks_tecnologicos)
            elif menu == "0":
                print("Saliendo del programa...")
            else:
                print("Debe elegir un valor que sea 1, 2, 3 o 0.")
    except:
        print("error")

main()

diccionario = [["print","imprimir"],["input","Entrada"]]
def CrearCodigo():
    codigo = input("Ingrese su codigo: ")

def Compilar():
    ""

def Menu():
    try:
        while True:
                opcionMenu = int(input("Bienvenido a PyTEC\n\nQue desea hacer:\n\n1)Nuevo Codigo\n2)Compilar\n\nElije una opcion: "))
                if opcionMenu < 0 or opcionMenu > 3:
                    print("ERROR")
                else:
                    if opcionMenu == 1:
                        CrearCodigo()
                        break
                    elif opcionMenu == 2:
                        Compilar()
                        break
    except:
        print("POR FAVOR, DIGITE VALORES NUMERICOS")
        Menu()
Menu()









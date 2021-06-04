import time
from multiprocessing import Process, Queue
from funcion1 import clase1
from funcion2 import clase2
from funcion3 import clase3

# VARIABLES GLOBALES
primera = clase1()
segunda = clase2()
tercera = clase3()


# MENU
def menu():
    while True:
        print("[1] Ingresar Problema 1")
        print("[2] Ingresar Problema 2")
        print("[3] Ingresar Problema 3")

        print('Ingrese una opcion: ', end="")
        opc = input()
        print("")
        if str(opc)=="1":
            print(f"Ingreso {opc}")
            primera.saludar()
            break
        elif str(opc)=="2":
            print(f"Ingreso {opc}")
            segunda.despedir()
            break
        elif str(opc)=="3":
            print(f"Ingreso {opc}")
            tercera.preguntar()
            break
        else:
            print("[~] OPCION INCORRECTA [~]\n")
            continue



# MAIN
def main():
    menu()
    print("\n")


if __name__ == "__main__":
    main()

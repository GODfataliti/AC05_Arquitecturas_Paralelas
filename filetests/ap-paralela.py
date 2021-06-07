import time
from multiprocessing import Process, Queue
from funcion1 import clase1
from funcion2 import clase2
from funcion3 import clase3

# VARIABLES GLOBALES
primera = clase1() #PIPE
segunda = clase2() #PIPE
tercera = clase3() #COLA


# MENU
def menu():
    while True:
        print("======================================")
        print("[1] Ingresar Problema [1]")
        print("[2] Ingresar Problema [2]")
        print("[3] Ingresar Problema [3]")
        print("[4]      Salir        [4]")

        print('[!] Ingrese una opcion [>]: ', end="")
        opc = input()
        print("")
        if str(opc)=="1":
            primera.start()
            print("======================================")
            break
        elif str(opc)=="2":
            print(f"Ingreso {opc}")
            segunda.despedir()
            print("======================================")
            break
        elif str(opc)=="3":
            print(f"Ingreso {opc}")
            tercera.preguntar()
            print("======================================")
            break
        elif str(opc)=="4":
            print("[!] Hasta pronto [!]")
            print("======================================")
            break
        else:
            print("[~] OPCION INCORRECTA [~]\n")
            print("======================================")
            continue


# MAIN
# UNIR CON JOIN AL FINAL.
def main():
    tm = time.time()
    menu()
    print(f'Tiempo: {time.time() - tm} \n')


if __name__ == "__main__":
    main()

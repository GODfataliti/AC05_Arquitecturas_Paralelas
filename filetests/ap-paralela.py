import time
from multiprocessing import Process, Queue
import os
from funcion1 import clase1
from funcion2 import clase2
from funcion3 import clase3
from funcion4 import clase4

# VARIABLES GLOBALES
primera = clase1() #PIPE
segunda = clase2() #PIPE
tercera = clase3() #COLA
cuarta = clase4()


# MENU
def menu():
    try:
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
                cuarta.start()
                print("======================================")
                break
            elif str(opc)=="2":
                segunda.start()
                print("======================================")
                break
            elif str(opc)=="3":
                tercera.start()
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
    except Exception as e:
        print(f"[ERROR] Ha ocurrido un problema: {e} [!]")


# MAIN
# UNIR CON JOIN AL FINAL.
def main():
    tm = time.time()
    menu()
    #print(f'Tiempo: {time.time() - tm} \n')


if __name__ == "__main__":
    main()

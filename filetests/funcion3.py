import time
from multiprocessing import Process, Queue
import random
import os


#COLA
class clase3:

    def colores1(self,lista,colores1):
        valor1 = random.choice(lista)
        valor2 = random.choice(lista)
        lista = []
        lista.append(valor1)
        lista.append(valor2)
        colores1.put(lista)
        print(f'[3] Lista: {lista}  PID:{os.getpid()} [3]')
    
    def colores2(self,lista,colores2):
        valor1 = random.choice(lista)
        valor2 = random.choice(lista)
        lista = []
        lista.append(valor1)
        lista.append(valor2)
        colores2.put(lista)
        print(f'[3] Lista: {lista}  PID:{os.getpid()} [3]')

    def colores3(self,lista,colores3):
        valor1 = random.choice(lista)
        valor2 = random.choice(lista)
        lista = []
        lista.append(valor1)
        lista.append(valor2)
        colores3.put(lista)
        print(f'[3] Lista: {lista}  PID:{os.getpid()} [3]')
    
    def start(self):
        
        t = time.time()
        lista_colores = ['Red', 'Yellow', 'Blue']
        lista_colores2 = ['Green','Purple','Orange']
        lista_colores3 = ['Black','White']

        
        colores1 = Queue()
        colores2 = Queue()
        colores3 = Queue()

        p1 = Process(target=self.colores1, args=(lista_colores,colores1,))
        p2 = Process(target=self.colores2, args=(lista_colores2,colores2,))
        p3 = Process(target=self.colores3, args=(lista_colores3,colores3,))
        p1.start()
        p2.start()
        p3.start()

        clist = colores1.get()
        clist2 = colores2.get()
        clist3 = colores3.get()

        #SUMAR COLORES 
        if 'Red' in clist[0]:
            if 'Red' in  clist[1]:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Red'}")
            elif 'Yellow' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Orange'}")
            elif 'Blue' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Purple'}")
        
        if 'Yellow' in clist[0]:
            if 'Yellow' in clist[1]:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Yellow'}")
            elif 'Red' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Orange'}")
            elif 'Blue' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Green'}")
        
        if 'Blue' in clist[0]:
            if 'Blue' in clist[1]:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Blue'}")
            elif 'Red' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Purple'}")
            elif 'Yellow' in clist:
                print(f"[3] GET COLORES 1: {clist} SUMA: {'Green'}")

        #==================================================================
        if 'Green' in clist2[0]:
            if 'Green' in  clist2[1]:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Green'}")
            elif 'Purple' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Grayish'}")
            elif 'Orange' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Lilac'}")
        
        if 'Purple' in clist2[0]:
            if 'Green' in clist2[1]:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Grayish'}")
            elif 'Purple' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Purple'}")
            elif 'Orange' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Reddish ocher'}")
        
        if 'Orange' in clist2[0]:
            if 'Green' in clist2[1]:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Lilac'}")
            elif 'Purple' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Reddish ocher'}")
            elif 'Orange' in clist2:
                print(f"[3] GET COLORES 2: {clist2} SUMA: {'Orange'}")
        
        #=============================================================================
        if 'Black' in clist3[0]:
            if 'Black' in clist3[1]:
                print(f"[3] GET COLORES 3: {clist3} SUMA: {'Black'}")
            elif 'White' in clist3:
                print(f"[3] GET COLORES 3: {clist3} SUMA: {'Gray'}")
        
        if 'White' in clist3[0]:
            if 'White' in clist3[1]:
                print(f"[3] GET COLORES 3: {clist3} SUMA: {'White'}")
            elif 'Black' in clist3:
                print(f"[3] GET COLORES 3: {clist3} SUMA: {'Gray'}")
        
        print(f'[3] PID:{os.getpid()} [3]')
        print(f'[3] Tiempo de ejecucion: {time.time()-t} seg. [3]')

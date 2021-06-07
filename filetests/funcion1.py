import time
from multiprocessing import Process, Pipe, Queue, process
import math
import random

#PIPE
class clase1:

    def generadorRandom(self):

        x = [random.randint(0,15) for _ in range(random.randint(3,8)+1)]
        return x
    
    #FUNCION 1
    def cubo(self,q1,list1,datos1):

        for x in datos1:
            Cubo= x**3
            Proceso = 0
            list1.append(Cubo)
            for j in list1:
                Proceso+=j
        print(f"Proceso Calculo 1: {Proceso}")
        q1.send(Proceso)
        q1.close()
    
    #FUNCION 2
    def log(self,connect1,q2):
        x = connect1.recv()
        x = math.log10(x)
        print(f'Proceso Calculo 2: {x}')
        q2.send(x)
        #q2.close()

    #FUNCION 3
    def raizlog(self,connect2,q3):
        y = connect2.recv()
        y = math.sqrt(y)
        print(f'Pronceso Calculo 3: {y}')
        q3.send(y)
    
    #MAIN
    def start(self):
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        datos1 = self.generadorRandom()
        datos2 = self.generadorRandom()
        lista1 = []
        p1 = Process(target=self.cubo, args=(q1,lista1,datos1,))
        p2 = Process(target=self.log, args=(connect1,q2,))
        p3 = Process(target=self.raizlog, args=(connect2,q3,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
    


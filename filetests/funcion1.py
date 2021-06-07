import time
from multiprocessing import Process, Pipe, Queue, process
import math
import random

#PIPE
class clase1:

    def generadorRandom(self):

        x = [x for n in range(random.randint(15))]
        return x
    
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
    

    def log(self,connect1,q2):
        x = connect1.recv()
        x = math.log10(x)
        print(f'Proceso Calculo 2: {x}')
        q2.send(x)
        #q2.close()


    def raizlog(self,connect2,q3):
        y = connect2.recv()
        y = math.sqrt(y)
        print(f'Pronceso Calculo 3: {y}')
        q3.send(y)
    
    def start(self):
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        datos1 = self.generadorRandom()
        datos2 = self.generadorRandom()
        lista1 = []
        p1 = Process(target=cubo, args=(q1,lista1,datos1))
    


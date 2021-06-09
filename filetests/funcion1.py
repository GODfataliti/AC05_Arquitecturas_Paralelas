import time
from multiprocessing import Process, Pipe, Queue
import math
import random
import os

#PIPE
class clase1:

    def generadorRandom(self):

        x = [random.randint(0,15) for _ in range(random.randint(3,8)+1)]
        return x
    
    #FUNCION 1 PROMEDIO
    def promedio(self,q1,datos):
        promedio = 0
        for valor in datos:
            promedio+=valor
        
        promedio = promedio/len(datos)
        print(f"[1] Proceso Calculo 1: {datos} - Promedio: {promedio} [1]")
        q1.send(promedio)
        q1.close()

    #FUNCION 2 VARIANZA
    def varianza(self,connect1,q2,datos):
        promedio = connect1.recv()
        varianza = 0
        for valor in datos:
            varianza+=(valor-promedio)**2
        
        varianza = varianza/len(datos)
        print(f'[1] Proceso Calculo 2 - Varianza: {varianza} [1]')
        q2.send(varianza)
        q2.close()


    #FUNCION 3 DESVIACION ESTANDAR
    def cv(self,connect2,q3):
        varz = connect2.recv()
        sigma = math.sqrt(varz)
        print(f'[1] Pronceso Calculo 3 - Desviacion Estandar: {sigma} [1]')
        q3.send(sigma)
        q3.close()
        
    #MAIN
    def start(self):
        t= time.time()
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        datos1 = self.generadorRandom()

        p1 = Process(target=self.promedio, args=(q1,datos1,))
        p2 = Process(target=self.varianza, args=(connect1,q2,datos1,))
        p3 = Process(target=self.cv, args=(connect2,q3,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()

        #varianza = connect2.recv()
        promedio = connect1.recv()
        desviacion = connect3.recv()
        cv = (desviacion/promedio)*100



        print(f'[1] Resultado Final: Lista {datos1} CV: {cv} [1]')
        print(f'[1] Tiempo de Ejecucion 1: {time.time()-t} seg. [1]\n')
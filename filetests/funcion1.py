import time
from multiprocessing import Process, Pipe, Queue, process
import math
import random

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

            
        print(f"Proceso Calculo 1: {datos} Promedio: {promedio}")
        q1.send(promedio,datos)
        q1.close()
    
    #FUNCION 2 VARIANZA
    def varianza(self,connect1,q2):
        promeido,list = connect1.recv()
        varianza = 0
        for valor in list:
            varianza+=(valor-promeido)**2
        
        varianza = varianza/len(datos)

        print(f'Proceso Calculo 2: {datos} Varianza {varianza}')
        q2.send(varianza,promeido)
        q2.close()

    #FUNCION 3 COEFICIENTE DE VARIACION
    def cv(self,connect2,q3):
        varz, prom = connect2.recv()
        sigma = math.sqrt(varz)
        cv = (sigma/prom)*100
        print(f'Pronceso Calculo 3: Coeficiente de variacion {cv}')
        q3.send(cv)
        q3.close()
    
    #MAIN
    def start(self):
        t= time.time()
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        datos1 = self.generadorRandom()

        p1 = Process(target=self.promedio, args=(q1,datos1,))
        p2 = Process(target=self.varianza, args=(connect1,q2,))
        p3 = Process(target=self.cv, args=(connect2,q3,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        print(f'Resultado Final: Lista {datos1} C.V: {connect3.recv()}')
        print(f'Tiempo de Ejecucion: {time.time()-t}\n')
    


import time
from multiprocessing import Process, Pipe, Queue, process
import math
import random

#PIPE
class clase2:

    def generadorRandom(self):
        x = random.randint(20,100)+1
        return x
    
    #SUMA DE LOS CUADRADOS
    def SumaCuadrados(self,q1,num):
        summation = 0
        for valor in range (0,num+1):
            summation+=valor**2
        
        print(f"[2] Proceso Calculo 1 - Suma de los Cuadrados: {summation}")
        q1.send(summation)
        q1.close()
    
    #SUMA DE LOS VALORES MULTIPLES
    def sumaMultiples(self,q2,connect1,a,b):
        num = connect1.recv()
        prime = a
        secon = b
        number = 0
        for valor in range(num):
            if(valor%prime==0):
                number+=valor
            
            if (valor%secon==0):
                number+=valor
            
            if (valor%(prime*secon)==0):
                number-=valor

        print(f"[2] Proceso Calculo 2 - Suma de los Multiples: {number}")
        q2.send(number)
        q2.close()
    
    #LOGARITMO DEL VALOR
    def logValor(self,q3,connect2):
        valor = connect2.recv()
        v_log = math.log10(valor)
        print(f"[2] Proceso Calculo 3 - Logaritmo: {v_log}")
        q3.send(v_log)
        q3.close()
    
    #MAIN
    def start(self):
        t= time.time()
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        dato = self.generadorRandom()
        a = 3
        b = 5

        p1 = Process(target=self.SumaCuadrados, args=(q1,dato,))
        p2 = Process(target=self.sumaMultiples, args=(q2,connect1,a,b,))
        p3 = Process(target=self.logValor, args=(q3,connect2,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        print(f'[2] Tiempo de Ejecucion 1: {time.time()-t} seg. [2]\n')

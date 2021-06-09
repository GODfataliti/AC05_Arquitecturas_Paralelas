import time
from multiprocessing import Process, Pipe, Queue
import math
import random
import os

#PIPE
class clase2:

    def generadorRandom(self):
        x = random.randint(20,50)+1
        return x
    
    #SUMA DE LOS CUADRADOS
    def SumaCuadrados(self,q1,num):
        summation = 0
        for valor in range (0,num+1):
            summation+=valor**2
        
        print(f"[2] Proceso Calculo 1 - Suma de los Cuadrados: {summation}    PID:{os.getpid()} [2]")
        q1.send(summation)
        q1.close()
    
    #SUMA DE LOS VALORES MULTIPLES
    def sumaMultiples(self,q2,a,b,num):
        num = num
        prime = a
        secon = b
        number = 0
        for valor in range(num+1):
            if(valor%prime==0):
                number+=valor
            
            if (valor%secon==0):
                number+=valor
            
            if (valor%(prime*secon)==0):
                number-=valor

        print(f"[2] Proceso Calculo 2 - Suma de los Multiplos: {number}      PID:{os.getpid()} [2]")
        q2.send(number)
        q2.close()
    
    #LOGARITMO DEL VALOR
    def logValor(self,q3,num):
        valor = num
        v_log = math.log10(valor)
        print(f"[2] Proceso Calculo 3 - Logaritmo: {v_log}    PID:{os.getpid()} [2]")
        q3.send(v_log)
        q3.close()
    
    #MAIN
    def start(self):
        t= time.time()
        q1,connect1 = Pipe()
        q2, connect2 = Pipe()
        q3, connect3 = Pipe()

        dato = self.generadorRandom()
        a = 15
        b = 7
        print(f"[2] VALOR TOMADO: {dato}    [2]")

        p1 = Process(target=self.SumaCuadrados, args=(q1,dato,))
        p2 = Process(target=self.sumaMultiples, args=(q2,a,b,dato,))
        p3 = Process(target=self.logValor, args=(q3,dato,))
        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()

        diferencia = (connect1.recv() - connect2.recv()) - round(connect3.recv(),3)

        print(f'[2] Diferencia de valores: {diferencia}     PID:{os.getpid()} [2]\n')


        print(f'[2] Tiempo de Ejecucion 1: {time.time()-t} seg. [2]\n')

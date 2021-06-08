from multiprocessing import Process, Pipe, Queue
import math
import time

Base_triangulo = 5
Altura_triangulo = 7
Lado_Cuadrado = 8
Ancho_rectangulo = 4
Largo_rectangulo = 6

class clase4:

    def generadorRandom(self):

        x = random.randint(3,8)+1
        return x

    #Función que calcula el area del triangulo
    def f1(self,q1,Base_triangulo,Altura_triangulo):
        Area_Triangulo = (Base_triangulo*Altura_triangulo)/2
        print(f"[1] Proceso del cálculo 1 - Area Triangulo: {Area_Triangulo}   [1]")
        q1.send(Area_Triangulo)
        q1.close()

    #Función que calcula el area del cuadrado
    def f2(self,q2,Lado_Cuadrado):
        Area_Cuadradro = Lado_Cuadrado*Lado_Cuadrado
        print(f"[1] Proceso del cálculo 2 - Area Cuadrado: {Area_Cuadradro}      [1]")
        q2.send(Area_Cuadradro)
        q2.close()
    
    #Función que calcula el area del rectangulo
    def f3(self,q3,Ancho_rectangulo,Largo_rectangulo):
        Area_Rectangulo = Ancho_rectangulo*Largo_rectangulo
        print(f"[1] Proceso del cálculo 3 - Area Rectangulo: {Area_Rectangulo}    [1]")
        q3.send(Area_Rectangulo)
        q3.close()
    
    def start(self):
        t = time.time()
        q1,conne1 = Pipe()
        q2,conne2 = Pipe()
        q3,conne3 = Pipe()

        p1 = Process(target=self.f1,args=(q1,Base_triangulo,Altura_triangulo,))
        p2 = Process(target=self.f2,args=(q2,Lado_Cuadrado,))
        p3 = Process(target=self.f3, args=(q3,Ancho_rectangulo,Largo_rectangulo,))

        p1.start()
        p2.start()
        p3.start()
        p1.join()
        p2.join()
        p3.join()
        Suma_area = conne1.recv()+conne2.recv()+conne3.recv()
        print(f"[1] La suma de las areas de las figuras geométricas es: {Suma_area}  [1]")
        print(f"[1] Tiempo de ejecución: {time.time()-t} seg.   [1]\n")
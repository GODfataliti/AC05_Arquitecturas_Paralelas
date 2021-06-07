import time
from multiprocessing import Process, Queue

#PIPE
class clase2:

    def generadorRandom(self):

        x = [random.randint(0,15) for _ in range(random.randint(3,8)+1)]
        return x
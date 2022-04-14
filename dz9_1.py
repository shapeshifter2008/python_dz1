from time import sleep
from itertools import cycle

class TraficLight:
    def __init__(self):
        self.__color = (('red', 7), ('yellow', 2), ('green', 3))

    def running(self):
        for color, sec in cycle(self.__color):
            print(color, f'wait {sec} sec')
            if color == 'green':
                break
            sleep(sec)

traffic_light = TraficLight()
traffic_light.running()

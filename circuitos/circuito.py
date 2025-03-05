import numpy as np

class Circuito:
    def __init__(self, fuente, componentes, tiempo=np.linspace(0.001, 0.1, 1000)):
        self.fuente = fuente
        self.componentes = componentes
        self.tiempo = tiempo
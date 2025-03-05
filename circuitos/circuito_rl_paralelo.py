from .circuito import Circuito
import numpy as np

class CircuitoRL_Paralelo(Circuito):
    def __init__(self, fuente, resistencia, inductancia):
        super().__init__(fuente, [resistencia, inductancia])
        self.resistencia = resistencia
        self.inductancia = inductancia

    def voltaje_Circuito(self):
        return np.full_like(self.tiempo, self.fuente.valor)

    def corriente_R(self):
        return np.full_like(self.tiempo, self.fuente.valor / self.resistencia.valor)

    def corriente_L(self):
        return np.cumsum(self.voltaje_Circuito()) * (self.tiempo[1] - self.tiempo[0]) / self.inductancia.valor

    def corriente_Total(self):
        return self.corriente_R() + self.corriente_L()
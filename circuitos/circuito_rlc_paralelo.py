from .circuito import Circuito
import numpy as np

class CircuitoRLC_Paralelo(Circuito):
    def __init__(self, fuente, resistencia, inductancia, capacitancia):
        super().__init__(fuente, [resistencia, inductancia, capacitancia])
        self.resistencia = resistencia
        self.inductancia = inductancia
        self.capacitancia = capacitancia

    def voltaje_Circuito(self):
        return np.full_like(self.tiempo, self.fuente.valor)

    def corriente_R(self):
        return np.full_like(self.tiempo, self.fuente.valor / self.resistencia.valor)

    def corriente_L(self):
        return np.cumsum(self.voltaje_Circuito()) * (self.tiempo[1] - self.tiempo[0]) / self.inductancia.valor

    def corriente_C(self):
        return self.capacitancia.valor * np.gradient(self.voltaje_Circuito(), self.tiempo, edge_order=2)

    def corriente_Total(self):
        return self.corriente_R() + self.corriente_L() + self.corriente_C()
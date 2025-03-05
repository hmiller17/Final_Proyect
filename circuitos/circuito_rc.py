from .circuito import Circuito
import numpy as np

class CircuitoRC(Circuito):
    def __init__(self, fuente, resistencia, capacitancia):
        super().__init__(fuente, [resistencia, capacitancia])
        self.resistencia = resistencia
        self.capacitancia = capacitancia

    def voltaje_R(self):
        return self.fuente.valor * np.exp(-self.tiempo / (self.resistencia.valor * self.capacitancia.valor))

    def voltaje_C(self):
        return self.fuente.valor * (1 - np.exp(-self.tiempo / (self.resistencia.valor * self.capacitancia.valor)))

    def corriente_Circuito(self):
        return self.voltaje_R() / self.resistencia.valor
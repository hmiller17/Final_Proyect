from .circuito import Circuito
import numpy as np
class CircuitoRL(Circuito):
    def __init__(self, fuente, resistencia, inductancia):
        super().__init__(fuente, [resistencia, inductancia])
        self.resistencia = resistencia
        self.inductancia = inductancia

    def corriente_Circuito(self):
        return self.fuente.valor * (1 - np.exp(-self.tiempo / (self.inductancia.valor / self.resistencia.valor))) / self.resistencia.valor

    def voltaje_R(self):
        return self.resistencia.valor * self.corriente_Circuito()

    def voltaje_L(self):
        return self.fuente.valor * np.exp(-self.tiempo / (self.inductancia.valor / self.resistencia.valor))
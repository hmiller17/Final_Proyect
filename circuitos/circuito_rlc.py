from .circuito import Circuito
import numpy as np

class CircuitoRLC(Circuito):
    def __init__(self, fuente, resistencia, inductancia, capacitancia):
        super().__init__(fuente, [resistencia, inductancia, capacitancia])
        self.resistencia = resistencia
        self.inductancia = inductancia
        self.capacitancia = capacitancia

    def corriente_Circuito(self):
        return (self.fuente.valor / self.resistencia.valor * (1 - np.exp(-self.tiempo / (self.inductancia.valor / self.resistencia.valor))))

    def voltaje_R(self):
        return self.resistencia.valor * self.corriente_Circuito()

    def voltaje_L(self):
        return self.inductancia.valor * np.gradient(self.corriente_Circuito(), self.tiempo)

    def voltaje_C(self):
        return self.fuente.valor * (1 - np.exp(-self.tiempo / (self.resistencia.valor * self.capacitancia.valor)))
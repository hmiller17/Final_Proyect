from .circuito import Circuito
import numpy as np

class CircuitoRC_Paralelo(Circuito):
    def __init__(self, fuente, resistencia, capacitancia):
        super().__init__(fuente, [resistencia, capacitancia])
        self.resistencia = resistencia
        self.capacitancia = capacitancia

    def voltaje_Circuito(self):
        return np.full_like(self.tiempo, self.fuente.valor)

    def corriente_R(self):
        return np.full_like(self.tiempo, self.fuente.valor / self.resistencia.valor)

    def corriente_C(self):
        return self.capacitancia.valor * np.gradient(self.voltaje_Circuito(), self.tiempo, edge_order=2)

    def corriente_Total(self):
        return self.corriente_R() + self.corriente_C()
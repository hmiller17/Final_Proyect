import math

class Bobina:
    def __init__(self, inductancia_nominal, resistencia_dc, material_nucleo):
        self.inductancia_nominal = inductancia_nominal
        self.resistencia_dc = resistencia_dc
        self.material_nucleo = material_nucleo

    def calcularReactancia(self, frecuencia):
        # Reactancia inductiva: X_L = 2 * pi * f * L
        return 2 * math.pi * frecuencia * self.inductancia_nominal

    def verificarSobrecorriente(self, corriente):
        corriente_maxima = 5  # Ejemplo de corriente máxima permitida
        if corriente > corriente_maxima:
            return True
        else:
            return False

    def calcularEnergiaAlmacenada(self, corriente):
        # Energía almacenada en una bobina: E = 0.5 * L * I^2
        return 0.5 * self.inductancia_nominal * (corriente ** 2)



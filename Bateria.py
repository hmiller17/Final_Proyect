class bateria:
    def __init__(self, voltaje, corriente):
        self.voltaje = voltaje
        self.corriente = corriente

    def calcularPotencia(self):
        # Potencia = Voltaje * Corriente
        return self.voltaje * self.corriente

    def verificarSobrecarga(self, potencia_maxima):
        # Verificar si la potencia actual excede la potencia máxima permitida
        potencia_actual = self.calcularPotencia()
        if potencia_actual > potencia_maxima:
            return True
        else:
            return False


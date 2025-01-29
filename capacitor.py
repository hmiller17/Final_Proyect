class Capacitor:
    def __init__(self, capacidad_nominal, tolerancia, potencia_maxima):
        self.capacidad_nominal = capacidad_nominal
        self.tolerancia = tolerancia
        self.potencia_maxima = potencia_maxima
        self.estado = "funcional"

    def verificarSobrevoltaje(self, voltaje):
        voltaje_maximo = 50  # Ejemplo de voltaje máximo
        if voltaje > voltaje_maximo:
            self.estado = "sobrevoltaje"
            return True
        else:
            return False

    def calcularEnergiaAlmacenada(self, voltaje):
        # Energía almacenada en un capacitor: E = 0.5 * C * V^2
        return 0.5 * self.capacidad_nominal * (voltaje ** 2)

    def verificarPerdidaCorriente(self, corriente):
        corriente_maxima = 1  # Ejemplo de corriente máxima
        if corriente > corriente_maxima:
            self.estado = "pérdida de corriente"
            return True
        else:
            return False

    def capacitorQuemado(self):
        self.estado = "quemado"
        print("El capacitor está quemado.")


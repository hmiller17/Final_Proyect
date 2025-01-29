class Resistor:
    def __init__(self, resistencia_nominal, tolerancia, coeficiente_temperatura):
        self.resistencia_nominal = resistencia_nominal
        self.tolerancia = tolerancia
        self.codigo_colores = []
        self.coeficiente_temperatura = coeficiente_temperatura
        self.estado = "funcional"

    def calcularPotenciaMaxima(self, voltaje, corriente):
        return voltaje * corriente

    def verificarSobrecarga(self, potencia_disipada):
        potencia_maxima = self.calcularPotenciaMaxima(10, 1)  # Ejemplo de valores
        if potencia_disipada > potencia_maxima:
            self.estado = "sobrecargado"
            return True
        else:
            return False

    def generarCodigoColores(self):
        # Aquí se simula un código de colores básico
        self.codigo_colores = ["Marrón", "Negro", "Rojo", "Dorado"]
        print("Código de colores generado:", self.codigo_colores)

    def calcularTemperaturaMaxima(self):
        # Este método debería calcular la temperatura máxima basada en el coeficiente de temperatura
        return 100 

    def calcularResistenciaMedida(self):
        # Este método debería calcular la resistencia medida basada en la resistencia nominal y la tolerancia
        return self.resistencia_nominal * (1 + self.tolerancia / 100)

    def resistenciaQuemada(self):
        self.estado = "quemada"
        print("La resistencia está quemada.")


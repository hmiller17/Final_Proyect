from .componente import Componente

class Capacitor(Componente):
    def __init__(self, valor, unidad="F"):
        if unidad != "F":
            raise ValueError("Los capacitores deben estar en faradios (F)")
        super().__init__(valor, unidad)
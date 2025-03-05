from .componente import Componente
class Resistencia(Componente):
    def __init__(self, valor, unidad="ohm"):
        if unidad != "ohm":
            raise ValueError("Las resistencias deben estar en ohmios (ohm)")
        super().__init__(valor, unidad)
from .componente import Componente
class FuenteDC(Componente):
    def __init__(self, valor, unidad="V"):
        if unidad != "V":
            raise ValueError("Las fuentes de voltaje deben estar en voltios (V)")
        super().__init__(valor, unidad)
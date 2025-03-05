from .componente import Componente

class Inductor(Componente):
    def __init__(self, valor, unidad="H"):
        if unidad != "H":
            raise ValueError("Los inductores deben estar en henrios (H)")
        super().__init__(valor, unidad)
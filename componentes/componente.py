class Componente:
    def __init__(self, valor: float, unidad: str):
        if valor <= 0:
            raise ValueError(f"El valor del componente {self.__class__.__name__} debe ser mayor que cero")
        self._valor = float(valor)
        self._unidad = str(unidad)

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor <= 0:
            raise ValueError("El valor del componente debe ser mayor que cero")
        self._valor = float(nuevo_valor)

    @property
    def unidad(self):
        return self._unidad

    @unidad.setter
    def unidad(self, nueva_unidad):
        if not isinstance(nueva_unidad, str):
            raise TypeError("La unidad debe ser un string")
        self._unidad = nueva_unidad
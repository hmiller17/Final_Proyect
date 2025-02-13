'''SUPER CLASE-COMPONENTE'''
class Componente():
    def __init__(self, valor, unidad):
        self.valor = float(valor)
        self.unidad = str(unidad)

    def obtener_valor(self) -> float:
        return self.valor
    
    def obtener_unidad(self) -> str:
        return self.unidad

    #Para imprimir el valor del componente en la prueba
    def __str__(self):
        return f"{self.valor} {self.unidad}."

#region (Prueba SUPER-CLASE-COMPONENTE)
# prueba_componente = Componente(5.1, "Unidades")
# print(f"El valor del componente es {prueba_componente}")
#endregion

'''Subclases-Componentes'''
class Fuente_DC(Componente):
    def __init__(self, valor, unidad):
        super().__init__(valor, unidad)

class Resistencia(Componente):
    def __init__(self, valor, unidad):
        super().__init__(valor, unidad)

class Capacitor(Componente):
    def __init__(self, valor, unidad):
        super().__init__(valor, unidad)

class Inductor(Componente):
    def __init__(self, valor, unidad):
        super().__init__(valor, unidad)

#region (Prueba Subclases-Componentes)
# prueba_FuenteDC = Fuente_DC(3,"Volts")
# prueba_Resistencia = Resistencia(5.1, "Ohms")
# prueba_Capacitor = Capacitor(10, "Faradios")
# prueba_Inductor = Inductor(5, "Henrios")

# print(f"El valor de la fuente DC es {prueba_FuenteDC}")
# print(f"El valor de la resistencia es {prueba_Resistencia}")
# print(f"El valor del capacitor es {prueba_Capacitor}")
# print(f"El valor del inductor es {prueba_Inductor}")
#endregion

'''SUPER CLASE CIRCUITO'''
class Circuito():
    def __init__ (self, fuente: Fuente_DC, resistencias: list[Resistencia]):
        self.fuenteDC = fuente
        self.resistencias = resistencias

    def Calcular_Corriente(self):
        resistencia_total = sum([resistencia.obtener_valor() for resistencia in self.resistencias])
        return self.fuenteDC.obtener_valor() / resistencia_total 
    
    def Calcular_Potencia(self):
        return self.fuenteDC.obtener_valor() * self.Calcular_Corriente()
    

#region (Prueba SUPER-CLASES)
# resistores = [Resistencia(3, "Ohms")]
# valor_fuente = Fuente_DC(9, "Volts")
# prueba_corriente = Circuito(valor_fuente,resistores).Calcular_Corriente()
# print(f"La corriente del circuito es {prueba_corriente} A.")
# prueba_potencia = Circuito(valor_fuente,resistores).Calcular_Potencia()
# print(f"La potencia del circuito es {prueba_potencia} W.")
#endregion


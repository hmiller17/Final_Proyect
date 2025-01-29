## **Simulador de circuitos**

Para este proyecto vamos a hacer un simulador de tres tipos de señales, las cuales serian señales RC, RL Y RLC. las cuales estan compuestas por resistencias (R), capacitores (C) e inductores (L), configurados en serie o en paralelo


## **Diagrama de Clases**

El diseño orientado a objetos se representa mediante el siguiente diagrama de clases:

```mermaid
classDiagram
direction TB

class Capacitor {
    + float capacidad_nominal
    + float tolerancia
    + float potencia_maxima
    + string estado
    + verificarSobrevoltaje(voltaje : float) bool
    + calcularEnergiaAlmacenada(voltaje : float) float
    + verificarPerdidaCorriente(corriente : float) bool
    + capacitorQuemado()
}

class Bobina {
    + float inductancia_nominal
    + float resistencia_dc
    + string material_nucleo
    + calcularReactancia(frecuencia : float) float
    + verificarSobrecorriente(corriente : float) bool
    + calcularEnergiaAlmacenada(corriente : float) float
    + calcularCampoElectrico()
}

class Resistor {
    + float resistencia_nominal
    + float tolerancia
    + list codigo_colores
    + float coeficiente_temperatura
    + string estado
    + calcularPotenciaMaxima(voltaje : float, corriente : float) float
    + verificarSobrecarga(potencia_disipada : float) bool
    + generarCodigoColores() void
    + calcularTemperaturaMaxima()
    + calcularResistenciaMedida()
    + resistenciaQuemada()
}

class FuenteEnergia {
    + float voltage
    + float corriente
}

class CircuitoRC {
    + Resistor resistor
    + Capacitor capacitor
    + string configuracion
    + calcularImpedancia(frecuencia : float) float
    + calcularCorriente(fuente : FuenteEnergia, frecuencia : float) float
    + calcularTensionComponentes(fuente : FuenteEnergia, frecuencia : float) tuple
    + graficar(frecuencia_range : list, fuente : FuenteEnergia) void
}

class CircuitoRL {
    + Resistor resistor
    + Bobina bobina
    + string configuracion
    + calcularImpedancia(frecuencia : float) float
    + calcularCorriente(fuente : FuenteEnergia, frecuencia : float) float
    + calcularTensionComponentes(fuente : FuenteEnergia, frecuencia : float) tuple
    + graficar(frecuencia_range : list, fuente : FuenteEnergia) void
}

class CircuitoRLC {
    + Resistor resistor
    + Capacitor capacitor
    + Bobina bobina
    + string configuracion
    + calcularImpedancia(frecuencia : float) float
    + calcularCorriente(fuente : FuenteEnergia, frecuencia : float) float
    + calcularFrecuenciaResonancia() float
    + calcularTensionComponentes(fuente : FuenteEnergia, frecuencia : float) tuple
    + graficar(frecuencia_range : list, fuente : FuenteEnergia) void
}

CircuitoRC *-- Resistor
CircuitoRC *-- Capacitor
CircuitoRL *-- Resistor
CircuitoRL *-- Bobina
CircuitoRLC *-- Resistor
CircuitoRLC *-- Capacitor
CircuitoRLC *-- Bobina

CircuitoRC o-- FuenteEnergia
CircuitoRL o-- FuenteEnergia
CircuitoRLC o-- FuenteEnergia

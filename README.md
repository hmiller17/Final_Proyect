# **Simulador de circuitos**
## **Integrantes**
***Juan Manuel Toro Rojas
    Hector Miller Patiño Avellaneda
    Miguel Angel Tovar Rincón***

##  **proyecto**

**Parte 1: Menú de Navegación (Imagen 1)**
En esta parte, el usuario verá un menú principal que le permitirá seleccionar entre los tres tipos de señales: RC, RL y RLC. Este menú será la primera interfaz que el usuario encuentre al iniciar la aplicación.

** Características del Menú**
+Señal RC: Simulación de un circuito RC (Resistencia y Capacitor).

+Señal RL: Simulación de un circuito RL (Resistencia e Inductor).

+Señal RLC: Simulación de un circuito RLC (Resistencia, Inductor y Capacitor).




## **Imagenes de la GUI (Interfaz grafica)**
![Imagen de WhatsApp 2025-01-27 a las 12 52 21_f5a31c5d](https://github.com/user-attachments/assets/61484a29-ebbb-46c7-b570-08206f9a165d)
**Imagen 1**

![Imagen de WhatsApp 2025-01-27 a las 12 52 33_0eb51c0c](https://github.com/user-attachments/assets/226167c1-2d6b-482b-88c0-8ebb5ce29fa8)
**Imagen 2**

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

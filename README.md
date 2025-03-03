# **Simulador de circuitos**

## 📖 Índice:
+ [Integrantes](#integrantes)
+ [Alternativa](#alternativa-4)
+ [Solución Preliminar](#solución-preliminar)
    + [Interfaz de Usuario](#parte-1-interfaz-de-usuario-gui)
        + [Frame 1: Menú](#frame-1-menú)
        + [Frame 2: Simulador](#frame-2-simulador)
        + [Diagrama de clases](#diagrama-de-clases-de-la-interfaz)
    + [Lógica del simulador](#parte-2-lógica-para-la-simulación-de-los-circuitos)
        + [Clases (Componentes)](#clases-componentes)
        + [Clases (Cirrcuitos)](#clases-circuitos)
        + [Diagrama de clases](#diagrama-de-clases)
+ [Inspiración para la interfaz](#inspiración-para-la-interfaz)

## **Integrantes**
+ Juan Manuel Toro Rojas
+ Héctor Miller Patiño Avellaneda
+ Miguel Ángel Tovar Rincón

## **Alternativa 4**
Desarrollar una aplicación en Python que permita simular circuitos RC, RL y RLC simples. Condiciones:

+ Código original.
+ Uso de herramientas vistas en el curso (CLASES) - Los componentes deben aplicar el enfoque de POO (por ejemplo, una resistencia debe tener atributos como resistividad, potencia, etc.).
+ Se deben poder configurar los componentes en serie y en paralelo.
+ Se deben trabajar con fuentes de tensión en DC únicamente.
+ El resultado de la simulación debe ser una representación gráfica de la tensión/corriente en cada uno de los componentes.
+ Se pueden utilizar módulos externos para la solución de los componentes numéricos.

**Características extra:**
+ Hacer análisis en el dominio AC.

## **Solución Preliminar**
Para desarrollar este simulador de circuitos simples **RC, RL y RLC**, es necesario tener en cuenta las partes que se deben desarrollar. Para esta alternativa se requiere:
+ Interfaz de usuario (GUI).
+ Lógica para la simulación de los circuitos.

### **Parte 1: Interfaz de Usuario (GUI)**
***
#### **Frame 1: Menú**
En esta parte, se presenta un mensaje de bienvenida y el usuario verá un menú principal que le permitirá seleccionar entre los tres tipos de circuitos que se pueden simular: RC, RL y RLC. Este menú será el primer frame que el usuario encontrará al iniciar la aplicación.

![Imagen de WhatsApp 2025-01-27 a las 12 52 21_f5a31c5d](https://github.com/user-attachments/assets/61484a29-ebbb-46c7-b570-08206f9a165d)

**Características del Menú:**
+ Señal RC: Simulación de un circuito RC (Resistencia y Capacitor).
+ Señal RL: Simulación de un circuito RL (Resistencia e Inductor).
+ Señal RLC: Simulación de un circuito RLC (Resistencia, Inductor y Capacitor).

#### **Frame 2: Simulador** 
Este frame será una interfaz sencilla en la que el usuario podrá observar el circuito seleccionado en el menú anterior. Adicionalmente, en un contenedor ubicado en la parte derecha de la pantalla, el usuario podrá ingresar los parámetros de cada componente del circuito en cajas de texto. Los valores que se pueden ingresar son:
+ Resistencia.
+ Capacitor.
+ Inductor.
+ Fuente de energía.

![Imagen de WhatsApp 2025-01-27 a las 12 52 33_0eb51c0c](https://github.com/user-attachments/assets/226167c1-2d6b-482b-88c0-8ebb5ce29fa8)


Finalmente, el usuario podrá observar los datos del circuito en forma de gráficos en un contenedor ubicado en la parte inferior de la ventana. También habrá una opción para volver al menú principal y la opción de realizar la simulación con los mismos componentes en un circuito en serie y paralelo.

### **Diagrama de clases de la interfaz**
A continuación, se presenta el diagrama de clases de la GUI:

```mermaid
classDiagram
    class VentanaPrincipal {
        +abrirVentana()
        +cerrarVentana()
        +ajustarTamano()
    }

    class Boton {
        +texto: String
        +clic()
    }

    class VentanaCircuito {
        +abrirVentana()
        +cerrarVentana()
        +ajustarTamano()
        +mostrarCircuito(tipo: String)
        +volverMenu()
    }

    class Contenedor {
        +mostrarContenido()
    }

    class ConfiguracionParametros {
        +bateria: Bateria
        +resistencia: Resistencia
        +capacitancia: Capacitor
        +inductancia: Bobina
        +modificarParametro()
    }

    class EstadisticasSimulacion {
        +mostrarGraficas()
        +mostrarDatos()
    }
    VentanaPrincipal --> Boton : contiene
    VentanaPrincipal --> VentanaCircuito : genera
    VentanaCircuito --> Boton : contiene
    VentanaCircuito --> Contenedor : contiene
    Contenedor --> ConfiguracionParametros : muestra
    Contenedor --> EstadisticasSimulacion : muestra
```

**Class VentanaPrincipal:**
Es la ventana inicial del simulador, donde el usuario puede seleccionar el tipo de circuito (RC, RL o RLC). Tiene métodos para abrir, cerrar y ajustar el tamaño.

**Class VentanaCircuito:**
Se genera cuando el usuario selecciona un tipo de circuito. Contiene métodos para abrir, cerrar, ajustar el tamaño, mostrar el circuito y volver al menú principal.

**Class Boton:**
Representa los botones de la interfaz. Contiene un texto y un método clic() para activar una acción.

**Class Contenedor:**
Se encarga de mostrar los diferentes elementos en la interfaz.

**Class ConfiguracionParametros:**
Contiene los valores de los componentes del circuito, como batería, resistencia, capacitancia e inductancia. Permite modificar estos valores.

**Class EstadisticasSimulacion:**
Muestra las gráficas y datos generados por la simulación del circuito.

### **Parte 2: Lógica para la simulación de los circuitos**
***
Para el desarrollo de la lógica del simulador, hay que tener en cuenta los factores que pueden afectar los valores de la simulación, tales como los parámetros de cada componente y si el circuito es en serie o en paralelo. Un buen primer paso es definir **qué objetos existirán** en este simulador, posteriormente **qué datos deben ser ingresados** y **qué datos pueden ser generados**, para finalmente desarrollar una **salida de datos en forma de diagramas y estadísticas**.

#### **Clases (Componentes):**
+ *Componente*: Es el elemento base para los diferentes componentes del circuito, que contiene el valor numérico, la unidad de medida y devuelve el valor con su respectiva unidad.
    + Fuente DC: Maneja el voltaje.
    + Resistencia: Devuelve el valor en ohmios.
    + Capacitor: Devuelve la capacitancia en faradios.
    + Bobina: Devuelve el valor en henrios de la inductancia.

#### **Clases (Circuitos):**
+ *Circuito*: Representa un circuito eléctrico genérico que puede contener una fuente de corriente continua (DC) y una colección de resistencias. Es la base para los demás tipos de circuitos a simular, este va a calcular la corriente, el voltaje y tambien va a mostrar los datos y las gráficas, esta función sera heredada para cada tipo de circuito.
    + Circuito en Serie: Se calculan la resistencia y la corriente; las resistencias se suman y la corriente es la misma en todos los componentes.
    + Circuito en Paralelo: Se calcula la resistencia y la corriente; la corriente se divide entre las ramas, pero el voltaje es el mismo para todas.
    + Circuito RC: Contiene una resistencia y un capacitor; calcula la carga y el tiempo de carga del capacitor.
    + Circuito RL: Contiene una resistencia y una bobina; calcula la corriente inducida y el tiempo de respuesta.
    + Circuito RLC: Contiene una resistencia, una bobina y un capacitor; calcula los mismos parámetros de las clases anteriores y la frecuencia de resonancia del circuito.
  
#### **Clases (logica de calculo):**
### **Fórmulas Matemáticas**
Las fórmulas utilizadas en las simulaciones de los circuitos son las siguientes:

1. **Circuito RC (Serie):**
   - Voltaje en la resistencia:

     ![image](https://github.com/user-attachments/assets/ac0674c0-bcfa-471a-84ef-231c26db9c0d)

   - Voltaje en el capacitor:

     ![image](https://github.com/user-attachments/assets/fb67130d-eda4-4794-abb8-6480e19c7d92)
     
   - Corriente en el circuito:

     ![image](https://github.com/user-attachments/assets/9e9060cd-4be8-473f-b6b4-2eca4c2fb3db)


2. **Circuito RL (Serie):**
   - Corriente en el circuito:

     ![image](https://github.com/user-attachments/assets/8b3b6c57-f114-40be-b78f-e9e320d545e6)

   - Voltaje en la resistencia:

     ![image](https://github.com/user-attachments/assets/cb481f2d-dab2-4dc6-a610-b2f05414d172)

   - Voltaje en el inductor:

     ![image](https://github.com/user-attachments/assets/42396330-c581-4f08-aef8-7ee7e09385a2)


3. **Circuito RLC (Serie):**
   - Corriente en el circuito:

     ![image](https://github.com/user-attachments/assets/ae1be8fe-6aa8-4456-9ac2-3bcd1f57d33b)

   - Voltaje en la resistencia:

     ![image](https://github.com/user-attachments/assets/cbd138f7-9775-4d6a-bf58-45ee52671e89)

   - Voltaje en el inductor:

     ![image](https://github.com/user-attachments/assets/472076b9-3688-45e1-b9aa-7d2fae09518f)

   - Voltaje en el capacitor:
   
     ![image](https://github.com/user-attachments/assets/cb0cd2ad-4d75-4425-aad1-7d554599f809)


4. **Circuito RC (Paralelo):**
   - Voltaje en el circuito:

     ![image](https://github.com/user-attachments/assets/302c7ba9-6fb2-419c-bb13-70e5bcb2c130)

   - Corriente en la resistencia:

     ![image](https://github.com/user-attachments/assets/87788625-1f0a-4488-ab15-b17ecad02cb4)

   - Corriente en el capacitor:

     ![image](https://github.com/user-attachments/assets/9220f2ae-0b37-4235-b74b-6044b795c326)

   - Corriente total:
  
     ![image](https://github.com/user-attachments/assets/84704f58-99ed-4138-aa9a-1849b5698120)


5. **Circuito RL (Paralelo):**
   - Voltaje en el circuito:

     ![image](https://github.com/user-attachments/assets/44236adb-be49-44fd-9de1-1ecfab2fefe4)

   - Corriente en la resistencia:
  
     ![image](https://github.com/user-attachments/assets/fbe1e169-c9c3-4cea-8815-1a890b36a9da)

   - Corriente en el inductor:

     ![image](https://github.com/user-attachments/assets/63bfe76a-1e2b-4c0a-9876-30daf67bcd88)

   - Corriente total:

     ![image](https://github.com/user-attachments/assets/6579e61d-80b7-4ad9-8bfc-153e66b3e43f)


6. **Circuito RLC (Paralelo):**
   - Voltaje en el circuito:

    ![image](https://github.com/user-attachments/assets/9fc1721a-2c05-4d03-a062-5820e6cbc218)

   - Corriente en la resistencia:

     ![image](https://github.com/user-attachments/assets/7cd70d12-b437-4efb-b715-e80b27c4ec0b)

   - Corriente en el inductor:

     ![image](https://github.com/user-attachments/assets/b9939b67-283a-4322-a560-1c79fe0acefa)

   - Corriente en el capacitor:

     ![image](https://github.com/user-attachments/assets/57d0372a-7f25-4a5a-b4ca-e3374b328d85)

   - Corriente total:

     ![image](https://github.com/user-attachments/assets/381f2157-1142-42ad-8649-ed1cc3d6127e)


---

### **Aspectos de POO**
El código utiliza varios conceptos de Programación Orientada a Objetos (POO) para estructurar la lógica del simulador:

1. **Herencia:**
   - Las clases `FuenteDC`, `Resistencia`, `Capacitor` e `Inductor` heredan de la clase base `Componente`. Esto permite reutilizar código y definir comportamientos comunes para todos los componentes.
   - Las clases `CircuitoRC`, `CircuitoRL`, `CircuitoRLC`, `CircuitoRC_Paralelo`, `CircuitoRL_Paralelo` y `CircuitoRLC_Paralelo` heredan de la clase base `Circuito`. Esto permite definir comportamientos específicos para cada tipo de circuito.

2. **Encapsulamiento:**
   - Los atributos de las clases están encapsulados mediante el uso de propiedades (`@property`). Esto permite controlar el acceso y la modificación de los valores de los componentes, asegurando que no se asignen valores inválidos.

3. **Polimorfismo:**
   - Cada tipo de circuito implementa sus propios métodos para calcular voltajes y corrientes, pero todos comparten una interfaz común gracias a la herencia. Esto permite que la simulación se realice de manera uniforme, independientemente del tipo de circuito.

4. **Abstracción:**
   - La clase `Componente` es una abstracción que define los atributos y métodos comunes a todos los componentes del circuito. Las clases derivadas implementan detalles específicos.

---

### **Casos de Uso**
1. **Simulación de un circuito RC en serie:**
   - El usuario selecciona el circuito RC en el menú principal.
   - Ingresa los valores de la resistencia, el capacitor y la fuente de voltaje.
   - El simulador calcula y muestra las gráficas de voltaje en la resistencia, voltaje en el capacitor y corriente en el circuito.

2. **Simulación de un circuito RL en paralelo:**
   - El usuario selecciona el circuito RL en el menú principal.
   - Ingresa los valores de la resistencia, el inductor y la fuente de voltaje.
   - El simulador calcula y muestra las gráficas de voltaje en el circuito, corriente en la resistencia, corriente en el inductor y corriente total.

3. **Guardar y cargar configuraciones:**
   - El usuario puede guardar los valores de los componentes en un archivo JSON.
   - Posteriormente, puede cargar estos valores para realizar una simulación sin necesidad de ingresar los datos nuevamente.

4. **Cambiar entre serie y paralelo:**
   - El usuario puede cambiar la configuración del circuito entre serie y paralelo para observar cómo afecta el comportamiento del circuito.


#### **Diagrama de Clases**
El diagrama de las clases anteriores se representa de esta manera:

```mermaid
classDiagram
direction TB

    class Circuito {
        +fuente: FuenteDC
        +resistencias: list
        +calcularCorriente() : float
        +calcularVoltaje() : float
        +mostrarDatos()
        +mostrarGraficas()
    }

    class CircuitoSerie {
        +calcular_resistencia_eq()
    }

    class CircuitoParalelo {
        +calcular_resistencia_eq()
    }

    class CircuitoRC {
        +capacitores: list
        +calcularCarga() : float
        +calcularTiempoCarga() : float
        +mostrarDatos()
        +mostrarGraficas()
    }

    class CircuitoRL {
        +inductores: list
        +calcularCorrienteInducida() : float
        +calcularTiempoRespuesta() : float
        +mostrarDatos()
        +mostrarGraficas()
    }

    class CircuitoRLC {
        +capacitores: list
        +inductores: list
        +calcularFrecuenciaResonancia() : float
        +mostrarDatos()
        +mostrarGraficas()
    }

    class Componente {
        +valor: float
        +unidad: String
        +obtener_valor() : float
    }

    class Resistencia {
        +valor: float
        +obtener_valor()
    }

    class Capacitor {
        +valor: float
        +obtener_valor()
    }

    class Bobina {
        +valor: float
        +obtener_valor()
    }

    class FuenteDC {
        +voltaje: float
        +obtener_valor()
    }

    %% Herencia de Circuito
    Circuito <|-- CircuitoSerie
    Circuito <|-- CircuitoParalelo
    CircuitoRC --|> Circuito
    CircuitoRL --|> Circuito
    CircuitoRLC --|> Circuito

    %% Relación de Circuitos específicos con sus componentes
    CircuitoRC --> Capacitor
    CircuitoRL --> Bobina
    CircuitoRLC --> Capacitor
    CircuitoRLC --> Bobina

    %% Relación de Circuito con sus componentes
    Circuito --> FuenteDC
    Circuito --> Resistencia

    %% Herencia de Componente
    Componente <|-- Resistencia
    Componente <|-- Capacitor
    Componente <|-- Bobina
    Componente <|-- FuenteDC
```



## **Inspiración para la interfaz**
Un apoyo para la realización de este proyecto es una calculadora desarrollada el semestre pasado, en la que adquirimos conocimientos para programar y crear una interfaz gráfica y proyectar datos por medio de gráficos. Dicha calculadora se encuentra en el siguiente repositorio de GitHub:
+ [Calculadora en GitHub](https://github.com/Mike-arch-code/Calculadora)

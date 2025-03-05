import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2Tk
from PIL import Image, ImageTk
import os
from componentes.fuente_dc import FuenteDC
from componentes.resistencia import Resistencia
from componentes.capacitor import Capacitor
from componentes.inductor import Inductor
from circuitos.circuito_rc import CircuitoRC
from circuitos.circuito_rl import CircuitoRL
from circuitos.circuito_rlc import CircuitoRLC
from circuitos.circuito_rc_paralelo import CircuitoRC_Paralelo
from circuitos.circuito_rl_paralelo import CircuitoRL_Paralelo
from circuitos.circuito_rlc_paralelo import CircuitoRLC_Paralelo
from clases_interfaz.ventana_principal import VentanaPrincipal

class VentanaCircuito:
    def __init__(self, root, tipo, image_path):
        self.root = root
        self.root.title(f"Simulación {tipo}")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        self.image_path = image_path
        self.tipo_circuito = tipo
        self.parametros = {}
        self.configuracion = "serie"

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=0, minsize=50)
        self.root.rowconfigure(1, weight=1, minsize=150)
        self.root.rowconfigure(2, weight=1, minsize=50)

        frame_botones = tk.Frame(self.root)
        frame_botones.grid(row=0, column=0, sticky="nsew")

        frame_botones.columnconfigure([0, 1, 2, 3, 4, 5], weight=1)
        frame_botones.rowconfigure(0, weight=1)

        tk.Button(frame_botones, text="Serie", command=self.serie).grid(row=0, column=0, sticky="nsew")
        tk.Button(frame_botones, text="Paralelo", command=self.paralelo).grid(row=0, column=1, sticky="nsew")
        tk.Button(frame_botones, text="Simular", command=self.simular).grid(row=0, column=2, sticky="nsew")
        tk.Button(frame_botones, text="Guardar", command=self.guardar_circuito).grid(row=0, column=3, sticky="nsew")
        tk.Button(frame_botones, text="Cargar", command=self.cargar_circuito).grid(row=0, column=4, sticky="nsew")
        tk.Button(frame_botones, text="Menú", command=self.volverMenu).grid(row=0, column=5, sticky="nsew")

        self.frame_imagen_circuito = tk.Frame(self.root, bd=2, relief="solid", bg="lightgreen")
        self.frame_imagen_circuito.grid(row=1, column=0, sticky="nsew")

        self.frame_parametros = tk.Frame(self.root, bd=2, relief="solid", bg="lightblue")
        self.frame_parametros.grid(row=2, column=0, sticky="nsew")

        self.crear_campos_parametros()
        self.cargar_imagen()

    def crear_campos_parametros(self):
        campos = {"resistencia": "Resistencia (Ω)", "voltaje": "Voltaje (V)"}
        if self.tipo_circuito in ["RC", "RLC"]:
            campos["capacitor"] = "Capacitor (F)"
        if self.tipo_circuito in ["RL", "RLC"]:
            campos["inductor"] = "Inductor (H)"

        for i, (clave, etiqueta) in enumerate(campos.items(), start=0):
            ttk.Label(self.frame_parametros, text=etiqueta, background="lightblue", font=("Arial", 12)).grid(row=i, column=0, padx=10, pady=10, sticky="ew")
            self.parametros[clave] = ttk.Entry(self.frame_parametros, width=15, font=("Arial", 12))
            self.parametros[clave].grid(row=i, column=1, padx=10, pady=10, sticky="ew")

        self.frame_parametros.columnconfigure(0, weight=1)
        self.frame_parametros.columnconfigure(1, weight=1)

    def cargar_imagen(self):
        try:
            imagen = Image.open(self.image_path)
            width, height = 400, 200
            imagen = imagen.resize((width, height))
            self.imagen_tk = ImageTk.PhotoImage(imagen)
            label_imagen = tk.Label(self.frame_imagen_circuito, image=self.imagen_tk)
            label_imagen.place(relwidth=1, relheight=1)
        except FileNotFoundError:
            error_label = tk.Label(self.frame_imagen_circuito, text="Imagen no encontrada", fg="red", font=("Arial", 14))
            error_label.pack(expand=True)
        except Exception as e:
            error_label = tk.Label(self.frame_imagen_circuito, text=f"Error: {e}", fg="red", font=("Arial", 14))
            error_label.pack(expand=True)

    def obtener_valores(self):
        valores = {}
        for clave, entry in self.parametros.items():
            try:
                valores[clave] = float(entry.get())
            except ValueError:
                messagebox.showerror("Error", f"Valor inválido para {clave}")
                return None
        return valores

    def simular(self):
        valores = self.obtener_valores()
        if valores is None:
            return

        tiempo = np.linspace(0, 0.1, 1000)
        if self.tipo_circuito == "RC":
            if self.configuracion == "serie":
                circuito = CircuitoRC(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Capacitor(valores["capacitor"]))
            else:
                circuito = CircuitoRC_Paralelo(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Capacitor(valores["capacitor"]))
        elif self.tipo_circuito == "RL":
            if self.configuracion == "serie":
                circuito = CircuitoRL(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Inductor(valores["inductor"]))
            else:
                circuito = CircuitoRL_Paralelo(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Inductor(valores["inductor"]))
        elif self.tipo_circuito == "RLC":
            if self.configuracion == "serie":
                circuito = CircuitoRLC(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Inductor(valores["inductor"]), Capacitor(valores["capacitor"]))
            else:
                circuito = CircuitoRLC_Paralelo(FuenteDC(valores["voltaje"]), Resistencia(valores["resistencia"]), Inductor(valores["inductor"]), Capacitor(valores["capacitor"]))

        self.mostrar_graficas(circuito, tiempo)

    def mostrar_graficas(self, circuito, tiempo):
        ventana_graficas = tk.Toplevel(self.root)
        ventana_graficas.title("Gráficas del Circuito")
        ventana_graficas.geometry("800x600")

        # Crear la figura y los ejes
        fig, axs = plt.subplots(2, 1, figsize=(8, 6))
        
        # Graficar los voltajes
        if self.configuracion == "serie":
            axs[0].plot(tiempo, circuito.voltaje_R(), label="Voltaje en R")
            if hasattr(circuito, 'voltaje_C'):
                axs[0].plot(tiempo, circuito.voltaje_C(), label="Voltaje en C")
            if hasattr(circuito, 'voltaje_L'):
                axs[0].plot(tiempo, circuito.voltaje_L(), label="Voltaje en L")
        else:
            # En paralelo, el voltaje es el mismo en todos los componentes
            axs[0].plot(tiempo, np.full_like(tiempo, circuito.fuente.valor), label="Voltaje en R, L, C")
        
        axs[0].set_title("Voltajes")
        axs[0].legend()
        axs[0].grid()

        # Graficar la corriente
        if self.configuracion == "serie":
            if hasattr(circuito, 'corriente_Circuito'):
                axs[1].plot(tiempo, circuito.corriente_Circuito(), label="Corriente")
        else:
            # En paralelo, graficar las corrientes individuales
            if hasattr(circuito, 'corriente_R'):
                axs[1].plot(tiempo, circuito.corriente_R(), label="Corriente en R")
            if hasattr(circuito, 'corriente_C'):
                axs[1].plot(tiempo, circuito.corriente_C(), label="Corriente en C")
            if hasattr(circuito, 'corriente_L'):
                axs[1].plot(tiempo, circuito.corriente_L(), label="Corriente en L")
            if hasattr(circuito, 'corriente_Total'):
                axs[1].plot(tiempo, circuito.corriente_Total(), label="Corriente Total", linestyle="--")
        
        axs[1].set_title("Corriente")
        axs[1].legend()
        axs[1].grid()

        # Crear el canvas para la figura
        canvas = FigureCanvasTkAgg(fig, master=ventana_graficas)
        canvas.draw()

        # Crear el toolbar y agregarlo a la ventana
        toolbar = NavigationToolbar2Tk(canvas, ventana_graficas)
        toolbar.update()

        # Empaquetar el canvas y el toolbar en la ventana
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
        toolbar.pack(side=tk.BOTTOM, fill=tk.X)

    def serie(self):
        self.configuracion = "serie"
        if self.tipo_circuito == "RC":
            image_file = "circuito_RC.jpg"  # Imagen para RC en serie
        elif self.tipo_circuito == "RL":
            image_file = "circuito_RL.jpg"  # Imagen para RL en serie
        else:
            image_file = "circuito_RLC.jpg"  # Imagen para RLC en serie

        # Actualizar la ruta de la imagen
        self.image_path = os.path.join("assets", image_file)
        self.cargar_imagen()  # Cargar y mostrar la nueva imagen
        print("Configuración en Serie:", self.tipo_circuito, self.configuracion)

    def paralelo(self):
        self.configuracion = "paralelo"
        if self.tipo_circuito == "RC":
            image_file = "circuito_RC_PARALELO.jpg"  # Imagen para RC en paralelo
        elif self.tipo_circuito == "RL":
            image_file = "circuito_RL_PARALELO.jpg"  # Imagen para RL en paralelo
        else:
            image_file = "circuito_RLC_PARALELO.jpg"  # Imagen para RLC en paralelo

        # Actualizar la ruta de la imagen
        self.image_path = os.path.join("assets", image_file)
        self.cargar_imagen()  # Cargar y mostrar la nueva imagen
        print("Configuración en Paralelo:", self.tipo_circuito, self.configuracion)

    def guardar_circuito(self):
        valores = self.obtener_valores()
        if valores is None:
            return

        nombre_archivo = filedialog.asksaveasfilename(defaultextension=".json", filetypes=[("JSON files", "*.json")])
        if nombre_archivo:
            with open(nombre_archivo, "w") as archivo:
                json.dump(valores, archivo)
            messagebox.showinfo("Guardado", "Circuito guardado correctamente.")

    def cargar_circuito(self):
        nombre_archivo = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if nombre_archivo:
            with open(nombre_archivo, "r") as archivo:
                valores = json.load(archivo)
            for clave, entry in self.parametros.items():
                if clave in valores:
                    entry.delete(0, tk.END)
                    entry.insert(0, str(valores[clave]))
            messagebox.showinfo("Cargado", "Circuito cargado correctamente.")

    def volverMenu(self):
        self.root.destroy()
        root_menu = tk.Tk()
        VentanaPrincipal(root_menu)
        root_menu.mainloop()
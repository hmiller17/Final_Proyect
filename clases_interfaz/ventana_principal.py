import tkinter as tk
import os

class VentanaPrincipal:
    def __init__(self, root):
        self.root = root
        self.root.title("Simulador de Circuitos")
        self.root.geometry("400x400")

        tk.Label(root, text="Seleccione el tipo de circuito:", font=("Arial", 12)).pack(pady=10)

        self.boton1 = tk.Button(self.root, text="Circuito RC", font=("Arial", 12),
                                command=lambda: self.abrir_simulador("RC", "circuito_RC.jpg"),
                                bg="lightblue", fg="black")
        self.boton1.pack(pady=10, fill=tk.BOTH, expand=True)

        self.boton2 = tk.Button(self.root, text="Circuito RL", font=("Arial", 12),
                                command=lambda: self.abrir_simulador("RL", "circuito_RL.jpg"),
                                bg="teal", fg="black")
        self.boton2.pack(pady=10, fill=tk.BOTH, expand=True)

        self.boton3 = tk.Button(self.root, text="Circuito RLC", font=("Arial", 12),
                                command=lambda: self.abrir_simulador("RLC", "circuito_RLC.jpg"),
                                bg="pink", fg="black")
        self.boton3.pack(pady=10, fill=tk.BOTH, expand=True)

        self.boton_borrar = tk.Button(self.root, text="Cerrar programa", font=("Arial", 12),
                                      command=self.finalizar_programa, bg="red", fg="white")
        self.boton_borrar.pack(pady=10, fill=tk.BOTH, expand=True)

    def abrir_simulador(self, tipo, image_file):
        self.root.destroy()
        root_circuito = tk.Tk()
        image_path = os.path.join("assets", image_file)
        from clases_interfaz.ventana_circuito import VentanaCircuito
        VentanaCircuito(root_circuito, tipo, image_path)
        root_circuito.mainloop()

    def finalizar_programa(self):
        self.root.destroy()
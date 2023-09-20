import os
import sys
import tkinter as tk
#from tkinter import *
#from tkinter import ttk
from tkinter import Tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

from subprocess import check_output
from typing import List, Any

from analizador import instruccion, ObtenerErrores, operar_recursivo

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Pantalla Principal Proyecto 1")

        self.lineaBarra = tk.Text(root, width=4, padx=4, takefocus=0, border=0, background='#f1d5dd', state='disabled')
        self.lineaBarra.pack(side=tk.LEFT, fill=tk.Y)

        self.textoblanco = ScrolledText(self.root, wrap=tk.WORD)
        self.textoblanco.pack(expand=True, fill='both')
        self.textoblanco.bind('<Key>', self.actualizar_linea)
        self.textoblanco.bind('<MouseWheel>', self.actualizar_linea)

        self.lineaActual = 1

        #Menu
        self.menubarra = tk.Menu(root)
        self.root.config(menu = self.menubarra)

        #Opciones en la barra de menu
        self.ArchivoMenu = tk.Menu(self.menubarra, tearoff = 0)

        #Menu de Archivo
        self.menubarra.add_cascade(label="ARCHIVO", menu=self.ArchivoMenu)
        self.ArchivoMenu.add_command(label="Abrir", command=self.abrirArchivo)
        self.ArchivoMenu.add_command(label="Guardar", command=self.Guardar)
        self.ArchivoMenu.add_command(label="Guardar como", command=self.GuardarComo)
        
        self.ArchivoMenu.add_separator()
        self.ArchivoMenu.add_command(label="Salir", command=self.root.quit)
        
        #Menu de Opciones
        self.menubarra.add_command(label="Analizar", command=self.analizar)
        self.menubarra.add_command(label="Errores", command=self.errores)
        self.menubarra.add_command(label="Reporte", command=self.grafica)

    def abrirArchivo(self):
        archivo = filedialog.askopenfilename(filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            with open(archivo, 'r') as file:
                x = file.read()
                self.textoblanco.delete(1.0, tk.END)
                self.textoblanco.insert(tk.END, x)
            self.actualizar_linea()
        self.data = self.textoblanco.get(1.0, tk.END)
        print(x)
    
    def Guardar(self):
        archivo = filedialog.asksaveasfile(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            x = self.textoblanco.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(x)
            messagebox.showinfo("Guardado", "Archivo guardado!")

    def GuardarComo(self):
        archivo = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos JSON", "*.JSON")])
        if archivo:
            x = self.textoblanco.get(1.0, tk.END)
            with open(archivo, 'w') as file:
                file.write(x)
            messagebox.showinfo("Guardado", "Archivo guardado!")
    
    def actualizar_linea(self, event=None):
        CuentaLinea = self.textoblanco.get(1.0, tk.END).count('\n')
        if CuentaLinea != self.lineaActual:
            self.lineaBarra.config (state=tk.NORMAL)
            self.lineaBarra.delete(1.0, tk.END)
            for linea in range(1, CuentaLinea + 1):
                self.lineaBarra.insert(tk.END, f'{linea}\n')
            self.lineaBarra.config(state=tk.DISABLED)
            self.lineaActual = CuentaLinea
    
    def analizar(self):
        try:
            instrucciones = instruccion(self.data)
            respuestaO = operar_recursivo()
            Resultados = ''
            Operacion = 1
            configuracion = 1
            salto = "\n"
            for respuesta in respuestaO:
                if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                    Resultados += str(f'Operacion {Operacion} --> {respuesta.tipo.operar(None)} = {respuesta.operar(None)}\n')
                    print(respuesta.operar(None))
                    Operacion += 1
            messagebox.showinfo("Documento Analizado", Resultados)
        except:
            messagebox.showinfo("Error", "No se ha ingresado ningun archivo")

    def errores(self):
        lista_errores = ObtenerErrores
        for errores in lista_errores:
            cont = 1
            er = errores.operar(cont)
            cont += 1
            print(er)

    def grafica(self):
        try:
            operar_recursivo().clear()
            instrucciones = instruccion(self.data)
            respuestaO = operar_recursivo()
            
            graf_contenido = "digraph G {\n\n"
            abrir = open("Operaciones.dot", "w", encoding="utf-8")
            graf_contenido += str(Graphviz(respuestaO))
            graf_contenido += '\n}'
            abrir.write(graf_contenido)
            abrir.close()
            
            print("--------------------------------------------------")
            print("             ** COMANDOS DE GRAPHVIZ **"           )
            print("")
            print(graf_contenido)
            print("")
            os.environ["PATH"] += os.pathsep + 'C:\Program Files\Graphviz\bin'
            #os.system('dot -Tpng bb.dot -o grafo_original.png')
            os.system('dot -Tpng Operaciones.dot -o Operaciones.png')

        except Exception as e:
            messagebox.showinfo("Se produjo un error: ", str(e))
            messagebox.showinfo("Mensaje", f"Error al generar el archivo de entrada, Verificar el archivo de entrada.")
        else:
            messagebox.showinfo("Mensaje", "Grafica generada con exito")
            respuestaO.clear()
            instrucciones.clear()

def Graphviz(respuestaO):
    Titulo = ""
    color = ""
    fuente = ""
    forma = ""

    try:
        print("------------------------------------------------")
        for respuesta in respuestaO:
            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                pass
            else:
                temporal = str(respuesta.texto.operar(None)).lower()
                print(respuesta.texto.operar(None))
                print(respuesta.ejecutarT())
                #Configuracion para el titulo
                if respuesta.ejecutarT() == "texto":
                    Titulo = str(respuesta.texto.operar(None))
                #Configuracion para el color de fondo
                if respuesta.ejecutarT() == "fondo" or respuesta.ejecutarT() == "color-fondo-nodo":
                    if temporal == ("amarillo" or "yellow"):
                        temporal = "yellow"
                        color = temporal
                    elif temporal == ("azul" or "blue"):
                        temporal = "blue"
                        color = temporal
                    elif temporal == ("rojo" or "red"):
                        temporal = "red"
                        color = temporal
                    elif temporal == ("verde" or "green"):
                        temporal = "green"
                        color = temporal
                    elif temporal == ("morado" or "purple"):
                        temporal = "purple"
                        color = temporal
                #Configuracion para el color de la fuente
                if respuesta.ejecutarT() == "fuente" or respuesta.ejecutarT() == "color-fuente-nodo":
                    if temporal == ("amarillo" or "yellow"):
                        temporal = "yellow"
                        fuente = temporal
                    elif temporal == ("azul" or "blue"):
                        temporal = "blue"
                        fuente = temporal
                    elif temporal == ("rojo" or "red"):
                        temporal = "red"
                        fuente = temporal
                    elif temporal == ("verde" or "green"):
                        temporal = "green"
                        fuente = temporal
                    elif temporal == ("morado" or "purple"):
                        temporal = "purple"
                        fuente = temporal
                    elif temporal == ("negro" or "black"):
                        temporal = "black"
                        fuente = temporal
                    elif temporal == ("blanco" or "white"):
                        temporal = "white"
                        fuente = temporal
                #Configuracion para la forma
                if respuesta.ejecutarT() == "forma" or respuesta.ejecutarT() == "forma-nodo":
                    if temporal == ("circulo" or "circle"):
                        temporal = "circle"
                        forma = temporal
                    elif temporal == ("cuadrado" or "square"):
                        temporal = "square"
                        forma = temporal
                    elif temporal == ("triangulo" or "triangle"):
                        temporal = "triangle"
                        forma = temporal
                    elif temporal == ("rectangulo" or "box"):
                        temporal = "box"
                        forma = temporal
                    elif temporal == ("elipse" or "ellipse"):
                        temporal = "ellipse"
                        forma = temporal
        temporal = ''
        ColumnumIzq = 0
        ColumnumDer = 0
        Columrespuesta = 0
        ColumTotal = 0

        text = ""
        text += f"\tnode [shape={forma}]\n"
        text += f"\tnodo0 [label = \"{Titulo}\"]\n"
        text += f"\tnodo0" + "[" + f"style =filled"+ f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"

        for respuesta in respuestaO:
            ColumnumIzq += 1
            ColumnumDer += 1
            Columrespuesta += 1
            ColumTotal += 1

            if isinstance(respuesta.operar(None), int) or isinstance(respuesta.operar(None), float) == True:
                text += f"\tnodoRespuesta{Columrespuesta}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoIzqu{ColumnumIzq}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoDere{ColumnumDer}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"
                text += f"\tnodoT{ColumTotal}" + "[" + f"style =filled" + f",fillcolor = {color}" + f", fontcolor = {fuente}" + "]\n"

                text += f"\tnodoRespuesta{Columrespuesta}" + f"[label = \"{str(respuesta.tipo.operar(None))}: " + "\"]\n"
                text += f"\tnodoIzqu{ColumnumIzq}" + "[label = \"Varlor1: " + f"{str(respuesta.vizq.operar(None))}" + "\"]\n"
                text += f"\tnodoDere{ColumnumDer}" + "[label = \"Valor2: " + f"{str(respuesta.vder.operar(None))}" + "\"]\n"

                text += f"\tnodoRespuesta{Columrespuesta} -> nodoIzqu{ColumnumIzq}\n"
                text += f"\tnodoRespuesta{Columrespuesta} -> nodoDere{ColumnumDer}\n"

                text += f"\tnodoT{ColumTotal}" + f"[label = \"{respuesta.operar(None)}" + "\"]\n"
                text += f"\tnodoT{ColumTotal} -> nodoRespuesta{Columrespuesta}\n"
            else:
                pass
        return text
    except Exception as e:
        messagebox.showinfo("Se produjo un error: ", str(e))
        messagebox.showinfo("Mensaje", "Ya me canseeeeee!!!!")


    """def pantalla1(self):
        self.Frame = Frame(height = 500, width = 800)
        self.Frame.configure(bg = "#cbcdcc")
        self.Frame.pack(padx = 25, pady = 25)
        self.Frame.mainloop()"""    

if __name__ == "__main__":
    root = tk.Tk()
    app = Interfaz(root)
    root.mainloop()
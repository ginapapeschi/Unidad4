from tkinter import *
from tkinter import messagebox              # Sirve para mandar el mensaje de "perdiste" al usuario.
import random                               # Porque son aleatorios los botones que se apretarán.
import time                                 # Para las pausas entre cada ronda.
import winsound                             # Para ejecutar sonidos al apretar los botones.

class SimonDice:
    
    def __init__(self):
        self.ventana = Tk()               # Se crea una ventana y se le asigna un nuevo constructor de Tk para crear el nuevo frame.
        self.secuencia = []               # Lista donde se almacenará el ORDEN de los colores conforme se fueron encendiendo.
        self.marcador = 0                 # Para saber cuántos puntos lleva el usuario ganando.
        self.mayorPuntaje = 0             # En caso de que se llegue a superar el récord del juego.
        self.contador = 0                 # Permite avanzar a través de la lista.
        self.juegoInicial = False         # Indica en qué momento el usuario apretó el botón "INICIAR".
        self.colores = ["Verde", "Rojo", "Amarillo", "Azul"]
        self.ventana.title("Simón Dice")
        self.ventana.geometry("400x400")
        self.iniciarBotones()             # Se llama a un método que se encargará de INICIAR la INTERFAZ GRÁFICA.
        self.ventana.mainloop()           # Indica que va a iniciar el CICLO PRINCIPAL del juego.


    # INTERFAZ GRÁFICA DEL JUEGO
    def iniciarBotones(self):
        self.botonVerde = Button(self.ventana, command=lambda: self.presionar("Verde"), height=6, width=13, background="green")

        # Botón que se localizará dentro de la ventana que cuando se presione se ejecutará un método. Para evitar hacer una función por cada botón se llama a un método "presionar" en general, mandándole como PARÁMETRO el botón que se presionó. "command" no permite el ENVÍO DE PARÁMETROS, por ello se utiliza "lambda", creando una función "self.presionar".

        # Lambda es una forma de crear funciones sin nombre de manera concisa. Su sintaxis es lambda argumentos: expresión, siendo esta última una sola expresión que se evalúa y se devuelve. Las funciones lambda se suelen utilizar en situaciones donde se necesita una pequeña función desechable y no se quiere definir una función completa con def.

        self.botonVerde.place(x=100, y=100) # Permite colocar el botón.

        self.botonRojo = Button(self.ventana, command=lambda: self.presionar("Rojo"), height=6, width=13, background="red")
        self.botonRojo.place(x=200, y=100)  # Se cambia la posición de cada botón.

        self.botonAmarillo = Button(self.ventana, command=lambda: self.presionar("Amarillo"), height=6, width=13, background="yellow")
        self.botonAmarillo.place(x=100, y=200)

        self.botonAzul = Button(self.ventana, command=lambda: self.presionar("Azul"), height=6, width=13, background="blue")
        self.botonAzul.place(x=200, y=200)

        self.botonIniciar = Button(self.ventana, command=self.iniciar, height=2, width=7, bg="white", text="Iniciar") # "bg" es "background".
        # Como no se manda parámetros en el command, se pone directamente el método que se va a ejecutar.
        
        self.botonIniciar.place(x=175, y=40)
        self.etiqueta = Label(self.ventana, text="Marcador: 0\nPuntaje récord: 0") # Se coloca en 0 porque ya se sabe en qué valor INICIA.
        self.etiqueta.place(x=40, y=30)
        
    def presionar(self):
        print("")

    def iniciar(self):                   # Lo que hace es REINICIAR todos los valores, ya sea para la 1era, 2da, 3ra o 4ta vez de iniciar el juego.
        self.contador = 0
        self.marcador = 0
        self.secuencia = []
        self.juegoInicial = True         # True porque el juego inició.
        self.crearColor()                # Método para que el usuario EMPIECE A JUGAR.

    def revisarTurno(self):
        if len(self.secuencia) == self.contador:    # El contador va aumentando conforme el usuario va jugando (cuando hace un punto).
            self.contador = 0                       # Se setea en 0 porque se iniciará de nuevo.
            self.marcador += 1                      # Aumenta el marcador porque el usuario apretó los botones correctamente (tiene un punto más).
            self.botonIniciar.after(1000, self.crearColor) 
            
            # El método after, después de la cantidad de MILISEGUNDOS (1000, 1 segundo), llamará a un método que AUMENTARÁ LA DIFICULTAD al añadir un color más.

    def crearColor(self):                # Método para que permite generar un nuevo color para aumentar la dificultad dentro del juego. 
        print("")

    def cambioColorBoton(self, boton, colorCambio, colorInicial, frecuencia, duracion):#Los últimos 2 parámetros sirven para el sonido al apretar un botón.
        print("")

    def sonido(self, frecuencia, duracion):
        winsound.Beep(frecuencia, duracion) # La frecuencia determina la tonalidad del sonido (si es alto o bajo), la duración, cuántos segundos durará.

test = SimonDice()

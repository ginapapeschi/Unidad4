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
        self.etiqueta = Label(self.ventana, text="\nMarcador: 0\nMayor puntaje: 0") # Se coloca en 0 porque ya se sabe en qué valor INICIA.
        self.etiqueta.place(x=40, y=30)
        
    def presionar(self, color):          # Se ejecuta en el momento en que el usuario presione el botón de alguno de los colores.
        if self.juegoInicial == True:    # Sólo se revisa en qué momento el usuario aprieta los botones cuando esta variable sea igual a True.
            if len(self.secuencia) >= self.contador - 1: # Ya que el contador va en una posición adelantada.
                if self.secuencia[self.contador] == color: # Color es el parámetro enviado por cada botón al ser presionado (usuario atinó al botón).
                    self.contador += 1               # Para que vaya avanzando
                    if color == "Verde":
                        self.sonido(600, 500)
                    elif color == "Rojo":
                        self.sonido(500, 500)
                    elif color == "Amarillo":
                        self.sonido(700, 500)
                    elif color == "Azul":
                        self.sonido(800, 500)
                    self.revisarTurno() # Llama a esta función para saber si este botón que presionó el usuario fue el último o faltan más.
                    self.etiqueta.config(text="\nMarcador: " + str(self.marcador) + "\nMayor puntaje: " + str(self.mayorPuntaje)) # Se cambia la etiqueta luego de que el usuario presionó los botones

                else:                   # Si el usuario se equivocó al presionar un botón (DEBE TERMINAR EL JUEGO)
                    messagebox.showinfo("Perdiste mogo", "\nPuntaje: " + str(self.marcador))
                    if self.marcador > self.mayorPuntaje:   # Se establece un nuevo récord en caso de ser así.
                        self.mayorPuntaje = self.marcador
                    self.etiqueta.config(text="\nMarcador: " + str(self.marcador) + "\nMayor puntaje: " + str(self.mayorPuntaje))

        # SE RESETEAN LOS ATRIBUTOS
                    self.juegoInicial = False               # Para que el usuario no siga jugando y deba presionar el botón de INICIAR para volver a jugar.
                    self.contador = 0
                    self.marcador = 0
                    self.secuencia = []




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

    def crearColor(self):                      # Método para que permite generar un nuevo color para aumentar la dificultad dentro del juego. 
        if self.juegoInicial == True:          # Chequea si el juego está iniciado o no.
            i = 0                              # Variable que recorre todo el arreglo.
            while i < len(self.secuencia):
                if self.secuencia[i] == "Verde":
                    self.cambioColorBoton(self.botonVerde, "black", "green", 500, 500)
                elif self.secuencia[i] == "Rojo":
                    self.cambioColorBoton(self.botonRojo, "black", "red", 500, 500)
                elif self.secuencia[i] == "Amarillo":
                    self.cambioColorBoton(self.botonAmarillo, "black", "yellow", 500, 500)
                elif self.secuencia[i] == "Azul":
                    self.cambioColorBoton(self.botonAzul, "black", "blue", 500, 500)

                i += 1
                time.sleep(1)                   # Para que no vaya tan rápido, 1 segundo de diferencia en la animación de recorrer las posiciones.
            aleatorio = random.randrange(0, 4)  # Rango de 0 a 4. Dependiendo del número aleatorio es el botón que se va a encender.
            self.secuencia.append(self.colores[aleatorio]) 
            # Al arreglo que está guardando el número de los colores se le agrega un nuevo elemento de una posición random en el arreglo de colores.
            if self.secuencia[i] == "Verde":    # Como es un nuevo botón y el usuario debe saber qué boton se iluminó
                self.cambioColorBoton(self.botonVerde, "black", "green", 500, 500)
            elif self.secuencia[i] == "Rojo":
                self.cambioColorBoton(self.botonRojo, "black", "red", 500, 500)
            elif self.secuencia[i] == "Amarillo":
                self.cambioColorBoton(self.botonAmarillo, "black", "yellow", 500, 500)
            elif self.secuencia[i] == "Azul":
                self.cambioColorBoton(self.botonAzul, "black", "blue", 500, 500)
            # Primero recorre todas las posiciones del arreglo y después agrega un nuevo color.

    def cambioColorBoton(self, boton, colorCambio, colorInicial, frecuencia, duracion):#Los últimos 2 parámetros sirven para el sonido al apretar un botón.
        boton.configure(bg=colorCambio)
        self.ventana.update()               # Para actualizar el fondo porque hubo un cambio de color, y quiero mostrarlo.
        self.sonido(frecuencia, duracion)   # El beep suena al hacer el cambio de color.
        boton.configure(bg=colorInicial)    # Lo manda a su color original.
        self.ventana.update()               # Se actualiza la ventana para ver ese cambio.
        

    def sonido(self, frecuencia, duracion):
        winsound.Beep(frecuencia, duracion) # La frecuencia determina la tonalidad del sonido (si es alto o bajo), la duración, cuántos segundos durará.

test = SimonDice()

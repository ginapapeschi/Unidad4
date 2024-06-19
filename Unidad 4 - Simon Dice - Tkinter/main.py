from tkinter import *
from tkinter import ttk, font
import tkinter as tk
import random                                             # Porque son aleatorios los botones que se apretarán.
import time                                               # Para las pausas entre cada ronda.
import winsound                                           # Para ejecutar sonidos al apretar los botones.
import json
from functools import partial

class SimonDice:
    __ventana: object
    __secuencia: list
    __marcador: int
    __puntajeRecord: int
    __contador: int
    __juegoInicial: bool
    __colores: list

    def __init__(self):
        self.__ventana = tk.Tk()            # Se crea una ventana y se le asigna un nuevo constructor de Tk para crear el nuevo frame.
        self.__secuencia = []               # Lista donde se almacenará el ORDEN de los colores conforme se fueron encendiendo.
        self.__marcador = 0                 # Para saber cuántos puntos lleva el usuario ganando.
        self.__puntajeRecord = 0             # En caso de que se llegue a superar el récord del juego.
        self.__contador = 0                 # Permite avanzar a través de la lista.
        self.__juegoInicial = False         # Indica en qué momento el usuario apretó el botón "INICIAR".
        self.__colores = ["Verde", "Rojo", "Amarillo", "Azul"]
        self.__ventana.title("Simón Dice")
        self.__ventana.geometry("400x500")

        self.__ventana.resizable(False, False)          # 19/6
        self.__ventana.withdraw()                       # 19/6 
        self.__nombreUsuario = None                     # 19/6
        self.preguntarNombre()                          # 19/6
        self.centrarVentana(self.__ventana)             # 19/6
        self.__timer = None                             # 19/6


        self.__ventana.configure(background="#f0f0f0")
        self.__ventana.mainloop()           # Indica que va a iniciar el CICLO PRINCIPAL del juego.

    def centrarVentana(self, ventana):
        ventana.update_idletasks()  # Asegura que las dimensiones de la ventana son correctas.
        ancho = ventana.winfo_width()
        alto = ventana.winfo_height()
        x = (ventana.winfo_screenwidth() // 2) - (ancho // 2)
        y = (ventana.winfo_screenheight() // 2) - (alto // 2)       # División entera.
        ventana.geometry(f'{ancho}x{alto}+{x}+{y}') 

# 19/6
    def preguntarNombre(self):
        ventanaIngresarNombre = tk.Toplevel()               # Crea una ventana SECUNDARIA para ingresar nombre.
        ventanaIngresarNombre.title("Simon Dice")
        label = tk.Label(ventanaIngresarNombre, text="Ingrese su nombre:", font=("Comic Sans MS", 10)) # Etiqueta de instrucción.
        label.pack(padx=80, pady=10)
        nombre = tk.Entry(ventanaIngresarNombre)            # Campo de entrada para el nombre del usuario.
        nombre.pack(padx=20, pady=5)
        boton = tk.Button(ventanaIngresarNombre, text="Aceptar", font=("Comic Sans MS", 10), command=partial(self.obtenerNombre, nombre, ventanaIngresarNombre))                             # Botón para aceptar.
        boton.pack(padx=20, pady=10)
        self.centrarVentana(ventanaIngresarNombre)             # 19/6
        ventanaIngresarNombre.resizable(False, False)          # 19/6
        
# 19/6
        # Función para obtener el nombre ingresado.
    def obtenerNombre(self, nombre, ventanaIngresarNombre):
        nombre = nombre.get().strip()   # El método "strip()" sirve para eliminar espacios en blanco al inicio y al final de la cadena.

        #VALIDACIÓN DEL NOMBRE
        if len(nombre) <= 10 and len(nombre) != 0:
            self.__nombreUsuario = nombre
        
        elif len(nombre) > 10:
            ventanaIngresarNombre.destroy()     # Se destruye la primera ventana secundaria.
            
            ventanaIngresarNombre2 = tk.Toplevel()               
            ventanaIngresarNombre2.title("Simon Dice")
            label = tk.Label(ventanaIngresarNombre2, text="Excede los 10 caracteres. Ingrese su nombre:", font=("Comic Sans MS", 10)) 
            label.pack(padx=80, pady=10)
            nombre = tk.Entry(ventanaIngresarNombre2)            
            nombre.pack(padx=20, pady=5)
            boton = tk.Button(ventanaIngresarNombre2, text="Aceptar", font=("Comic Sans MS", 10), command=partial(self.obtenerNombre, nombre, ventanaIngresarNombre2))
            boton.pack(padx=20, pady=10)
            self.centrarVentana(ventanaIngresarNombre2)             # 19/6
            ventanaIngresarNombre2.resizable(False, False)          # 19/6

        else:
            ventanaIngresarNombre.destroy()     # Se destruye la primera ventana secundaria.
            
            ventanaIngresarNombre3 = tk.Toplevel()               
            ventanaIngresarNombre3.title("Simon Dice")
            label = tk.Label(ventanaIngresarNombre3, text="No se ingresó ningún nombre. Ingrese su nombre:", font=("Comic Sans MS", 10))
            label.pack(padx=80, pady=10)
            nombre = tk.Entry(ventanaIngresarNombre3)  
            nombre.pack(padx=20, pady=5)
            boton = tk.Button(ventanaIngresarNombre3, text="Aceptar", font=("Comic Sans MS", 10), command=partial(self.obtenerNombre, nombre, ventanaIngresarNombre3))
            boton.pack(padx=20, pady=10)
            self.centrarVentana(ventanaIngresarNombre3)     # 19/6
            ventanaIngresarNombre3.resizable(False, False)  # 19/6

        if self.__nombreUsuario:
            ventanaIngresarNombre.destroy()  # Cerrar la ventana que pregunta el nombre.
            self.__ventana.deiconify()       # Mostrar la ventana del juego principal.
            self.elegirDificultad()         # 19/6
            self.iniciarBotones()
            self.__labNombre.config(text=f"Nombre: {str(self.__nombreUsuario)}", font=("Comic Sans MS", 10))
            # Se llama a un método que se encargará de INICIAR la INTERFAZ GRÁFICA.
            #if self.__juegoInicial == False: # Comprueba si el juego aún no ha comenzado.
            #    self.__botonIniciar.after(1600, self.iniciar)
        


    # 19/6
    def elegirDificultad(self):
        ventanaElegirDificultad = tk.Toplevel()
        ventanaElegirDificultad.title("Elegir dificultad")

        ventanaElegirDificultad.geometry('400x200')  # Ajustar el tamaño de la ventana

        label = tk.Label(ventanaElegirDificultad, text="Seleccione una dificultad:", font=("Comic Sans MS", 10))
        label.place(relx=0.5, rely=0.17, anchor=tk.CENTER)

        labelFrameSeleccione = ttk.LabelFrame(ventanaElegirDificultad, text='Elija una opción', borderwidth=2, relief='raised', padding=5)
        labelFrameSeleccione.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Lista de opciones para el OptionMenu
        opciones = ['Dificultad', 'Principiante', 'Experto', 'Súper Experto']

        # Variable para almacenar la opción seleccionada
        opcionSeleccionada = tk.StringVar(ventanaElegirDificultad)
        opcionSeleccionada.set(opciones[0])  # Opción por defecto

        optionMenu = ttk.OptionMenu(labelFrameSeleccione, opcionSeleccionada, *opciones)
        optionMenu.pack(padx=20, pady=10)

        
        botonConfirmar = ttk.Button(ventanaElegirDificultad, text="Confirmar")  # Falta el comando.
        botonConfirmar.place(relx=0.5, rely=0.85, anchor=tk.CENTER)


        self.centrarVentana(ventanaElegirDificultad)
        ventanaElegirDificultad.resizable(False, False)


    
    # INTERFAZ GRÁFICA DEL JUEGO
    def iniciarBotones(self):
        band = True
        """
        # 19/6 - Se colocan en 0 porque ya se sabe en qué valor INICIA.
        self.__labMarcador = Label(self.__ventana, text="Marcador: 0", font=("Arial", 10))
        self.__labMarcador.place(relx=0.20, rely=0.010, anchor=tk.NW)
        self.__labMarcador.destroy()        # Para destruirlo una vez ingresado el nombre.

        self.__labMayorPuntaje = Label(self.__ventana, text="Mayor puntaje: 0", font=("Arial", 10))
        self.__labMayorPuntaje.place(relx=0.59, rely=0.010, anchor=tk.NW)
        self.__labMayorPuntaje.destroy()    # Para destruirlo una vez ingresado el nombre.
        """

        # 19/6 ETIQUETAS
        self.__labMarcador = Label(self.__ventana, text=f"Marcador: {self.__marcador}", font=("Comic Sans MS", 10))
        self.__labMarcador.place(relx=0.40, rely=0.011, anchor=tk.NW)

        self.__labMayorPuntaje = Label(self.__ventana, text=f"Mayor puntaje: {self.__puntajeRecord}", font=("Comic Sans MS", 10))
        self.__labMayorPuntaje.place(relx=0.71, rely=0.011, anchor=tk.NW)

        self.__labNombre = Label(self.__ventana, text=f"Nombre: {self.__nombreUsuario}", font=("Comic Sans MS", 10))
        self.__labNombre.place(relx=0.02, rely=0.011, anchor=tk.NW)
        #


        # BOTONES
        self.__botonVerde = Button(self.__ventana, command=partial(self.presionar, "Verde"), background="#008080", highlightthickness=20, relief="raised")
        self.__botonVerde.place(relx=0.29, rely=0.28, relheight=0.45, relwidth=0.4, anchor=tk.CENTER) # Permite colocar el botón.

        self.__botonRojo = Button(self.__ventana, command=partial(self.presionar,"Rojo"), background="#ff0000", highlightthickness=20, relief="raised")
        self.__botonRojo.place(relx=0.72, rely=0.28, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)  # Se cambia la posición de cada botón.

        self.__botonAmarillo = Button(self.__ventana, command=partial(self.presionar, "Amarillo"), background="#ffff00", highlightthickness=20, relief="raised")
        self.__botonAmarillo.place(relx=0.29, rely=0.75, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)

        self.__botonAzul = Button(self.__ventana, command=partial(self.presionar,"Azul"), background="#0080ff", highlightthickness=20, relief="raised")
        self.__botonAzul.place(relx=0.72, rely=0.75, relheight=0.45, relwidth=0.4, anchor=tk.CENTER)

        self.__botonIniciar = Button(self.__ventana, command=self.iniciar, bg="white", text="INICIAR", font=("Comic Sans MS", 10)) # "bg" es "background".
        # Como no se manda parámetros en el command, se pone directamente el método que se va a ejecutar.
        self.__botonIniciar.place(relx=0.505, rely=0.46, relheight=0.1, relwidth=0.2, anchor=tk.N)

    def presionar(self, color):          # Se ejecuta en el momento en que el usuario presione el botón de alguno de los colores.
        if self.__juegoInicial == True:    # Sólo se revisa en qué momento el usuario aprieta los botones cuando esta variable sea igual a True.
            if len(self.__secuencia) >= self.__contador - 1: # Ya que el contador va en una posición adelantada.
                if self.__secuencia[self.__contador] == color: # Color es el parámetro enviado por cada botón al ser presionado (usuario atinó al botón).
                    self.__contador += 1               # Para que vaya avanzando
                    if color == "Verde":
                        self.sonido(600, 500)
                    elif color == "Rojo":
                        self.sonido(500, 500)
                    elif color == "Amarillo":
                        self.sonido(700, 500)
                    elif color == "Azul":
                        self.sonido(800, 500)
                    self.revisarTurno() # Llama a esta función para saber si este botón que presionó el usuario fue el último o faltan más.

                    # 19/6
                    self.__labMarcador.config(text=f"Marcador: {str(self.__marcador)}", font=("Comic Sans MS", 10))
                    # Se cambia la etiqueta luego de que el usuario presionó los botones

                    """
                    self.__etiqueta.config(text=f"Nombre: {self.__nombreUsuario}\nMarcador: " + str(self.__marcador) + "\nMayor puntaje: " + str(self.__puntajeRecord)) 
                    """
                else:                   # Si el usuario se equivocó al presionar un botón (DEBE TERMINAR EL JUEGO)
                    self.finalizar()

    def finalizar(self):
        if self.__marcador > self.__puntajeRecord:   # Se establece un nuevo récord en caso de ser así.
            self.__puntajeRecord = self.__marcador

    # 19/6 - CUANDO EL USUARIO INGRESA EL NOMBRE
        # MARCADOR
        self.__labMarcador.config(text=f"Marcador: {str(self.__marcador)}", font=("Comic Sans MS", 10))
        # MAYOR PUNTAJE
        self.__labMayorPuntaje.config(text=f"Mayor puntaje: {str(self.__puntajeRecord)}", font=("Comic Sans MS", 10))
        # NOMBRE:
        self.__labNombre.config(text=f"Nombre: {str(self.__nombreUsuario)}", font=("Comic Sans MS", 10))
        
        self.__ventanaPerdiste = Toplevel(self.__ventana)
        self.__ventanaPerdiste.title("Perdiste mogo")
        self.__ventanaPerdiste.geometry('300x150')
        label = tk.Label(self.__ventanaPerdiste, text=f"\nPuntaje: {str(self.__marcador)}")
        label.pack(pady=10)
        self.centrarVentana(self.__ventanaPerdiste)
        self.__ventanaPerdiste.resizable(False, False)   # 19/6

        self.__juegoInicial = False  # Se asegura de que el juego se detenga.

        self.__labNombre.config(text=f"Nombre: {""}", font=("Comic Sans MS", 10)) # Reinicia el Nombre
    
        

    #JEISON
        self.guardarPuntaje()
        boton_reiniciar = ttk.Button(self.__ventanaPerdiste, text="REINICIAR JUEGO", command=self.reiniciarJuego)
        boton_reiniciar.pack(side=tk.LEFT, padx=20, pady=20)
        boton_salir = ttk.Button(self.__ventanaPerdiste, text='SALIR', command=quit)
        boton_salir.pack(side=tk.RIGHT, padx=20, pady=20)
        
        
        
        
        """
        self.__ventanaPerdiste = Tk()
        self.__ventanaPerdiste.title("Perdiste mogo")
        self.__ventanaPerdiste.geometry('290x115')
        ttk.Button(self.__ventanaPerdiste, text="REINICIAR JUEGO", command=self.reiniciarJuego).grid(column=2, row=3, sticky=W)
        ttk.Button(self.__ventanaPerdiste, text='SALIR', command=quit).grid(column=3, row=3, sticky=W)
        """
        
        #self.__botonReiniciar = Button(self.__ventana, command=self.reiniciarJuego, bg="white", text="REINICIAR JUEGO")
        #self.__botonReiniciar.place(relx=0.505, rely=0.45, relheight=0.1, relwidth=0.25, anchor=tk.N)


    def reiniciarJuego(self):
        # SE RESETEAN LOS ATRIBUTOS
        self.__juegoInicial = False # Para que el usuario no siga jugando y deba presionar el botón de INICIAR para volver a jugar.
        self.__ventanaPerdiste.destroy()
        self.__nombreUsuario = None
        self.__botonIniciar.destroy()
        self.preguntarNombre()
        #self.__botonIniciar.after(1600, self.iniciar)  # 19/6 - ELIMINAR
        
    def iniciar(self):                   # Lo que hace es REINICIAR todos los valores, ya sea para la 1era, 2da, 3ra o 4ta vez de iniciar el juego.
        self.__contador = 0
        self.__marcador = 0
        self.__secuencia = []
        self.__juegoInicial = True       # True porque el juego inició.
        self.__botonIniciar.destroy()


        
    # 19/6 - CUANDO EL USUARIO INGRESA EL NOMBRE
        # MARCADOR
        
        self.__labMarcador.config(text=f"Marcador: {str(self.__marcador)}", font=("Comic Sans MS", 10))

        # MAYOR PUNTAJE
        
        self.__labMayorPuntaje.config(text=f"Mayor puntaje: {str(self.__puntajeRecord)}", font=("Comic Sans MS", 10))

        # NOMBRE:
        self.__labNombre.config(text=f"Nombre: {str(self.__nombreUsuario)}", font=("Comic Sans MS", 10))





        #self.__etiqueta.config(text=f"Nombre: {self.__nombreUsuario}\nMarcador: " + str(self.__marcador) + "\nMayor puntaje: " + str(self.__puntajeRecord))

        self.__botonIniciar.destroy()    # Destruye el botón de INICIO.
        self.crearColor()                # Método para que el usuario EMPIECE A JUGAR.

    def revisarTurno(self):
        if len(self.__secuencia) == self.__contador:  # El contador va aumentando conforme el usuario va jugando (cuando hace un punto).
            self.__contador = 0                       # Se setea en 0 porque se iniciará de nuevo.
            self.__marcador += 1                      # Aumenta el marcador porque el usuario apretó los botones correctamente (tiene un punto más).
            self.__botonIniciar.after(1000, self.crearColor)
            # El método after, después de la cantidad de MILISEGUNDOS (1000, 1 segundo), llamará a un método que AUMENTARÁ LA DIFICULTAD al añadir un color más.

    def crearColor(self):                       # Método para que permite generar un nuevo color para aumentar la dificultad dentro del juego. 
        if self.__juegoInicial == True:         # Chequea si el juego está iniciado o no.
            i = 0                               # Variable que recorre todo el arreglo.
#            self.__botonIniciar.destroy()

            while i < len(self.__secuencia):
                
                # 19/6
                if not self.__juegoInicial:  # Verifica si el juego todavía está en curso, evitando que se realice cualquier procesamiento si el juego no está activo.
                    return
                

                if self.__secuencia[i] == "Verde":
                    self.cambioColorBoton(self.__botonVerde, "white", "#008080", 500, 500)
                elif self.__secuencia[i] == "Rojo":
                    self.cambioColorBoton(self.__botonRojo, "white", "#ff0000", 500, 500)
                elif self.__secuencia[i] == "Amarillo":
                    self.cambioColorBoton(self.__botonAmarillo, "white", "#ffff00", 500, 500)
                elif self.__secuencia[i] == "Azul":
                    self.cambioColorBoton(self.__botonAzul, "white", "#0080ff", 500, 500)

                i += 1

# PARA AUMENTAR DIFICULTAD
                time.sleep(1)                 # Para que no vaya tan rápido, 1 segundo de diferencia en la animación de recorrer las posiciones.


            if not self.__juegoInicial:
                    return

            # Verifica nuevamente, crucial porque el estado __juegoInicial puede CAMBIAR mientras el método está en EJECUCIÓN. Si el jugador PIERDE mientras el bucle se ejecuta, se quiere asegurar que el método se DETENGA INMEDIATAMENTE y no continúe procesando la secuencia de colores.

            aleatorio = random.randrange(0, 4)  # Rango de 0 a 4. Dependiendo del número aleatorio es el botón que se va a encender.
            self.__secuencia.append(self.__colores[aleatorio]) 
            # Al arreglo que está guardando el número de los colores se le agrega un nuevo elemento de una posición random en el arreglo de colores.

            if self.__secuencia[i] == "Verde":    # Como es un nuevo botón y el usuario debe saber qué boton se iluminó
                self.cambioColorBoton(self.__botonVerde, "white", "#008080", 500, 500)
            elif self.__secuencia[i] == "Rojo":
                self.cambioColorBoton(self.__botonRojo, "white", "#ff0000", 500, 500)
            elif self.__secuencia[i] == "Amarillo":
                self.cambioColorBoton(self.__botonAmarillo, "white", "#ffff00", 500, 500)
            elif self.__secuencia[i] == "Azul":
                self.cambioColorBoton(self.__botonAzul, "white", "#0080ff", 500, 500)
            # Primero recorre todas las posiciones del arreglo y después agrega un nuevo color.

    def cambioColorBoton(self, boton, colorCambio, colorInicial, frecuencia, duracion):#Los últimos 2 parámetros sirven para el sonido al apretar un botón.
        boton.configure(bg=colorCambio)
        self.__ventana.update()               # Para actualizar el fondo porque hubo un cambio de color, y quiero mostrarlo.
        self.sonido(frecuencia, duracion)     # El beep suena al hacer el cambio de color.
        boton.configure(bg=colorInicial)      # Lo manda a su color original.
        self.__ventana.update()               # Se actualiza la ventana para ver ese cambio. 

    def sonido(self, frecuencia, duracion):
        winsound.Beep(frecuencia, duracion)   # La frecuencia determina la tonalidad del sonido (si es alto o bajo), la duración, cuántos segundos durará.


#JEISON
    def guardarPuntaje(self):                       # pedilo
        data = {
            "Nombre": self.__nombreUsuario,
            "Puntaje": self.__marcador
            #"Puntaje más alto": self.__mayorPuntaje # Clase usuario, atributos
            
        }
        with open("pysimonpuntajes.json", "a") as f:
            json.dump(data, f)
            f.write("\n")

if __name__ == '__main__':
    test = SimonDice()

  
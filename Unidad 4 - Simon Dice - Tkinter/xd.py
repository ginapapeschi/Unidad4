"""
self.__tiempoEspera = 1000                      # 20/6  

20/6 - Función para confirmar la dificultad elegida.
    def confirmarDificultad(self):
        dificultad = self.opcionSeleccionada.get()
        if dificultad == 'Principiante':
            self.__tiempoEspera = 1000
        elif dificultad == 'Experto':
            self.__tiempoEspera = 500
        elif dificultad == 'Súper Experto':
            self.__tiempoEspera = 250
        self.__ventanaElegirDificultad.destroy()



    # 20/6 - REVISAR TURNO Y CREAR COLOR PARA AUMENTAR DIFICULTAD

    def revisarTurno(self):
        if len(self.__secuencia) == self.__contador:  # El contador va aumentando conforme el usuario va jugando (cuando hace un punto).
            self.__contador = 0                       # Se setea en 0 porque se iniciará de nuevo.
            self.__marcador += 1                      # Aumenta el marcador porque el usuario apretó los botones correctamente (tiene un punto más).
            self.__botonIniciar.after(self.__tiempoEspera, self.crearColor)
            # El método after, después de la cantidad de MILISEGUNDOS (1000, 1 segundo), llamará a un método que AUMENTARÁ LA DIFICULTAD al añadir un color más.


# 20/6
#   self.__botonIniciar.after(1000, self.crearColor) - PRINCIPIANTE
#   self.__botonIniciar.after(500, self.crearColor) - EXPERTO
#   self.__botonIniciar.after(200, self.crearColor) - SÚPER EXPERTO
"""
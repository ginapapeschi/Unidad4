class TemporizadorApp:
    def __init__(self): 
        self.__tiempo = 0
        self.temporizador_activado = False

    def iniciar_temporizador(self):
        if not self.temporizador_activado:
            self.temporizador_activado = True
            self.temporizador()

    def temporizador(self):
        if self.temporizador_activado:
            self.__tiempo += 1

    def detener_temporizador(self):
        self.temporizador_activado = False

    def getTiempo(self):
        return self.__tiempo
from tkinter import ttk, font
import tkinter as tk

class LabelConEstilo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Ejemplo')
        self.resizable(0,0)
        self.geometry('255x195')
        self.config(padx=5, pady=5)
        fuente=font.Font(font='Verdana 10',weight='normal')
        self.valorMM=tk.IntVar()
        self.__texto=tk.StringVar()
        self.__texto.set('Texto ejemplo')
        # variables booleanas que controlan el estilo del texto
        self.subrayado=tk.BooleanVar()
        self.negrita=tk.BooleanVar()
        self.cursiva=tk.BooleanVar()
        self.tachado=tk.BooleanVar()
        # Elementos de la ventana
        self.textoLbl=ttk.Label(self, textvariable=self.__texto, font=fuente)
        opts = {'ipadx': 15, 'ipady': 15 , 'sticky': 'nswe'}
        self.textoLbl.grid(row=0, column=0, **opts, columnspan=2)
        
        labelFrameSeleccione=tk.LabelFrame(self, text='Seleccione:', font=fuente,borderwidth=2,
        relief='raised', padx=5, pady=5)
        labelFrameSeleccione.grid(row=1, column=0, **opts)
        labelFrameMarque=tk.LabelFrame(self, text='Marque:', font=fuente,borderwidth=2,
        relief="raised")
        labelFrameMarque.grid(row=1, column=1, **opts)
        ttk.Radiobutton(labelFrameSeleccione, text='Mayúsculas', value=0, variable=self.valorMM,
        command=self.cambiaValorMM).grid(row =2, column=0, columnspan=1, sticky='w')
        ttk.Radiobutton(labelFrameSeleccione, text='Minúsculas', value=1, variable=self.valorMM,
        command=self.cambiaValorMM).grid(row =3, column=0, columnspan=1,sticky='w')
        ttk.Checkbutton(labelFrameMarque, text='Subrayado',variable=self.subrayado,
        command=self.cambiarEstilo).grid(row=2, column=1, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque, text='Negrita',variable=self.negrita,
        command=self.cambiarEstilo).grid(row=3, column=1, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque, text='Cursiva',variable=self.cursiva,
        command=self.cambiarEstilo).grid(row=4, column=1, columnspan=1, sticky='w')
        ttk.Checkbutton(labelFrameMarque, text='Tachado', variable=self.tachado,
        command=self.cambiarEstilo).grid(row=5, column=1, columnspan=1, sticky='w')
        self.valorMM.set(-1)

    def cambiaValorMM(self):
        if self.valorMM.get()==0:
            self.__texto.set(self.__texto.get().upper())

        elif self.valorMM.get()==1:
            self.__texto.set(self.__texto.get().lower())

    def cambiarEstilo(self):
        subrayado=' underline ' if self.subrayado.get()==True else''
        negrita=' bold ' if self.negrita.get()==True else ''
        cursiva=' italic ' if self.cursiva.get()==True else ''
        tachado=' overstrike ' if self.tachado.get()==True else ''
        fuente='Verdana 10'+subrayado+negrita+cursiva+tachado
        self.textoLbl.configure(font=fuente)

    def testAPP():
        app=LabelConEstilo()
        app.mainloop()

if __name__=='__main__':
    test = LabelConEstilo
    test.testAPP()
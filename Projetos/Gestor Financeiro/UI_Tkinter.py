from tkinter import *
import os
from PIL import Image, ImageTk

# Class das Instâncias
class Screen_Longin():
    def __init__(self):
        #Inicializações
        self.Login = Tk()
        self.Screen()
        self.Frame()
        self.BackGraund()
        self.TextBox()
        self.Button()

        #Loop
        self.Login.mainloop()
    
    def Screen(self):
        #Dimensões do screen
        self.largura_screen = self.Login.winfo_screenwidth()
        self.altura_screen = self.Login.winfo_screenheight()

        #Dimensões da janela
        self.largura = 1080
        self.altura = 680

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 1.8))

        #Icone da janela
        #self.Sign_IN.iconbitmap('Python/Projetos/Gestor Financeiro/IMG/IMG1.ico')

        #Nome da Aplicação
        self.Login.title('Financial Manager')

        #Define o tamanho da janela
        self.Login.geometry('{}x{}+{}+{}'.format(self.largura, self.altura, self.posx, self.posy))

        #Trava o redimensionamento da janela
        self.Login.resizable(False, False)

    def Frame(self):
        pass

    def BackGraund(self):
        pass

    def TextBox(self):
        pass

    def Button(self):
        pass
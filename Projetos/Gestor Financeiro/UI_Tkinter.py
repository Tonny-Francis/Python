from tkinter import *
import os
from PIL import Image, ImageTk

# Class das Instâncias
class Screen_Sign_IN():
    def __init__(self):
        #Inicializações
        self.Sign_IN = Tk()
        self.Screen()
        self.Frame()
        self.BackGraund()
        self.TextBox()
        self.Button()

        #Loop
        self.Sign_IN.mainloop()
    
    def Screen(self):
        #Dimensões do screen
        self.largura_screen = self.Sign_IN.winfo_screenwidth()
        self.altura_screen = self.Sign_IN.winfo_screenheight()

        #Dimensões da janela
        self.largura = 720
        self.altura = 480
        
        #Canvas
        self.canvas = Canvas(self.Sign_IN, width = self.largura, height = self.altura, bg = 'white')
        self.canvas.pack()

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 1.8))

        #Icone da janela
        #self.Sign_IN.iconbitmap('Python/Projetos/Gestor Financeiro/IMG/IMG1.ico')

        #Nome da Aplicação
        #self.Sign_IN.title('Gestor Financeiro')

        #Define o tamanho da janela
        self.Sign_IN.geometry('{}x{}+{}+{}'.format(self.largura, self.altura, self.posx, self.posy))

        #Trava o redimensionamento da janela
        self.Sign_IN.resizable(False, False)

    def Frame(self):
        pass

    def BackGraund(self):
        BackGraund = PhotoImage(file = 'Python/Projetos/Gestor Financeiro/IMG/Login/BackGraund.png')
        BackGraund_Image = self.canvas.create_image(0,0, anchor = NW, image = BackGraund)

    def TextBox(self):
        pass

    def Button(self):
        pass

class Screen_Sign_UP():
    def __init__(self):
        #Inicializações
        self.Sing_UP = Tk()
        self.Screen()
        self.Frame()
        self.Label()
        self.Widgets()
        self.Button()

        #Loop
        self.Sing_UP.mainloop()
    def Screen(self):
        pass

    def Frame(self):
        pass

    def Label(self):
        pass

    def Widgets(self):
        pass

    def Button(self):
        pass

class Screen_Main():
    def __init__(self):
        #Inicializações
        self.Main = Tk()
        self.Screen()
        self.Frame()
        self.Label()
        self.Widgets()
        self.Button()

        #Loop
        self.Main.mainloop()

    def Screen(self):
        pass

    def Frame(self):
        pass

    def Label(self):
        pass

    def Widgets(self):
        pass

    def Button(self):
        pass
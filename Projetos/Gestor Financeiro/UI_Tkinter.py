from tkinter import *

# Class das Instâncias
class Screen_Sign_IN():
    def __init__(self):
        #Inicializações
        self.Sing_IN = Tk()
        self.Screen()
        self.Frame()
        self.Label()
        self.Widgets()
        self.Button()

        #Loop
        self.Sing_IN.mainloop()
    
    def Screen(self):
        #Dimensões do screen
        self.largura_screen = self.Sing_IN.winfo_screenwidth()
        self.altura_screen = self.Sing_IN.winfo_screenheight()

        #Dimensões da janela
        self.largura = int(self.largura_screen - self.largura_screen * 0.75)
        self.altura = int(self.altura_screen - self.altura_screen * 0.6)

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 1.8))

        #Icone da janela
        self.Sing_IN.iconbitmap("Gestor Financeiro\IMG\IMG1.ico")

        #Nome da Aplicação
        self.Sing_IN.title('Gestor Financeiro')

        #Define o tamanho da janela
        self.Sing_IN.geometry('{}x{}+{}+{}'.format(self.largura, self.altura, self.posx, self.posy))

        #Trava o redimensionamento da janela
        self.Sing_IN.resizable(False, False)

    def Frame(self):
        pass

    def Label(self):
        pass

    def Widgets(self):
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
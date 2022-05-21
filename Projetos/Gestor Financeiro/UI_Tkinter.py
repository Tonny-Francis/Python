from tkinter import *

# Class das Instâncias
class Screen_Sign_IN():
    def __init__(self):
        #Inicializações
        self.Sign_IN = Tk()
        self.Screen()
        self.Frame()
        self.BackGraund()
        self.Widgets()
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

        #Posicionamento da janela no screen
        self.posx = int((self.largura_screen / 2) - (self.largura / 2))
        self.posy = int((self.altura_screen / 2) - (self.altura / 1.8))

        #Icone da janela
        #self.Sing_IN.iconbitmap("Gestor Financeiro\IMG\IMG1.ico")

        #Nome da Aplicação
        self.Sign_IN.title('Gestor Financeiro')

        #Define o tamanho da janela
        self.Sign_IN.geometry('{}x{}+{}+{}'.format(self.largura, self.altura, self.posx, self.posy))

        #Trava o redimensionamento da janela
        self.Sign_IN.resizable(False, False)

    def Frame(self):
        self._BackGraund = Frame(self.Sign_IN)

    def BackGraund(self):
        Img_1 = PhotoImage(file = 'IMG\Login\BackGraund.png')
        Canvas_BackGraund = Canvas(self.Sign_IN, width = 720, height = 480)
        Canvas_BackGraund.pack(fill = "both", expand = True) 
        Canvas_BackGraund.create_image( 0, 0, image = Img_1, anchor = "nw")

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
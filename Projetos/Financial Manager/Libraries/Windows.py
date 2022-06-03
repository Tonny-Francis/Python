from msilib.schema import Class
import os
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QPixmap, QFontDatabase
from PySide6.QtCore import Qt

#Janela de Auntenticação de Usúario
class Window_Login(QWidget):
    def __init__(self):
        super().__init__()
        #Importação de Fonte
        QFontDatabase.addApplicationFont('Python/Projetos/Financial Manager/Sources/Itim.ttf')
        #Inicializações das Funções
        self.Window_Config()
        self.BackGraund()
        self.TextBox()
        self.Button()
        self.show()
        
    def Window_Config(self):
        self.setWindowTitle('Financial Manager')
        self.setFixedSize(920, 580)

    def BackGraund(self):
        Img = QPixmap('Python/Projetos/Financial Manager/Images/BackGraund/BackGround-Login.png')
        Label_BackGraund = QLabel(self)
        Label_BackGraund.setPixmap(Img)

    def TextBox(self):
        User = QLineEdit('',self)
        User.setGeometry(380, 211, 160, 30)
        User.setAlignment(Qt.AlignCenter)
        User.setMaxLength(15)
        User.setStyleSheet(""" 
            QLineEdit{
                border-radius: 15px;
                font-family: Itim;
                font-size: 16px
            }
            QLineEdit:hover{
                border: 2px solid #38A2D7;
            }
            QLineEdit:focus{
                border: 2px solid #38A2D7;
            }
        """)

        Passorwd = QLineEdit('',self)
        Passorwd.setEchoMode(QLineEdit.EchoMode.Password)
        Passorwd.setAlignment(Qt.AlignCenter)
        Passorwd.setGeometry(380, 260, 160, 30)
        Passorwd.setMaxLength(15)
        Passorwd.setStyleSheet(""" 
            QLineEdit{
                border-radius: 15px;
                font-family: Itim;
                font-size: 16px
            }
            QLineEdit:hover{
                border: 2px solid #38A2D7;
            }
            QLineEdit:focus{
                border: 2px solid #38A2D7;
            }
        """)
    def Button(self):
        Get_Start = QPushButton('Get Start',self)
        Get_Start.setGeometry(422, 317, 80, 30)
        #Get_Start.setFont('Itim')
        Get_Start.setStyleSheet(""" 
            QPushButton{
                background-color: #525E70; 
                border-radius: 15px; 
                color: white;
                font-family: Itim;
                font-size: 16px
            }
            QPushButton:hover{
                border: 2px solid #38A2D7;
            }
        """)

        Sign_Up = QPushButton('Sign Up',self)
        Sign_Up.setGeometry(422, 385, 80, 30)
        #Get_Start.setFont('Itim')
        Sign_Up.setStyleSheet(""" 
            QPushButton{
                background-color: #525E70; 
                border-radius: 15px; 
                color: white;
                font-family: Itim;
                font-size: 16px
            }
            QPushButton:hover{
                border: 2px solid #38A2D7;
            }
        """)

    def State(self):
        return True

#Janela Principal
class Window_Main(QWidget):
    def __init__(self):
        super().__init__()
        #Inicializações das Funções
        self.Window_Config()

    def Window_Config(self):
        pass
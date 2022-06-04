from msilib.schema import Class
import os
from PySide6.QtWidgets import QWidget, QPushButton, QLabel, QLineEdit
from PySide6.QtGui import QPixmap, QFontDatabase
from PySide6.QtCore import Qt

#Janela de Auntenticação de Usuário
class Window_Login(QWidget):
    def __init__(self):
        super().__init__()
        #Importação de Fonte
        QFontDatabase.addApplicationFont('Python/Projetos/Financial Manager/Sources/Itim.ttf')
        #Inicializações das Funções
        self.Window_Config()
        self.BackGraund()
        self.Label()
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

    def Label(self):
        Login = QLabel('Login', self)
        Login.setGeometry(418, 145, 84, 54)
        Login.setStyleSheet(""" 
            QLabel{
                font-family: Itim;
                font-size: 36px;
                color: white;
            }
        """)

        User = QLabel('User', self)
        User.setGeometry(392, 194, 47, 17)
        User.setStyleSheet(""" 
            QLabel{
                font-family: Itim;
                font-size: 14px;
                color: white;
            }
        """)

        Password = QLabel('Password', self)
        Password.setGeometry(392, 243, 65, 17)
        Password.setStyleSheet(""" 
            QLabel{
                font-family: Itim;
                font-size: 14px;
                color: white;
            }
        """)

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
                border: 2px solid #00FFD4;
            }
            QLineEdit:focus{
                border: 2px solid #00FFD4;
            }
        """)

        Password = QLineEdit('',self)
        Password.setEchoMode(QLineEdit.EchoMode.Password)
        Password.setAlignment(Qt.AlignCenter)
        Password.setGeometry(380, 260, 160, 30)
        Password.setMaxLength(15)
        Password.setStyleSheet(""" 
            QLineEdit{
                border-radius: 15px;
                font-family: Itim;
                font-size: 16px
            }
            QLineEdit:hover{
                border: 2px solid #00FFD4;
            }
            QLineEdit:focus{
                border: 2px solid #00FFD4;
            }
        """)
    def Button(self):
        Get_Start = QPushButton('Get Start',self)
        Get_Start.setGeometry(422, 317, 80, 30)
        #Get_Start.setFont('Itim')
        Get_Start.setStyleSheet(""" 
            QPushButton{
                background-color: #242333; 
                border-radius: 15px; 
                color: white;
                font-family: Itim;
                font-size: 16px
            }
            QPushButton:hover{
                border: 2px solid #00FFD4;
            }
        """)

        Sign_Up = QPushButton('Sign Up',self)
        Sign_Up.setGeometry(422, 385, 80, 30)
        #Get_Start.setFont('Itim')
        Sign_Up.setStyleSheet(""" 
            QPushButton{
                background-color: #242333; 
                border-radius: 15px; 
                color: white;
                font-family: Itim;
                font-size: 16px
            }
            QPushButton:hover{
                border: 2px solid #00FFD4;
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
"""
----------------------------- Informações ----------------------------
Projeto: Financial Manager      Autor: Tonny Francis
Data de Inicio: 03/06/2022      Ultima Modificação: 03/06/2022

Objetivo da Aplicação: Criar uma aplicação onde o usuário possa 
fazer o gerenciamento de suas finanças mensais e obter um extrato.

Objetivo Pessoal: Obter conhecimento e praticar sobre desenvolvimento 
de interfaces gráficas e banco de dados.
----------------------------------------------------------------------
"""

#Importação de bibliotecas
from Files.Libraries.Qt_Core.Qt_Core import *
from Files.Libraries.Windows.Login_SingUp import Login
import sys

#Login Window
class Login_Window(QMainWindow):
    def __init__(self):
        super().__init__()
        
        #Setup Login Window
        self.Ui = Login.UI_Login_Window()
        self.Ui.Setup(self, 1)

        #Exibe as alterações
        self.show()

#Inicio do Loop
MyApp = QApplication(sys.argv)

# ----> Conteúdo do Loop <----

#Inicia a Tela de Login
Login_Window_ = Login_Window()

#Fim do Loop
sys.exit(MyApp.exec())
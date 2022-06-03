"""
----------------------------- Informações ----------------------------
Projeto: Financial Manager      Autor: Tonny Francis
Data de Inicio: 03/06/2022      Ultima Modificação: 03/06/2022

Objetivo da Aplicação: Criar uma aplicação onde o usúario pode 
fazer o gerenciamento de suas finanças mensais e obter um extrato.

Objetivo Pessoal: Obter conhecimento e praticar sobre desenvolvimento 
de interfaces gráficas.
----------------------------------------------------------------------
"""

#Importações
import sys
from PySide6.QtWidgets import QApplication
from Libraries import Windows

#Inicio do Loop
MyApp = QApplication(sys.argv)

# ----> Conteúdo do Loop <----
#Inicia a Tela de Login
Wind_Login = Windows.Window_Login()
State = Wind_Login.State()

#Verifica se a Proxima Tela deve ser Executada
if State is True:
    #Wind_Login.close()
    #Wind_Main = Windows.Windows_Main()
    pass

#Final do Loop
MyApp.exec()
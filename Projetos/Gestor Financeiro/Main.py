import UI_Tkinter as UI
import os

#Variável de Controle
Controle = 0

if Controle == 0:
    UI.Screen_Sign_IN()
elif Controle == 1:
    UI.Screen_Sign_UP()
else:
    UI.Screen_Main()
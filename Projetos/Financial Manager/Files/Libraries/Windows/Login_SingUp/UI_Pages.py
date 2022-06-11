from  Files.Libraries.Qt_Core.Qt_Core import *

class Ui_Login_SingUp_Pages(object):
    def setupUi(self, StackedWidget, State_Page):
        #Verificação padrão do Qt
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")

        # ----------------------> Main Widgets <---------------------
        self.Main_Frame = QFrame()
        self.Main_Frame.setMinimumSize(720, 480)
        self.Main_Frame.setStyleSheet('background-color: #242333')

        self.Main_Layout = QVBoxLayout(self.Main_Frame)
        self.Main_Layout.setContentsMargins(0, 0, 0, 0)
        self.Main_Layout.setSpacing(15)
        self.Main_Layout.setAlignment(Qt.AlignCenter)

        if State_Page == 1:
            # --------------------> Widgets de Perfil <------------------
            self.Login_Frame = QFrame()
            self.Login_Frame.setMinimumSize(225, 365)
            self.Login_Frame.setMaximumSize(225, 365)

            self.Img_QPixmap = QPixmap('Python/Projetos/Financial Manager/Files/Images/IMG1.png')
            self.Login_Background_Label = QLabel(self.Login_Frame)
            self.Login_Background_Label.setPixmap(self.Img_QPixmap)
        
            self.Login_Label = QLabel('Login', self.Login_Frame)
            self.Login_Label.setGeometry(68, 45, 84, 54)
            self.Login_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 36px;
                    color: white;
                }
            """)

            self.User_Label = QLabel('User', self.Login_Frame)
            self.User_Label.setGeometry(42, 94, 47, 17)
            self.User_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 14px;
                    color: white;
                }
            """)

            self.Password_Label = QLabel('Password', self.Login_Frame)
            self.Password_Label.setGeometry(42, 143, 65, 17)
            self.Password_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 14px;
                    color: white;
                }
            """)

            self.Or_Label = QLabel('Or', self.Login_Frame)
            self.Or_Label.setGeometry(100, 254, 21, 19)
            self.Or_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 14px;
                    color: white;
                }
            """)

            self.User_Lineedit = QLineEdit(self.Login_Frame)
            self.User_Lineedit.setGeometry(30, 111, 160, 30)
            self.User_Lineedit.setAlignment(Qt.AlignCenter)
            self.User_Lineedit.setMaxLength(15)
            self.User_Lineedit.setStyleSheet(""" 
                QLineEdit{
                    background-color: rgba(255, 255, 255, 100);
                    border-radius: 15px;
                    font-family: Itim;
                    font-size: 16px
                }
            """)

            self.Password_Lineedit = QLineEdit(self.Login_Frame)
            self.Password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            self.Password_Lineedit.setAlignment(Qt.AlignCenter)
            self.Password_Lineedit.setGeometry(30, 160, 160, 30)
            self.Password_Lineedit.setMaxLength(15)
            self.Password_Lineedit.setStyleSheet(""" 
                QLineEdit{
                    background-color: rgba(255, 255, 255, 100);
                    border-radius: 15px;
                    font-family: Itim;
                    font-size: 16px
                }
            """)

            self.Get_Start_Button = QPushButton('Get Start', self.Login_Frame)
            self.Get_Start_Button.setGeometry(72, 217, 80, 30)
            self.Get_Start_Button.setStyleSheet(""" 
                QPushButton{
                    background-color: #242333; 
                    border-radius: 15px; 
                    color: white;
                    font-family: Itim;
                    font-size: 16px
                }
                QPushButton:hover{
                    border: 2px solid #888890;
                }
            """)

            self.Sign_Up_Button = QPushButton('Sign Up', self.Login_Frame)
            self.Sign_Up_Button.setGeometry(72, 285, 80, 30)
            self.Sign_Up_Button.setStyleSheet(""" 
                QPushButton{
                    background-color: #242333; 
                    border-radius: 15px; 
                    color: white;
                    font-family: Itim;
                    font-size: 16px
                }
                QPushButton:hover{
                    border: 2px solid #888890;
                }
            """)
 
            # -------------------> Adicionando no Main <-----------------
            self.Main_Layout.addWidget(self.Login_Frame)

            StackedWidget.addWidget(self.Main_Frame)

        elif State_Page == 0:
            # ---------------------> Sing Up <--------------------
            self.SingUp_Frame = QFrame()
            self.SingUp_Frame.setMinimumSize(225, 365)
            self.SingUp_Frame.setMaximumSize(225, 365)

            self.Img_QPixmap = QPixmap('Python/Projetos/Financial Manager/Files/Images/IMG1.png')
            self.SingUp_Background_Label = QLabel(self.SingUp_Frame)
            self.SingUp_Background_Label.setPixmap(self.Img_QPixmap)
        
            self.SingUp_Label = QLabel('Sing Up', self.SingUp_Frame)
            self.SingUp_Label.setGeometry(49, 80, 122, 54)
            self.SingUp_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 36px;
                    color: white;
                }
            """)

            self.User_Label = QLabel('User', self.SingUp_Frame)
            self.User_Label.setGeometry(42, 129, 47, 17)
            self.User_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 14px;
                    color: white;
                }
            """)

            self.Password_Label = QLabel('Password', self.SingUp_Frame)
            self.Password_Label.setGeometry(42, 178, 65, 17)
            self.Password_Label.setStyleSheet(""" 
                QLabel{
                    background-color: rgba(255, 255, 255, 0);
                    font-family: Itim;
                    font-size: 14px;
                    color: white;
                }
            """)

            self.User_Lineedit = QLineEdit(self.SingUp_Frame)
            self.User_Lineedit.setGeometry(30, 146, 160, 30)
            self.User_Lineedit.setAlignment(Qt.AlignCenter)
            self.User_Lineedit.setMaxLength(15)
            self.User_Lineedit.setStyleSheet(""" 
                QLineEdit{
                    background-color: rgba(255, 255, 255, 100);
                    border-radius: 15px;
                    font-family: Itim;
                    font-size: 16px
                }
            """)

            self.Password_Lineedit = QLineEdit(self.SingUp_Frame)
            self.Password_Lineedit.setEchoMode(QLineEdit.EchoMode.Password)
            self.Password_Lineedit.setAlignment(Qt.AlignCenter)
            self.Password_Lineedit.setGeometry(30, 195, 160, 30)
            self.Password_Lineedit.setMaxLength(15)
            self.Password_Lineedit.setStyleSheet(""" 
                QLineEdit{
                    background-color: rgba(255, 255, 255, 100);
                    border-radius: 15px;
                    font-family: Itim;
                    font-size: 16px
                }
            """)

            self.Get_Start_Button = QPushButton('Get Start', self.SingUp_Frame)
            self.Get_Start_Button.setGeometry(72, 252, 80, 30)
            self.Get_Start_Button.setStyleSheet(""" 
                QPushButton{
                    background-color: #242333; 
                    border-radius: 15px; 
                    color: white;
                    font-family: Itim;
                    font-size: 16px
                }
                QPushButton:hover{
                    border: 2px solid #888890;
                }
            """)
 
            # -------------------> Adicionando no Main <-----------------
            self.Main_Layout.addWidget(self.SingUp_Frame)

            StackedWidget.addWidget(self.Main_Frame)
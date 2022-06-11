#Importação de bibliotecas
from Files.Libraries.Qt_Core.Qt_Core import *
from Files.Libraries.Windows.Login_SingUp.UI_Pages import Ui_Login_SingUp_Pages

#Login Window
class UI_Login_Window(object):
    def Setup(self, Parent, State_Page):
        #Verificação padrão do Qt
        if not Parent.objectName():
            Parent.setObjectName(u"Parent")

        #Definindo parametros iniciais: Tamanho e Nome
        Parent.setWindowTitle('Financial Manager')
        Parent.setMinimumSize(720, 480)

        #Importação de fonte Itim
        QFontDatabase.addApplicationFont('Python/Projetos/Financial Manager/Files/Sources/Itim.ttf')
        
        # ----------------------> Main <----------------------
        #Criando main frame
        self.Main_Frame = QFrame()
        self.Main_Frame.setStyleSheet('background-color: #242333;')

        #Criando main layout
        self.Main_Layout = QHBoxLayout(self.Main_Frame)
        self.Main_Layout.setContentsMargins(0, 0, 0, 0)
        self.Main_Layout.setSpacing(0)

        # ---------------------> Content <--------------------
        #Criando first frame
        self.Content_Frame = QFrame()
        self.Content_Frame.setStyleSheet('background-color: #242333;')

        #Criando first layout
        self.Content_Layout = QVBoxLayout(self.Content_Frame)
        self.Content_Layout.setContentsMargins(0, 0, 0, 0)
        self.Content_Layout.setSpacing(0)

        # ----------------------> Pages <---------------------
        #Criando first page
        self.Pages = QStackedWidget()
        self.Pages.setStyleSheet('background-color: #242333; color: white;')
        self.Ui_Pages = Ui_Login_SingUp_Pages()
        self.Ui_Pages.setupUi(self.Pages, State_Page)

        # ------------------> Login Screen <------------------
        #Criando bottom bar
        self.Bottom_Bar = QFrame()
        self.Bottom_Bar.setStyleSheet('background-color: #393744;')
        self.Bottom_Bar.setMinimumHeight(20)
        self.Bottom_Bar.setMaximumHeight(20)
        self.Bottom_Bar_Layout = QHBoxLayout(self.Bottom_Bar)
        self.Bottom_Bar_Layout.setContentsMargins(20, 0, 20, 0)

        #Left label
        self.Left_Label = QLabel('Created By: Tonny Francis')
        self.Left_Label.setStyleSheet('font-size: 8pt; font-family: Arial; color: white;')
        
        #Espaçamento
        self.Spacing = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        #Right label
        self.Right_Label = QLabel('© 2022 | V1.0.1')
        self.Right_Label.setStyleSheet('font-size: 8pt; font-family: Arial; color: white;')
        
        #Adicionando widget ao Bottom_Bar_Layout
        self.Bottom_Bar_Layout.addWidget(self.Left_Label)
        self.Bottom_Bar_Layout.addItem(self.Spacing)
        self.Bottom_Bar_Layout.addWidget(self.Right_Label)

        # -------------------> Definições <-------------------
        #Adicionando Widget ao Main_layout
        self.Main_Layout.addWidget(self.Content_Frame)

        #Adicionando Widget ao Content_layout
        self.Content_Layout.addWidget(self.Pages)
        self.Content_Layout.addWidget(self.Bottom_Bar)

        #Definindo widget central/primary
        Parent.setCentralWidget(self.Main_Frame)
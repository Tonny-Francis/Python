from  Files.Libraries.Qt_Core.Qt_Core import *

class Ui_Login_SingUp_Pages(object):
    def setupUi(self, StackedWidget):
        if not StackedWidget.objectName():
            StackedWidget.setObjectName(u"StackedWidget")
        StackedWidget.resize(400, 300)
        self.Page_Login = QWidget()
        self.Page_Login.setObjectName(u"Page_Login")
        self.verticalLayout_2 = QVBoxLayout(self.Page_Login)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label = QLabel(self.Page_Login)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label)

        StackedWidget.addWidget(self.Page_Login)
        self.Page_SignUp = QWidget()
        self.Page_SignUp.setObjectName(u"Page_SignUp")
        self.verticalLayout = QVBoxLayout(self.Page_SignUp)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.Page_SignUp)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_2)

        StackedWidget.addWidget(self.Page_SignUp)

        self.retranslateUi(StackedWidget)

        QMetaObject.connectSlotsByName(StackedWidget)
    # setupUi

    def retranslateUi(self, StackedWidget):
        StackedWidget.setWindowTitle(QCoreApplication.translate("StackedWidget", u"StackedWidget", None))
        self.label.setText(QCoreApplication.translate("StackedWidget", u"LOGIN", None))
        self.label_2.setText(QCoreApplication.translate("StackedWidget", u"SINGUP", None))
    # retranslateUi


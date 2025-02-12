# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'index2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)
import ressources_rc
import ressources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1231, 715)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(-1, 2, 1231, 712))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_only_widget = QWidget(self.layoutWidget)
        self.icon_only_widget.setObjectName(u"icon_only_widget")
        self.icon_only_widget.setMinimumSize(QSize(71, 0))
        self.icon_only_widget.setMaximumSize(QSize(71, 16777215))
        self.icon_only_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"\n"
"QPushButton:checked{\n"
"  \n"
"background-color: rgb(255, 255, 255);\n"
"  border-radius:3px;\n"
"}")
        self.verticalLayout_10 = QVBoxLayout(self.icon_only_widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 30, -1, -1)
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer_2 = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.icon_only_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(40, 40))
        self.label_4.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.horizontalSpacer = QSpacerItem(13, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_10.addLayout(self.horizontalLayout_2)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setSpacing(20)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, 30, -1, -1)
        self.dashboard_1 = QPushButton(self.icon_only_widget)
        self.dashboard_1.setObjectName(u"dashboard_1")
        icon = QIcon()
        icon.addFile(u":/icones/dashboardsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon.addFile(u":/icones/dashboardsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_1.setIcon(icon)
        self.dashboard_1.setCheckable(True)
        self.dashboard_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.dashboard_1)

        self.institution_1 = QPushButton(self.icon_only_widget)
        self.institution_1.setObjectName(u"institution_1")
        icon1 = QIcon()
        icon1.addFile(u":/icones/institutionsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon1.addFile(u":/icones/institutionsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_1.setIcon(icon1)
        self.institution_1.setIconSize(QSize(100, 16))
        self.institution_1.setCheckable(True)
        self.institution_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.institution_1)

        self.pointage_1 = QPushButton(self.icon_only_widget)
        self.pointage_1.setObjectName(u"pointage_1")
        icon2 = QIcon()
        icon2.addFile(u":/icones/teacherssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon2.addFile(u":/icones/teacherssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pointage_1.setIcon(icon2)
        self.pointage_1.setIconSize(QSize(100, 20))
        self.pointage_1.setCheckable(True)
        self.pointage_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.pointage_1)

        self.employe_1 = QPushButton(self.icon_only_widget)
        self.employe_1.setObjectName(u"employe_1")
        icon3 = QIcon()
        icon3.addFile(u":/icones/studentssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon3.addFile(u":/icones/studentssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.employe_1.setIcon(icon3)
        self.employe_1.setIconSize(QSize(100, 20))
        self.employe_1.setCheckable(True)
        self.employe_1.setAutoExclusive(True)

        self.verticalLayout_7.addWidget(self.employe_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_7)

        self.verticalSpacer = QSpacerItem(20, 328, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_10.addItem(self.verticalSpacer)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(20)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.setting_1 = QPushButton(self.icon_only_widget)
        self.setting_1.setObjectName(u"setting_1")
        icon4 = QIcon()
        icon4.addFile(u":/icones/settingssmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon4.addFile(u":/icones/settingssmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setting_1.setIcon(icon4)
        self.setting_1.setIconSize(QSize(100, 20))
        self.setting_1.setCheckable(True)
        self.setting_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.setting_1)

        self.sign_1 = QPushButton(self.icon_only_widget)
        self.sign_1.setObjectName(u"sign_1")
        icon5 = QIcon()
        icon5.addFile(u":/icones/signoutsmall1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon5.addFile(u":/icones/signoutsmall2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.sign_1.setIcon(icon5)
        self.sign_1.setIconSize(QSize(100, 16))
        self.sign_1.setCheckable(True)
        self.sign_1.setAutoExclusive(True)

        self.verticalLayout_8.addWidget(self.sign_1)


        self.verticalLayout_10.addLayout(self.verticalLayout_8)


        self.gridLayout.addWidget(self.icon_only_widget, 0, 0, 1, 1)

        self.icon_txt_widget = QWidget(self.layoutWidget)
        self.icon_txt_widget.setObjectName(u"icon_txt_widget")
        self.icon_txt_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(0, 0, 0);\n"
"   color:white;\n"
"}\n"
"\n"
"QPushButton{\n"
"  height:30px;\n"
"  border:none;\n"
"\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.icon_txt_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 20, -1, -1)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, -1, -1, -1)
        self.label_2 = QLabel(self.icon_txt_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(40, 40))
        self.label_2.setPixmap(QPixmap(u":/icones/logo.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(self.icon_txt_widget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.label_3.setFont(font)

        self.horizontalLayout.addWidget(self.label_3)


        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setSpacing(15)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 35, -1, -1)
        self.dashboard_2 = QPushButton(self.icon_txt_widget)
        self.dashboard_2.setObjectName(u"dashboard_2")
        self.dashboard_2.setStyleSheet(u"QPushButton{\n"
"  padding-left:15px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  \n"
"background-color: rgb(255, 255, 255);\n"
"  border-radius:3px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icones/dashboard2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon6.addFile(u":/icones/dashboard1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.dashboard_2.setIcon(icon6)
        self.dashboard_2.setIconSize(QSize(100, 60))
        self.dashboard_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.dashboard_2)

        self.institution_2 = QPushButton(self.icon_txt_widget)
        self.institution_2.setObjectName(u"institution_2")
        self.institution_2.setStyleSheet(u"QPushButton{\n"
"  padding-left:5px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  \n"
"background-color: rgb(255, 255, 255);\n"
"  border-radius:3px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icones/institution2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon7.addFile(u":/icones/institution1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.institution_2.setIcon(icon7)
        self.institution_2.setIconSize(QSize(95, 45))
        self.institution_2.setCheckable(True)

        self.verticalLayout_5.addWidget(self.institution_2)

        self.pointage_frame = QFrame(self.icon_txt_widget)
        self.pointage_frame.setObjectName(u"pointage_frame")
        self.pointage_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.pointage_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.pointage_frame)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.pointage_2 = QPushButton(self.pointage_frame)
        self.pointage_2.setObjectName(u"pointage_2")
        icon8 = QIcon()
        icon8.addFile(u":/icones/teachers3.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon8.addFile(u":/icones/teachers2.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.pointage_2.setIcon(icon8)
        self.pointage_2.setIconSize(QSize(100, 60))
        self.pointage_2.setCheckable(True)

        self.verticalLayout_4.addWidget(self.pointage_2)

        self.pointage_dropdown = QFrame(self.pointage_frame)
        self.pointage_dropdown.setObjectName(u"pointage_dropdown")
        self.pointage_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.pointage_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.pointage_dropdown)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pointage = QPushButton(self.pointage_dropdown)
        self.pointage.setObjectName(u"pointage")
        self.pointage.setStyleSheet(u"QPushButton{\n"
"  padding-left:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"}")
        self.pointage.setCheckable(True)

        self.verticalLayout_2.addWidget(self.pointage)

        self.historique = QPushButton(self.pointage_dropdown)
        self.historique.setObjectName(u"historique")
        self.historique.setStyleSheet(u"QPushButton{\n"
"  padding-left:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"}")
        self.historique.setCheckable(True)

        self.verticalLayout_2.addWidget(self.historique)


        self.verticalLayout_4.addWidget(self.pointage_dropdown)


        self.verticalLayout_5.addWidget(self.pointage_frame)

        self.employee = QFrame(self.icon_txt_widget)
        self.employee.setObjectName(u"employee")
        self.employee.setFrameShape(QFrame.Shape.StyledPanel)
        self.employee.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.employee)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.employe_2 = QPushButton(self.employee)
        self.employe_2.setObjectName(u"employe_2")
        icon9 = QIcon()
        icon9.addFile(u":/icones/students4.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon9.addFile(u":/icones/students1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.employe_2.setIcon(icon9)
        self.employe_2.setIconSize(QSize(100, 60))
        self.employe_2.setCheckable(True)

        self.verticalLayout_3.addWidget(self.employe_2)

        self.employee_dropdown = QFrame(self.employee)
        self.employee_dropdown.setObjectName(u"employee_dropdown")
        self.employee_dropdown.setFrameShape(QFrame.Shape.StyledPanel)
        self.employee_dropdown.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.employee_dropdown)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.employes = QPushButton(self.employee_dropdown)
        self.employes.setObjectName(u"employes")
        self.employes.setStyleSheet(u"QPushButton{\n"
"  padding-left:35px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"}")
        self.employes.setCheckable(True)

        self.verticalLayout.addWidget(self.employes)

        self.administrateurs = QPushButton(self.employee_dropdown)
        self.administrateurs.setObjectName(u"administrateurs")
        self.administrateurs.setStyleSheet(u"QPushButton{\n"
"  padding-left:60px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"  color:#12B298\n"
"}")
        self.administrateurs.setCheckable(True)

        self.verticalLayout.addWidget(self.administrateurs)


        self.verticalLayout_3.addWidget(self.employee_dropdown)


        self.verticalLayout_5.addWidget(self.employee)


        self.verticalLayout_9.addLayout(self.verticalLayout_5)

        self.verticalSpacer_2 = QSpacerItem(20, 148, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(20)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.setting_2 = QPushButton(self.icon_txt_widget)
        self.setting_2.setObjectName(u"setting_2")
        self.setting_2.setStyleSheet(u"QPushButton{\n"
"  padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  \n"
"background-color: rgb(255, 255, 255);\n"
"  border-radius:3px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icones/settings2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon10.addFile(u":/icones/settings1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.setting_2.setIcon(icon10)
        self.setting_2.setIconSize(QSize(100, 60))
        self.setting_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.setting_2)

        self.sign_2 = QPushButton(self.icon_txt_widget)
        self.sign_2.setObjectName(u"sign_2")
        self.sign_2.setStyleSheet(u"QPushButton{\n"
"  padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"  \n"
"background-color: rgb(255, 255, 255);\n"
"  border-radius:3px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icones/signout2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        icon11.addFile(u":/icones/signout1.png", QSize(), QIcon.Mode.Normal, QIcon.State.On)
        self.sign_2.setIcon(icon11)
        self.sign_2.setIconSize(QSize(100, 60))
        self.sign_2.setCheckable(True)

        self.verticalLayout_6.addWidget(self.sign_2)


        self.verticalLayout_9.addLayout(self.verticalLayout_6)


        self.gridLayout.addWidget(self.icon_txt_widget, 0, 1, 1, 1)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.header_widget = QWidget(self.layoutWidget)
        self.header_widget.setObjectName(u"header_widget")
        self.horizontalLayout_5 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton = QPushButton(self.header_widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"BOrDER:none;")
        icon12 = QIcon()
        icon12.addFile(u":/icones/menu.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon12)
        self.pushButton.setIconSize(QSize(29, 35))
        self.pushButton.setCheckable(True)

        self.horizontalLayout_4.addWidget(self.pushButton)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 25, -1, 25)
        self.label = QLabel(self.header_widget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout_11.addWidget(self.label)

        self.label_5 = QLabel(self.header_widget)
        self.label_5.setObjectName(u"label_5")
        font2 = QFont()
        font2.setPointSize(10)
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(116, 116, 116);")

        self.verticalLayout_11.addWidget(self.label_5)


        self.horizontalLayout_4.addLayout(self.verticalLayout_11)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalSpacer_3 = QSpacerItem(364, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, 25, -1)
        self.lineEdit = QLineEdit(self.header_widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 31))
        self.lineEdit.setMaximumSize(QSize(16777215, 31))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"  padding-left:20px;\n"
"  border:1px solid gray;\n"
"  border-radius:10px;\n"
"}")
        self.lineEdit.setReadOnly(False)

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.label_6 = QLabel(self.header_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(40, 40))
        self.label_6.setPixmap(QPixmap(u":/icones/profile.png"))
        self.label_6.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.label_6)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_3)


        self.verticalLayout_12.addWidget(self.header_widget)

        self.main_screen_widget = QWidget(self.layoutWidget)
        self.main_screen_widget.setObjectName(u"main_screen_widget")
        self.main_screen_widget.setMinimumSize(QSize(920, 581))
        self.main_screen_widget.setMaximumSize(QSize(831, 581))
        self.main_screen_widget.setStyleSheet(u"")
        self.stackedWidget = QStackedWidget(self.main_screen_widget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(-1, -1, 911, 571))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(340, 210, 211, 51))
        self.label_7.setFont(font)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.label_8 = QLabel(self.page_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(400, 260, 221, 51))
        self.label_8.setFont(font)
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.label_9 = QLabel(self.page_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(10, 0, 251, 51))
        font3 = QFont()
        font3.setFamilies([u"Century Gothic"])
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_9.setFont(font3)
        self.layoutWidget_2 = QWidget(self.page_3)
        self.layoutWidget_2.setObjectName(u"layoutWidget_2")
        self.layoutWidget_2.setGeometry(QRect(20, 50, 168, 69))
        self.verticalLayout_13 = QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.date = QLabel(self.layoutWidget_2)
        self.date.setObjectName(u"date")
        font4 = QFont()
        font4.setFamilies([u"Century Gothic"])
        font4.setPointSize(12)
        self.date.setFont(font4)

        self.verticalLayout_13.addWidget(self.date)

        self.pointage_dob_dateEdit_2 = QDateEdit(self.layoutWidget_2)
        self.pointage_dob_dateEdit_2.setObjectName(u"pointage_dob_dateEdit_2")
        self.pointage_dob_dateEdit_2.setStyleSheet(u"QDateEdit{\n"
"   border: 1px solid gray;\n"
"  border-radius: 6px;\n"
"  padding-left: 15px;\n"
"  height: 30px;\n"
"}")

        self.verticalLayout_13.addWidget(self.pointage_dob_dateEdit_2)

        self.employe_info_table_2 = QTableWidget(self.page_3)
        if (self.employe_info_table_2.columnCount() < 4):
            self.employe_info_table_2.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.employe_info_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.employe_info_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.employe_info_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.employe_info_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.employe_info_table_2.setObjectName(u"employe_info_table_2")
        self.employe_info_table_2.setGeometry(QRect(10, 150, 950, 361))
        self.employe_info_table_2.setStyleSheet(u"/* Styles pour les sections d'en-t\u00eate */\n"
"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #555;\n"
"    padding: 4px; /* Espace autour du texte des en-t\u00eates */\n"
"}\n"
"\n"
"/* Styles pour le widget de table */\n"
"QTableWidget {\n"
"    alternate-background-color: #B0EDFB; /* Couleur de fond pour les lignes altern\u00e9es */\n"
"    background-color: #F4F9FA; /* Couleur de fond pour le tableau */\n"
"    border: 1px solid #ddd; /* Bordure autour du tableau */\n"
"}\n"
"\n"
"/* Styles pour les \u00e9l\u00e9ments des cellules */\n"
"QTableWidget QTableWidgetItem {\n"
"    padding-left: 10px; /* Espace \u00e0 gauche du texte des cellules */\n"
"    padding-right: 10px; /* Espace \u00e0 droite du texte des cellules */\n"
"}\n"
"\n"
"/* Espacement des lignes et colonnes */\n"
"QTableWidget::item {\n"
"    padding: 0px;\n"
"    border-right: 1px solid #ddd; /* Bordure droite des cellules pour s\u00e9parer les colonnes *"
                        "/\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    border-right: 1px solid #ddd; /* Bordure droite des en-t\u00eates pour s\u00e9parer les colonnes */\n"
"}\n"
"")
        self.employe_info_table_2.setAlternatingRowColors(True)
        self.layoutWidget_3 = QWidget(self.page_3)
        self.layoutWidget_3.setObjectName(u"layoutWidget_3")
        self.layoutWidget_3.setGeometry(QRect(290, 40, 611, 43))
        self.horizontalLayout_8 = QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.poin_select_services_2 = QComboBox(self.layoutWidget_3)
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.addItem("")
        self.poin_select_services_2.setObjectName(u"poin_select_services_2")
        self.poin_select_services_2.setMinimumSize(QSize(150, 0))
        self.poin_select_services_2.setStyleSheet(u"QComboBox{\n"
"     border: 2px solid white;\n"
"     border-radius: 8px;\n"
"     padding :1px  18px  1px  3px ;\n"
"     background-color:black;\n"
"	 color: rgb(255, 255, 255);\n"
"     height: 35px;\n"
"     padding-left: 15px;\n"
"     font-weight:bold;\n"
"     selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_8.addWidget(self.poin_select_services_2)

        self.poin_search_employe_2 = QLineEdit(self.layoutWidget_3)
        self.poin_search_employe_2.setObjectName(u"poin_search_employe_2")
        self.poin_search_employe_2.setMinimumSize(QSize(0, 38))
        self.poin_search_employe_2.setMaximumSize(QSize(16777215, 38))
        self.poin_search_employe_2.setStyleSheet(u"QLineEdit{\n"
"  padding-left:20px;\n"
"  border:1px solid gray;\n"
"  border-radius:10px;\n"
"}")
        self.poin_search_employe_2.setReadOnly(False)

        self.horizontalLayout_8.addWidget(self.poin_search_employe_2)

        self.save_pointage_btn = QPushButton(self.page_3)
        self.save_pointage_btn.setObjectName(u"save_pointage_btn")
        self.save_pointage_btn.setGeometry(QRect(800, 510, 112, 41))
        self.save_pointage_btn.setMinimumSize(QSize(0, 41))
        self.save_pointage_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#34D481;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"}")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.label_10 = QLabel(self.page_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(10, 10, 551, 51))
        self.label_10.setFont(font)
        self.layoutWidget_4 = QWidget(self.page_4)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(300, 80, 611, 45))
        self.horizontalLayout_9 = QHBoxLayout(self.layoutWidget_4)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.select_month_2 = QComboBox(self.layoutWidget_4)
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.addItem("")
        self.select_month_2.setObjectName(u"select_month_2")
        self.select_month_2.setMinimumSize(QSize(150, 0))
        self.select_month_2.setStyleSheet(u"QComboBox{\n"
"     border: 2px solid white;\n"
"     border-radius: 8px;\n"
"     padding :1px  18px  1px  3px ;\n"
"     background-color:black;\n"
"	 color: rgb(255, 255, 255);\n"
"     height: 35px;\n"
"     padding-left: 15px;\n"
"     font-weight:bold;\n"
"     selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_9.addWidget(self.select_month_2)

        self.select_year_2 = QComboBox(self.layoutWidget_4)
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.addItem("")
        self.select_year_2.setObjectName(u"select_year_2")
        self.select_year_2.setMinimumSize(QSize(150, 0))
        self.select_year_2.setStyleSheet(u"QComboBox{\n"
"     border: 2px solid white;\n"
"     border-radius: 8px;\n"
"     padding :1px  18px  1px  3px ;\n"
"     background-color:black;\n"
"	 color: rgb(255, 255, 255);\n"
"     height: 35px;\n"
"     padding-left: 15px;\n"
"     font-weight:bold;\n"
"     selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_9.addWidget(self.select_year_2)

        self.search_employe_histo = QLineEdit(self.layoutWidget_4)
        self.search_employe_histo.setObjectName(u"search_employe_histo")
        self.search_employe_histo.setMinimumSize(QSize(0, 38))
        self.search_employe_histo.setMaximumSize(QSize(16777215, 38))
        self.search_employe_histo.setStyleSheet(u"QLineEdit{\n"
"  padding-left:20px;\n"
"  border:1px solid gray;\n"
"  border-radius:10px;\n"
"}")
        self.search_employe_histo.setReadOnly(False)

        self.horizontalLayout_9.addWidget(self.search_employe_histo)

        self.historique_table_info = QTableWidget(self.page_4)
        if (self.historique_table_info.columnCount() < 3):
            self.historique_table_info.setColumnCount(3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.historique_table_info.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.historique_table_info.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.historique_table_info.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        self.historique_table_info.setObjectName(u"historique_table_info")
        self.historique_table_info.setGeometry(QRect(10, 150, 601, 361))
        self.historique_table_info.setStyleSheet(u"/* Styles pour les sections d'en-t\u00eate */\n"
"QHeaderView::section {\n"
"    font-weight: bold;\n"
"    background-color: black;\n"
"    color: white;\n"
"    border: 1px solid #555;\n"
"    padding: 6px; /* Espace autour du texte des en-t\u00eates */\n"
"}\n"
"\n"
"/* Styles pour le widget de table */\n"
"QTableWidget {\n"
"    alternate-background-color: #B0EDFB; /* Couleur de fond pour les lignes altern\u00e9es */\n"
"    background-color: #F4F9FA; /* Couleur de fond pour le tableau */\n"
"    border: 1px solid #ddd; /* Bordure autour du tableau */\n"
"}\n"
"\n"
"/* Styles pour les \u00e9l\u00e9ments des cellules */\n"
"QTableWidget QTableWidgetItem {\n"
"    padding-left: 10px; /* Espace \u00e0 gauche du texte des cellules */\n"
"    padding-right: 10px; /* Espace \u00e0 droite du texte des cellules */\n"
"}\n"
"\n"
"/* Espacement des lignes et colonnes */\n"
"QTableWidget::item {\n"
"    padding: 0px;\n"
"    border-right: 1px solid #ddd; /* Bordure droite des cellules pour s\u00e9parer les colonnes *"
                        "/\n"
"}\n"
"\n"
"QTableWidget QHeaderView::section {\n"
"    border-right: 1px solid #ddd; /* Bordure droite des en-t\u00eates pour s\u00e9parer les colonnes */\n"
"}\n"
"")
        self.historique_table_info.setAlternatingRowColors(True)
        self.layoutWidget_5 = QWidget(self.page_4)
        self.layoutWidget_5.setObjectName(u"layoutWidget_5")
        self.layoutWidget_5.setGeometry(QRect(620, 150, 291, 43))
        self.horizontalLayout_10 = QHBoxLayout(self.layoutWidget_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.ExportExcel_btn_2 = QPushButton(self.layoutWidget_5)
        self.ExportExcel_btn_2.setObjectName(u"ExportExcel_btn_2")
        self.ExportExcel_btn_2.setMinimumSize(QSize(0, 41))
        self.ExportExcel_btn_2.setStyleSheet(u"QPushButton{\n"
"  background-color:#34D481;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icones/excel.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExportExcel_btn_2.setIcon(icon13)

        self.horizontalLayout_10.addWidget(self.ExportExcel_btn_2)

        self.ExportPdf_btn_2 = QPushButton(self.layoutWidget_5)
        self.ExportPdf_btn_2.setObjectName(u"ExportPdf_btn_2")
        self.ExportPdf_btn_2.setMinimumSize(QSize(0, 41))
        self.ExportPdf_btn_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 62, 62);\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/icones/pdf (1).png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.ExportPdf_btn_2.setIcon(icon14)

        self.horizontalLayout_10.addWidget(self.ExportPdf_btn_2)

        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.label_11 = QLabel(self.page_5)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 0, 181, 51))
        self.label_11.setFont(font3)
        self.label_14 = QLabel(self.page_5)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(10, 40, 281, 41))
        font5 = QFont()
        font5.setFamilies([u"Century Gothic"])
        font5.setPointSize(10)
        font5.setBold(False)
        self.label_14.setFont(font5)
        self.employe_info_table = QTableWidget(self.page_5)
        if (self.employe_info_table.columnCount() < 9):
            self.employe_info_table.setColumnCount(9)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(7, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.employe_info_table.setHorizontalHeaderItem(8, __qtablewidgetitem15)
        self.employe_info_table.setObjectName(u"employe_info_table")
        self.employe_info_table.setGeometry(QRect(10, 180, 950, 381))
        self.employe_info_table.setStyleSheet(u"QHeaderView::section{\n"
"  font-weight:bold;\n"
"	background-color: black ;\n"
"  color:white;\n"
"   \n"
"}\n"
"QTableWidget:{\n"
"     alternate-background-color:#B0EDFB;\n"
"     background-color: #F4F9FA ;\n"
"}")
        self.employe_info_table.setAlternatingRowColors(True)
        self.layoutWidget1 = QWidget(self.page_5)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(10, 70, 451, 43))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.addemployee_btn = QPushButton(self.layoutWidget1)
        self.addemployee_btn.setObjectName(u"addemployee_btn")
        self.addemployee_btn.setMinimumSize(QSize(0, 41))
        self.addemployee_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(0, 0, 0);\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12\n"
"px;\n"
"\n"
"}")
        icon15 = QIcon()
        icon15.addFile(u":/icones/add student.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addemployee_btn.setIcon(icon15)

        self.horizontalLayout_6.addWidget(self.addemployee_btn)

        self.ExportExcel_btn = QPushButton(self.layoutWidget1)
        self.ExportExcel_btn.setObjectName(u"ExportExcel_btn")
        self.ExportExcel_btn.setMinimumSize(QSize(0, 41))
        self.ExportExcel_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#34D481;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"\n"
"}")
        self.ExportExcel_btn.setIcon(icon13)

        self.horizontalLayout_6.addWidget(self.ExportExcel_btn)

        self.ExportPdf_btn = QPushButton(self.layoutWidget1)
        self.ExportPdf_btn.setObjectName(u"ExportPdf_btn")
        self.ExportPdf_btn.setMinimumSize(QSize(0, 41))
        self.ExportPdf_btn.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 62, 62);\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:12px;\n"
"\n"
"}")
        self.ExportPdf_btn.setIcon(icon14)

        self.horizontalLayout_6.addWidget(self.ExportPdf_btn)

        self.layoutWidget2 = QWidget(self.page_5)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 120, 611, 43))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.select_gender = QComboBox(self.layoutWidget2)
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.addItem("")
        self.select_gender.setObjectName(u"select_gender")
        self.select_gender.setMinimumSize(QSize(150, 0))
        self.select_gender.setStyleSheet(u"QComboBox{\n"
"     border: 2px solid white;\n"
"     border-radius: 8px;\n"
"     padding :1px  18px  1px  3px ;\n"
"     background-color:black;\n"
"	 color: rgb(255, 255, 255);\n"
"     height: 35px;\n"
"     padding-left: 15px;\n"
"     font-weight:bold;\n"
"     selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_gender)

        self.select_services = QComboBox(self.layoutWidget2)
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.addItem("")
        self.select_services.setObjectName(u"select_services")
        self.select_services.setMinimumSize(QSize(150, 0))
        self.select_services.setStyleSheet(u"QComboBox{\n"
"     border: 2px solid white;\n"
"     border-radius: 8px;\n"
"     padding :1px  18px  1px  3px ;\n"
"     background-color:black;\n"
"	 color: rgb(255, 255, 255);\n"
"     height: 35px;\n"
"     padding-left: 15px;\n"
"     font-weight:bold;\n"
"     selection-background-color: #2980B9;\n"
"}")

        self.horizontalLayout_7.addWidget(self.select_services)

        self.search_employe = QLineEdit(self.layoutWidget2)
        self.search_employe.setObjectName(u"search_employe")
        self.search_employe.setMinimumSize(QSize(0, 38))
        self.search_employe.setMaximumSize(QSize(16777215, 38))
        self.search_employe.setStyleSheet(u"QLineEdit{\n"
"  padding-left:20px;\n"
"  border:1px solid gray;\n"
"  border-radius:10px;\n"
"}")
        self.search_employe.setReadOnly(False)

        self.horizontalLayout_7.addWidget(self.search_employe)

        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_12 = QLabel(self.page_6)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(250, 240, 211, 51))
        self.label_12.setFont(font)
        self.stackedWidget.addWidget(self.page_6)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_13 = QLabel(self.page_7)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(260, 260, 211, 51))
        self.label_13.setFont(font)
        self.stackedWidget.addWidget(self.page_7)

        self.verticalLayout_12.addWidget(self.main_screen_widget)


        self.gridLayout.addLayout(self.verticalLayout_12, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pointage_2.toggled.connect(self.pointage_dropdown.setHidden)
        self.employe_2.toggled.connect(self.employee_dropdown.setHidden)
        self.dashboard_2.toggled.connect(self.dashboard_1.setChecked)
        self.institution_2.toggled.connect(self.institution_1.setChecked)
        self.pointage_2.toggled.connect(self.pointage_1.setChecked)
        self.employe_2.toggled.connect(self.employe_1.setChecked)
        self.setting_2.toggled.connect(self.setting_1.setChecked)
        self.sign_2.toggled.connect(self.sign_1.setChecked)
        self.sign_2.toggled.connect(MainWindow.close)
        self.sign_1.toggled.connect(MainWindow.close)
        self.pushButton.toggled.connect(self.icon_txt_widget.setHidden)
        self.pushButton.toggled.connect(self.icon_only_widget.setVisible)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.dashboard_1.setText("")
        self.institution_1.setText("")
        self.pointage_1.setText("")
        self.employe_1.setText("")
        self.setting_1.setText("")
        self.sign_1.setText("")
        self.label_2.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Valtronic", None))
        self.dashboard_2.setText("")
        self.institution_2.setText("")
        self.pointage_2.setText("")
        self.pointage.setText(QCoreApplication.translate("MainWindow", u"Pointage", None))
        self.historique.setText(QCoreApplication.translate("MainWindow", u"Historique", None))
        self.employe_2.setText("")
        self.employes.setText(QCoreApplication.translate("MainWindow", u"Employes", None))
        self.administrateurs.setText(QCoreApplication.translate("MainWindow", u"Administrateurs", None))
        self.setting_2.setText("")
        self.sign_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Hello,Mark", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"welcome to your page ", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here ...", None))
        self.label_6.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"DASHBOARD", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"INSTITUTION", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Liste de Pointage", None))
        self.date.setText(QCoreApplication.translate("MainWindow", u"Date ", None))
        ___qtablewidgetitem = self.employe_info_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem1 = self.employe_info_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Services", None));
        ___qtablewidgetitem2 = self.employe_info_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Presence", None));
        ___qtablewidgetitem3 = self.employe_info_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Action", None));
        self.poin_select_services_2.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT SERVICE", None))
        self.poin_select_services_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Preci-Dip", None))
        self.poin_select_services_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Cellduc", None))
        self.poin_select_services_2.setItemText(3, QCoreApplication.translate("MainWindow", u"CMS", None))
        self.poin_select_services_2.setItemText(4, QCoreApplication.translate("MainWindow", u"4Energy", None))
        self.poin_select_services_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Qualite", None))
        self.poin_select_services_2.setItemText(6, QCoreApplication.translate("MainWindow", u"CMS", None))
        self.poin_select_services_2.setItemText(7, "")

        self.poin_search_employe_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search employe ...", None))
        self.save_pointage_btn.setText(QCoreApplication.translate("MainWindow", u"ENREGISTRER", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"BILAN DES HEURES TRAVAILLEES DURANT ", None))
        self.select_month_2.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT MONTH", None))
        self.select_month_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Janvier", None))
        self.select_month_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Fevrier", None))
        self.select_month_2.setItemText(3, QCoreApplication.translate("MainWindow", u"Mars", None))
        self.select_month_2.setItemText(4, QCoreApplication.translate("MainWindow", u"Avril", None))
        self.select_month_2.setItemText(5, QCoreApplication.translate("MainWindow", u"Mai", None))
        self.select_month_2.setItemText(6, QCoreApplication.translate("MainWindow", u"Juin", None))
        self.select_month_2.setItemText(7, QCoreApplication.translate("MainWindow", u"Juillet", None))
        self.select_month_2.setItemText(8, QCoreApplication.translate("MainWindow", u"Ao\u00fbt", None))
        self.select_month_2.setItemText(9, QCoreApplication.translate("MainWindow", u"Septembre", None))
        self.select_month_2.setItemText(10, QCoreApplication.translate("MainWindow", u"Octobre", None))
        self.select_month_2.setItemText(11, QCoreApplication.translate("MainWindow", u"Novembre", None))
        self.select_month_2.setItemText(12, QCoreApplication.translate("MainWindow", u"Decembre", None))

        self.select_year_2.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT YEAR", None))
        self.select_year_2.setItemText(1, QCoreApplication.translate("MainWindow", u"2020", None))
        self.select_year_2.setItemText(2, QCoreApplication.translate("MainWindow", u"2021", None))
        self.select_year_2.setItemText(3, QCoreApplication.translate("MainWindow", u"2022", None))
        self.select_year_2.setItemText(4, QCoreApplication.translate("MainWindow", u"2023", None))
        self.select_year_2.setItemText(5, QCoreApplication.translate("MainWindow", u"2024", None))
        self.select_year_2.setItemText(6, QCoreApplication.translate("MainWindow", u"2025", None))
        self.select_year_2.setItemText(7, QCoreApplication.translate("MainWindow", u"2026", None))
        self.select_year_2.setItemText(8, QCoreApplication.translate("MainWindow", u"2027", None))
        self.select_year_2.setItemText(9, QCoreApplication.translate("MainWindow", u"2028", None))
        self.select_year_2.setItemText(10, QCoreApplication.translate("MainWindow", u"2029", None))
        self.select_year_2.setItemText(11, QCoreApplication.translate("MainWindow", u"2030", None))
        self.select_year_2.setItemText(12, "")

        self.search_employe_histo.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search employe ...", None))
        ___qtablewidgetitem4 = self.historique_table_info.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem5 = self.historique_table_info.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Service", None));
        ___qtablewidgetitem6 = self.historique_table_info.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Totale des heures ", None));
        self.ExportExcel_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export To Excel ", None))
        self.ExportPdf_btn_2.setText(QCoreApplication.translate("MainWindow", u"Export To PDF", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Employe Info", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Welcome To The Employe Information Page", None))
        ___qtablewidgetitem7 = self.employe_info_table.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Nom", None));
        ___qtablewidgetitem8 = self.employe_info_table.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Genre", None));
        ___qtablewidgetitem9 = self.employe_info_table.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Services", None));
        ___qtablewidgetitem10 = self.employe_info_table.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Birthday", None));
        ___qtablewidgetitem11 = self.employe_info_table.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Age", None));
        ___qtablewidgetitem12 = self.employe_info_table.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Adresse", None));
        ___qtablewidgetitem13 = self.employe_info_table.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Phone", None));
        ___qtablewidgetitem14 = self.employe_info_table.horizontalHeaderItem(7)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem15 = self.employe_info_table.horizontalHeaderItem(8)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Actions", None));
        self.addemployee_btn.setText(QCoreApplication.translate("MainWindow", u"Ajouter", None))
        self.ExportExcel_btn.setText(QCoreApplication.translate("MainWindow", u"Export To Excel ", None))
        self.ExportPdf_btn.setText(QCoreApplication.translate("MainWindow", u"Export To PDF", None))
        self.select_gender.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT GENDER", None))
        self.select_gender.setItemText(1, QCoreApplication.translate("MainWindow", u"Male", None))
        self.select_gender.setItemText(2, QCoreApplication.translate("MainWindow", u"Female", None))

        self.select_services.setItemText(0, QCoreApplication.translate("MainWindow", u"SELECT SERVICE", None))
        self.select_services.setItemText(1, QCoreApplication.translate("MainWindow", u"Preci-Dip", None))
        self.select_services.setItemText(2, QCoreApplication.translate("MainWindow", u"Cellduc", None))
        self.select_services.setItemText(3, QCoreApplication.translate("MainWindow", u"CMS", None))
        self.select_services.setItemText(4, QCoreApplication.translate("MainWindow", u"4Energy", None))
        self.select_services.setItemText(5, QCoreApplication.translate("MainWindow", u"Qualite", None))
        self.select_services.setItemText(6, QCoreApplication.translate("MainWindow", u"CMS", None))
        self.select_services.setItemText(7, "")

        self.search_employe.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search employe ...", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"ADMINISTRATEURS", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"setting", None))
    # retranslateUi


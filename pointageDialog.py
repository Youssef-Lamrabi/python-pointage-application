# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pointageDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon, QImage, QKeySequence, 
    QLinearGradient, QPainter, QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSizePolicy, 
    QVBoxLayout, QWidget, QMessageBox)
from pymysql import OperationalError
import pymysql

class Ui_PointageDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()
        self.db_connection = self.create_connection()
        self.populate_employee_combobox()

    def setupUi(self):
        self.resize(548, 371)
        self.setStyleSheet(u"QDialog{\n"
" \n"
"	background-color:white;\n"
"}\n"
"\n"
"QLineEdit{\n"
"  border: 1px solid gray;\n"
"  border-radius: 6px;\n"
"  padding-left: 15px;\n"
"  height: 35px;\n"
"}\n"
"\n"
"QDateEdit{\n"
"   border: 1px solid gray;\n"
"  border-radius: 6px;\n"
"  padding-left: 15px;\n"
"  height: 30px;\n"
"  \n"
"}\n"
"QComboBox{\n"
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
        self.line = QFrame(self)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 60, 551, 20))
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)
        self.label = QLabel(self)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 241, 41))
        font = QFont()
        font.setFamilies([u"Century Gothic"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.layoutWidget = QWidget(self)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 90, 521, 171))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.employee_comboBox = QComboBox(self.layoutWidget)
        self.employee_comboBox.setObjectName(u"employee_comboBox")

        self.verticalLayout_5.addWidget(self.employee_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.poi_services_comboBox = QComboBox(self.layoutWidget)
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.addItem("")
        self.poi_services_comboBox.setObjectName(u"poi_services_comboBox")

        self.verticalLayout_6.addWidget(self.poi_services_comboBox)

        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.poi_dob_dateEdit = QDateEdit(self.layoutWidget)
        self.poi_dob_dateEdit.setObjectName(u"poi_dob_dateEdit")

        self.verticalLayout_7.addWidget(self.poi_dob_dateEdit)

        self.horizontalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        font2 = QFont()
        font2.setFamilies([u"Century Gothic"])
        font2.setPointSize(16)
        self.label_4.setFont(font2)

        self.verticalLayout_3.addWidget(self.label_4)

        self.heuresTravailles_lineEdit = QLineEdit(self.layoutWidget)
        self.heuresTravailles_lineEdit.setObjectName(u"heuresTravailles_lineEdit")
        self.heuresTravailles_lineEdit.setMinimumSize(QSize(0, 35))
        self.heuresTravailles_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.heuresTravailles_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.heuresTravailles_lineEdit)

        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 310, 231, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.saveemployee_btn = QPushButton(self.layoutWidget1)
        self.saveemployee_btn.setObjectName(u"saveemployee_btn")
        self.saveemployee_btn.setMinimumSize(QSize(0, 41))
        self.saveemployee_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#34D481;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.saveemployee_btn)

        self.cancle_btn = QPushButton(self.layoutWidget1)
        self.cancle_btn.setObjectName(u"cancle_btn")
        self.cancle_btn.setMinimumSize(QSize(0, 41))
        self.cancle_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#585858;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.cancle_btn)

        self.retranslateUi(self)
        self.saveemployee_btn.clicked.connect(self.add_pointage)
        self.cancle_btn.clicked.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    
    def add_pointage(self):
        self.insert_pointage_employee()
        self.accept()


    def retranslateUi(self, EmployesDialog):
        EmployesDialog.setWindowTitle(QCoreApplication.translate("EmployesDialog", u"Pointage Dialog", None))
        self.label.setText(QCoreApplication.translate("EmployesDialog", u"Pointage", None))
        self.label_6.setText(QCoreApplication.translate("EmployesDialog", u"Employee", None))
        self.label_7.setText(QCoreApplication.translate("EmployesDialog", u"Services ", None))
        self.poi_services_comboBox.setItemText(0, QCoreApplication.translate("EmployesDialog", u"Preci-Dip", None))
        self.poi_services_comboBox.setItemText(1, QCoreApplication.translate("EmployesDialog", u"Cellduc", None))
        self.poi_services_comboBox.setItemText(2, QCoreApplication.translate("EmployesDialog", u"CMS", None))
        self.poi_services_comboBox.setItemText(3, QCoreApplication.translate("EmployesDialog", u"4Energy", None))
        self.poi_services_comboBox.setItemText(4, QCoreApplication.translate("EmployesDialog", u"Qualite", None))
        self.poi_services_comboBox.setItemText(5, QCoreApplication.translate("EmployesDialog", u"CMS", None))
        self.poi_services_comboBox.setItemText(6, "")

        self.label_8.setText(QCoreApplication.translate("EmployesDialog", u"Date ", None))
        self.label_4.setText(QCoreApplication.translate("EmployesDialog", u"heure", None))
        self.saveemployee_btn.setText(QCoreApplication.translate("EmployesDialog", u"Ajouter", None))
        self.cancle_btn.setText(QCoreApplication.translate("EmployesDialog", u"Annuler", None))

    def create_connection(self):
        host_name = "localhost"
        user_name = "root"
        mypassword = "root"
        database_name = "gestion_pointage"

        try:
            mydb = pymysql.connect(
                host=host_name,
                user=user_name,
                password=mypassword,
                database=database_name
            )
            print("Connexion réussie et base de données prête")
            return mydb
        except OperationalError as e:
            print(f"Erreur lors de la connexion à la base de données : {e}")
            QMessageBox.critical(self, "Erreur de connexion", f"Impossible de se connecter à la base de données : {e}")
            return None

    def insert_pointage_employee(self):
        employe_id = self.employee_comboBox.currentData()  # Récupération de l'ID employé
        date = self.poi_dob_dateEdit.date().toString("yyyy-MM-dd")  # Récupération de la date
        heures_travaillees = self.heuresTravailles_lineEdit.text()  # Récupération des heures travaillées

        # Validation des champs
        if not employe_id or not heures_travaillees:
            QMessageBox.warning(self, "Données manquantes", "Veuillez remplir tous les champs.")
            return

        # Validation des heures travaillées comme nombre
        try:
            heures_travaillees = float(heures_travaillees)
        except ValueError:
            QMessageBox.warning(self, "Erreur de saisie", "Les heures travaillées doivent être un nombre.")
            return

        # Insertion dans la base de données si la connexion est valide
        if self.db_connection:
            try:
                with self.db_connection.cursor() as cursor:
                    # Requête SQL corrigée
                    insert_query = """
                        INSERT INTO pointage_table (employe_id, date, heures_travaillees) 
                        VALUES (%s, %s, %s)
                    """
                    cursor.execute(insert_query, (employe_id, date, heures_travaillees))
                self.db_connection.commit()
                self.show_inserted_message()
            except pymysql.MySQLError as e:
                QMessageBox.critical(self, "Erreur de base de données", f"Erreur lors de l'insertion du pointage : {e}")
        else:
            QMessageBox.critical(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")

    def populate_employee_combobox(self):
        if self.db_connection:
            try:
                with self.db_connection.cursor() as cursor:
                    cursor.execute("SELECT employe_id, names FROM employe_table")
                    employes = cursor.fetchall()

                self.employee_comboBox.clear()
                for employe_id, employe_name in employes:
                    self.employee_comboBox.addItem(employe_name, employe_id)
            except pymysql.MySQLError as e:
                QMessageBox.warning(self, "Erreur de chargement", f"Impossible de charger la liste des employés : {e}")
        else:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")

    def show_inserted_message(self):
        nom_employe = self.employee_comboBox.currentText() or "Un employé"
        QMessageBox.information(self, "Succès", f"{nom_employe} a été pointé avec succès.")
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'EmployeDialogue.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from random import randint
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget,QMessageBox)

import mysql.connector
from pymysql import OperationalError
from datetime import datetime

import pymysql
class Ui_EmployesDialog(QDialog):
    def __init__(self,parent=None):
        super().__init__(parent)
            
        self.resize(548, 520)
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
        self.layoutWidget.setGeometry(QRect(10, 90, 521, 351))
        self.verticalLayout_8 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Century Gothic"])
        font1.setPointSize(12)
        self.label_2.setFont(font1)

        self.verticalLayout.addWidget(self.label_2)

        self.name_lineEdit = QLineEdit(self.layoutWidget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(0, 35))
        self.name_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.name_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout.addWidget(self.name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.gender_comboBox = QComboBox(self.layoutWidget)
        self.gender_comboBox.addItem("")
        self.gender_comboBox.addItem("")
        self.gender_comboBox.setObjectName(u"gender_comboBox")

        self.verticalLayout_5.addWidget(self.gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.services_comboBox = QComboBox(self.layoutWidget)
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.addItem("")
        self.services_comboBox.setObjectName(u"services_comboBox")

        self.verticalLayout_6.addWidget(self.services_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.dob_dateEdit = QDateEdit(self.layoutWidget)
        self.dob_dateEdit.setObjectName(u"dob_dateEdit")

        self.verticalLayout_7.addWidget(self.dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.adresse_lineEdit = QLineEdit(self.layoutWidget)
        self.adresse_lineEdit.setObjectName(u"adresse_lineEdit")
        self.adresse_lineEdit.setMinimumSize(QSize(0, 35))
        self.adresse_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.adresse_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.adresse_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.phone_lineEdit = QLineEdit(self.layoutWidget)
        self.phone_lineEdit.setObjectName(u"phone_lineEdit")
        self.phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.phone_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.phone_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.phone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.email_lineEdit = QLineEdit(self.layoutWidget)
        self.email_lineEdit.setObjectName(u"email_lineEdit")
        self.email_lineEdit.setMinimumSize(QSize(0, 35))
        self.email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.email_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 460, 231, 43))
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

        QMetaObject.connectSlotsByName(self)
    # setupUi
        self.saveemployee_btn.clicked.connect(self.add_employe)
        self.cancle_btn.clicked.connect(self.close)

    def retranslateUi(self, EmployesDialog):
        EmployesDialog.setWindowTitle(QCoreApplication.translate("EmployesDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("EmployesDialog", u"Ajouter Employee", None))
        self.label_2.setText(QCoreApplication.translate("EmployesDialog", u"Nom Complet ", None))
        self.label_6.setText(QCoreApplication.translate("EmployesDialog", u"Genre", None))
        self.gender_comboBox.setItemText(0, QCoreApplication.translate("EmployesDialog", u"Male", None))
        self.gender_comboBox.setItemText(1, QCoreApplication.translate("EmployesDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("EmployesDialog", u"Services ", None))
        self.services_comboBox.setItemText(0, QCoreApplication.translate("EmployesDialog", u"Preci-Dip", None))
        self.services_comboBox.setItemText(1, QCoreApplication.translate("EmployesDialog", u"Cellduc", None))
        self.services_comboBox.setItemText(2, QCoreApplication.translate("EmployesDialog", u"CMS", None))
        self.services_comboBox.setItemText(3, QCoreApplication.translate("EmployesDialog", u"4Energy", None))
        self.services_comboBox.setItemText(4, QCoreApplication.translate("EmployesDialog", u"Qualite", None))
        self.services_comboBox.setItemText(5, QCoreApplication.translate("EmployesDialog", u"CMS", None))
        self.services_comboBox.setItemText(6, "")

        self.label_8.setText(QCoreApplication.translate("EmployesDialog", u"Date De Naissance", None))
        self.label_3.setText(QCoreApplication.translate("EmployesDialog", u"Adresse", None))
        self.label_4.setText(QCoreApplication.translate("EmployesDialog", u"Telephone", None))
        self.label_5.setText(QCoreApplication.translate("EmployesDialog", u"Email", None))
        self.saveemployee_btn.setText(QCoreApplication.translate("EmployesDialog", u"Ajouter", None))
        self.cancle_btn.setText(QCoreApplication.translate("EmployesDialog", u"Annuler", None))
        

        
    def create_connection(self):
            """Créer une connexion à la base de données MySQL et préparer la base de données"""
            host_name = "localhost"
            user_name = "root"
            mypassword = "root"
            database_name = "gestion_pointage"

            try:
                # Connexion au serveur MySQL
                self.mydb = pymysql.connect(
                    host=host_name,
                    user=user_name,
                    password=mypassword
                )

                # Création de la base de données si elle n'existe pas
                cursor = self.mydb.cursor()
                cursor.execute(f'CREATE DATABASE IF NOT EXISTS {database_name}')
                cursor.close()

                # Connexion à la base de données spécifique
                self.mydb = pymysql.connect(
                    host=host_name,
                    user=user_name,
                    password=mypassword,
                    database=database_name
                )

                print("Connexion réussie et base de données prête")
                return self.mydb

            except OperationalError as e:
                print(f"Erreur lors de la connexion ou de la création de la base de données : {e}")
                return None
    
    def insert_new_employe(self):
        try:
            connection = self.create_connection()
            if connection is None:
                return
            cursor = connection.cursor()
            
            gender = self.gender_comboBox.currentText()
            birthday = self.handleDateChane()
            birth_date = self.dob_dateEdit.date()
            age = self.calculate_age(birth_date)
            
            # Liste des valeurs à insérer dans la table employe_table
            self.new_employe = [
                self.name_lineEdit.text(),
                gender,
                self.services_comboBox.currentText(),
                birthday,
                age,
                self.adresse_lineEdit.text(),
                self.phone_lineEdit.text(),
                self.email_lineEdit.text()
            ]
            
            insert_employe_query = """
            INSERT INTO employe_table (names, gender, services, birthday, age, address, phone, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            
            cursor.execute(insert_employe_query, self.new_employe)
            self.show_inserted_message()
            connection.commit()
            cursor.close()
            connection.close()
            
        except pymysql.MySQLError as err:
            print(f"Error: {err}")

        
    def generate_employeId(self, gender):
        cursor = self.create_connection().cursor()
        
        if gender == 'Male':
            id_start_value = '24/U/M'
        else:
            id_start_value = '24/U/F'
        
        random_value = self.generate_randomNumber()
        employe_id = id_start_value + random_value
        
        cursor.execute("SELECT employe_id FROM employe_table WHERE employe_id=%s", (employe_id,))
        existing_id = cursor.fetchone()
        
        if not existing_id:
            return employe_id
        else:
            # Handle the case where the ID already exists (perhaps by retrying)
            return self.generate_employeId(gender)

        
    def generate_randomNumber(self):
        
        number=randint(1,1000)
        random_number=f"{number:04d}"
        return random_number
        
    def handleDateChane(self):
        
        selected_date=self.dob_dateEdit.date()
        self.date_string=selected_date.toString(Qt.ISODate)
        
        return self.date_string
        
    def calculate_age(self,birth_date):
        
        current_date=datetime.now().date()
        birth_datetime=datetime(birth_date.year(),birth_date.month(),birth_date.day()).date()
        age=current_date.year - birth_datetime.year
        if (current_date.month,current_date.day) <(birth_datetime.month,birth_datetime.day):
            age-=1
        return age
            
        
    def show_inserted_message(self):
        msg_box=QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.name_lineEdit.text()+" insert into to database")
        msg_box.exec()

    def add_employe(self):
        self.insert_new_employe()
        self.accept()
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdateEmploye.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from datetime import datetime
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt,Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget,QMessageBox)
from mysqlx import OperationalError
import pymysql
import mysql.connector
from mysql.connector import Error

class UpdateEmployeDialog(QDialog):
    data_updated=Signal()
    def __init__(self,row_index,row_data):
        super().__init__()
        
        self.row_index=row_index
        self.row_data=row_data
        
        self.employe_id=self.row_data[0]
        self.employe_info = self.select_employe(self.employe_id)[0]
        self.employe_name_info=self.employe_info[1]
        self.employe_gender_info=self.employe_info[2]
        self.employe_services_info=self.employe_info[3]
        self.employe_birthday_info=self.employe_info[4]
        self.employe_age_info=self.employe_info[5]
        self.employe_address_info=self.employe_info[6]
        self.employe_phone_info=self.employe_info[7]
        self.employe_email_info=self.employe_info[8]
        
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
        self.label.setGeometry(QRect(20, 10, 421, 41))
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

        self.upddate_name_lineEdit = QLineEdit(self.layoutWidget)
        self.upddate_name_lineEdit.setObjectName(u"upddate_name_lineEdit")
        self.upddate_name_lineEdit.setMinimumSize(QSize(0, 35))
        self.upddate_name_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.upddate_name_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout.addWidget(self.upddate_name_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.verticalLayout_5.addWidget(self.label_6)

        self.update_gender_comboBox = QComboBox(self.layoutWidget)
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.addItem("")
        self.update_gender_comboBox.setObjectName(u"update_gender_comboBox")

        self.verticalLayout_5.addWidget(self.update_gender_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.update_services_comboBox = QComboBox(self.layoutWidget)
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.addItem("")
        self.update_services_comboBox.setObjectName(u"update_services_comboBox")

        self.verticalLayout_6.addWidget(self.update_services_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_dob_dateEdit = QDateEdit(self.layoutWidget)
        self.update_dob_dateEdit.setObjectName(u"update_dob_dateEdit")

        self.verticalLayout_7.addWidget(self.update_dob_dateEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_7)


        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.verticalLayout_2.addWidget(self.label_3)

        self.update_adresse_lineEdit = QLineEdit(self.layoutWidget)
        self.update_adresse_lineEdit.setObjectName(u"update_adresse_lineEdit")
        self.update_adresse_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_adresse_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_adresse_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_2.addWidget(self.update_adresse_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)

        self.verticalLayout_3.addWidget(self.label_4)

        self.update_phone_lineEdit = QLineEdit(self.layoutWidget)
        self.update_phone_lineEdit.setObjectName(u"update_phone_lineEdit")
        self.update_phone_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_phone_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_phone_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.update_phone_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.verticalLayout_4.addWidget(self.label_5)

        self.update_email_lineEdit = QLineEdit(self.layoutWidget)
        self.update_email_lineEdit.setObjectName(u"update_email_lineEdit")
        self.update_email_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_email_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_email_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_4.addWidget(self.update_email_lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_4)

        self.layoutWidget1 = QWidget(self)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(300, 460, 231, 43))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.update_employee_btn = QPushButton(self.layoutWidget1)
        self.update_employee_btn.setObjectName(u"update_employee_btn")
        self.update_employee_btn.setMinimumSize(QSize(0, 41))
        self.update_employee_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#34D481;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_employee_btn)

        self.update_cancle_btn = QPushButton(self.layoutWidget1)
        self.update_cancle_btn.setObjectName(u"update_cancle_btn")
        self.update_cancle_btn.setMinimumSize(QSize(0, 41))
        self.update_cancle_btn.setStyleSheet(u"QPushButton{\n"
"  background-color:#585858;\n"
"color:white;\n"
"border: none;\n"
"border-radius:8px;\n"
"font-weight:bold;\n"
"font-size:15px;\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.update_cancle_btn)


        self.retranslateUi()

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("UpdateEmployeDialog", u"Update Employe Dialog", None))
        self.setWindowIcon(QIcon(":/icones/logo.png"))
        self.label.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Update Employe Information", None))
        self.label_2.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Nom Complet ", None))
        self.label_6.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Genre", None))
        self.update_gender_comboBox.setItemText(0, QCoreApplication.translate("UpdateEmployeDialog", u"Male", None))
        self.update_gender_comboBox.setItemText(1, QCoreApplication.translate("UpdateEmployeDialog", u"Female", None))

        self.label_7.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Services ", None))
        self.update_services_comboBox.setItemText(0, QCoreApplication.translate("UpdateEmployeDialog", u"Preci-Dip", None))
        self.update_services_comboBox.setItemText(1, QCoreApplication.translate("UpdateEmployeDialog", u"Cellduc", None))
        self.update_services_comboBox.setItemText(2, QCoreApplication.translate("UpdateEmployeDialog", u"CMS", None))
        self.update_services_comboBox.setItemText(3, QCoreApplication.translate("UpdateEmployeDialog", u"4Energy", None))
        self.update_services_comboBox.setItemText(4, QCoreApplication.translate("UpdateEmployeDialog", u"Qualite", None))
        self.update_services_comboBox.setItemText(5, QCoreApplication.translate("UpdateEmployeDialog", u"CMS", None))
        self.update_services_comboBox.setItemText(6, "")

        self.label_8.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Date De Naissance", None))
        self.label_3.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Adresse", None))
        self.label_4.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Telephone", None))
        self.label_5.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Email", None))
        self.update_employee_btn.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Modifier", None))
        self.update_cancle_btn.setText(QCoreApplication.translate("UpdateEmployeDialog", u"Annuler", None))
    # retranslateUi
        date_object=QDate.fromString(self.employe_birthday_info,"yyyy-MM-dd") 
        self.upddate_name_lineEdit.setText(str(self.employe_name_info))
        self.update_gender_comboBox.setCurrentText(str(self.employe_gender_info))
        self.update_services_comboBox.setCurrentText(str(self.employe_services_info))
        self.update_dob_dateEdit.setDate(date_object)
        self.update_adresse_lineEdit.setText(str(self.employe_address_info))
        self.update_phone_lineEdit.setText(str(self.employe_phone_info))
        self.update_email_lineEdit.setText(str(self.employe_email_info))
        
        self.lastIndex=self.update_gender_comboBox.currentText()
        self.update_employee_btn.clicked.connect(self.update_date)
        
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
    
    def select_employe(self, employe_id):
        """Sélectionner un employé par son ID."""
        connection = self.create_connection()
        
        if connection:
            cursor = connection.cursor()
            
            # Utiliser l'ID de l'employé pour la sélection
            select_query = "SELECT * FROM employe_table WHERE employe_id = %s"
            cursor.execute(select_query, (employe_id,))
            
            records = cursor.fetchall()
            
            cursor.close()
            connection.close()
            
            return records
        else:
            return None

    def update_date(self):
        """Met à jour les informations de l'employé dans la base de données."""
        try:
            connection = self.create_connection()
            
            if connection is None:
                return
            
            cursor = connection.cursor()
            
            # Récupération des informations à mettre à jour
            birth_date = self.update_dob_dateEdit.date()
            birthday = self.handleDateChane()
            age = self.calculate_age(birth_date)
            current_employe_id = self.employe_id  # Utilisez l'ID existant de l'employé
            
            params = (
                self.upddate_name_lineEdit.text(),
                self.update_gender_comboBox.currentText(),
                self.update_services_comboBox.currentText(),
                birthday,
                age,
                self.update_adresse_lineEdit.text(),
                self.update_phone_lineEdit.text(),
                self.update_email_lineEdit.text(),
                current_employe_id
            )
            
            update_query = """UPDATE employe_table 
                            SET names=%s, gender=%s, services=%s, birthday=%s, age=%s, address=%s, phone=%s, email=%s
                            WHERE employe_id=%s"""
            cursor.execute(update_query, params)
            connection.commit()
            
            self.show_updated_message()
        except mysql.connector.Error as err:
            print(f"ERROR: {err}")    
        finally:
            cursor.close()
            connection.close()
            self.close()
            self.data_updated.emit()


            
    def handleDateChane(self):
        
        selected_date = self.update_dob_dateEdit.date()
        self.date_string = selected_date.toString(Qt.ISODate)
        return self.date_string
        
    def calculate_age(self,birth_date):
        
        current_date=datetime.now().date()
        birth_datetime=datetime(birth_date.year(),birth_date.month(),birth_date.day()).date()
        age=current_date.year - birth_datetime.year
        if (current_date.month,current_date.day) <(birth_datetime.month,birth_datetime.day):
            age-=1
        return age
    def on_gender_changed(self, index):
        """Retourne l'ID de l'employé actuel si le genre change, sinon retourne l'ID existant."""
        if index != self.lastIndex:
            gender_item = self.update_gender_comboBox.currentText()
            # Pas de nouvelle méthode employée requise
            return self.employe_id
        else:
            return self.employe_id

        
    def show_updated_message(self):
        msg_box=QMessageBox(self)
        msg_box.setWindowTitle("Success")
        msg_box.setText(self.employe_name_info +" information updated successfully")
        msg_box.exec()
        
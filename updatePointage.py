# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'UpdatepointageDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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

class Ui_UpdateEmployesDialog(QDialog):
    data_update=Signal()
    def __init__(self,row_index,row_data):
        super().__init__()
        self.row_index=row_index
        self.row_data=row_data

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

        self.update_employee_comboBox = QComboBox(self.layoutWidget)
        self.update_employee_comboBox.setObjectName(u"update_employee_comboBox")

        self.verticalLayout_5.addWidget(self.update_employee_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.verticalLayout_6.addWidget(self.label_7)

        self.update_poi_services_comboBox = QComboBox(self.layoutWidget)
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.addItem("")
        self.update_poi_services_comboBox.setObjectName(u"update_poi_services_comboBox")

        self.verticalLayout_6.addWidget(self.update_poi_services_comboBox)


        self.horizontalLayout.addLayout(self.verticalLayout_6)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.verticalLayout_7.addWidget(self.label_8)

        self.update_poi_dob_dateEdit = QDateEdit(self.layoutWidget)
        self.update_poi_dob_dateEdit.setObjectName(u"update_poi_dob_dateEdit")

        self.verticalLayout_7.addWidget(self.update_poi_dob_dateEdit)


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

        self.update_heuresTravailles_lineEdit = QLineEdit(self.layoutWidget)
        self.update_heuresTravailles_lineEdit.setObjectName(u"update_heuresTravailles_lineEdit")
        self.update_heuresTravailles_lineEdit.setMinimumSize(QSize(0, 35))
        self.update_heuresTravailles_lineEdit.setMaximumSize(QSize(16777215, 35))
        self.update_heuresTravailles_lineEdit.setSizeIncrement(QSize(0, 0))

        self.verticalLayout_3.addWidget(self.update_heuresTravailles_lineEdit)


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


        self.retranslateUi()  # Appel de la méthode pour définir le texte et finaliser l'UI
        self.populate_employee_combobox()
        self.load_existing_data()

# Connecter les boutons après leur création
        self.saveemployee_btn.clicked.connect(self.update_pointage)
        self.cancle_btn.clicked.connect(self.close)

        QMetaObject.connectSlotsByName(self)
    # setupUi

    def retranslateUi(self):
        self.setWindowTitle(QCoreApplication.translate("UpdateEmployesDialog", u"Update Pointage Dialog", None))
        self.setWindowIcon(QIcon("/icons/logo.png"))
        self.label.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Update Pointage", None))
        self.label_6.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Employee", None))
        self.label_7.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Services ", None))
        self.update_poi_services_comboBox.setItemText(0, QCoreApplication.translate("UpdateEmployesDialog", u"Preci-Dip", None))
        self.update_poi_services_comboBox.setItemText(1, QCoreApplication.translate("UpdateEmployesDialog", u"Cellduc", None))
        self.update_poi_services_comboBox.setItemText(2, QCoreApplication.translate("UpdateEmployesDialog", u"CMS", None))
        self.update_poi_services_comboBox.setItemText(3, QCoreApplication.translate("UpdateEmployesDialog", u"4Energy", None))
        self.update_poi_services_comboBox.setItemText(4, QCoreApplication.translate("UpdateEmployesDialog", u"Qualite", None))
        self.update_poi_services_comboBox.setItemText(5, QCoreApplication.translate("UpdateEmployesDialog", u"CMS", None))
        self.update_poi_services_comboBox.setItemText(6, "")

        self.label_8.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Date ", None))
        self.label_4.setText(QCoreApplication.translate("UpdateEmployesDialog", u"heure", None))
        self.saveemployee_btn.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Modifier", None))
        self.cancle_btn.setText(QCoreApplication.translate("UpdateEmployesDialog", u"Annuler", None))
        
        
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
    # retranslateUi

    def select_pointage(self):
        connection = self.create_connection()
        if not connection:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")
            return []
        
        employe_name = self.row_data[0]
        employe_service = self.row_data[1]
        
        select_query = """
            SELECT pt.pointage_id, et.names, et.services, pt.heures_travaillees
            FROM pointage_table pt
            JOIN employe_table et ON pt.employe_id = et.employe_id
            WHERE et.names = %s AND et.services = %s
        """
        
        try:
            with connection.cursor() as cursor:
                cursor.execute(select_query, (employe_name, employe_service))
                records = cursor.fetchall()
            return records
        except pymysql.Error as e:
            QMessageBox.warning(self, "Erreur de sélection", f"Erreur lors de la sélection des pointages : {e}")
            return []
        finally:
            connection.close()

    def populate_employee_combobox(self):
        connection = self.create_connection()
        if not connection:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")
            return

        try:
            with connection.cursor() as cursor:
                cursor.execute("SELECT employe_id, names FROM employe_table")
                employes = cursor.fetchall()

            self.update_employee_comboBox.clear()
            for employe_id, employe_name in employes:
                self.update_employee_comboBox.addItem(employe_name, employe_id)
        except pymysql.Error as e:
            QMessageBox.warning(self, "Erreur de chargement", f"Impossible de charger la liste des employés : {e}")
        finally:
            connection.close()

    def load_existing_data(self):
        # Assurez-vous que self.row_data contient les bonnes données
        print("Contenu de row_data:", self.row_data)  # Pour vérifier le contenu
        print("Nombre d'éléments dans row_data:", len(self.row_data))  # Pour vérifier la longueur

        if len(self.row_data) >= 4:
            employe_name = self.row_data[1]  # Nom de l'employé
            service = self.row_data[2]  # Service
            heures_travaillees = self.row_data[3]  # Heures travaillées
            pointage_id = self.row_data[0]  # ID de pointage

            # Trouver l'index du nom de l'employé et le sélectionner
            index = self.update_employee_comboBox.findText(str(employe_name))
            if index >= 0:
                self.update_employee_comboBox.setCurrentIndex(index)
            else:
                QMessageBox.warning(self, "Erreur", "Nom de l'employé non trouvé.")

            # Met à jour le champ des heures travaillées
            self.update_heuresTravailles_lineEdit.setText(str(heures_travaillees))

            # Cherche l'index du service et le sélectionne si trouvé
            index = self.update_poi_services_comboBox.findText(service)
            if index >= 0:
                self.update_poi_services_comboBox.setCurrentIndex(index)
            else:
                QMessageBox.warning(self, "Erreur", "Service non trouvé.")
        else:
            QMessageBox.warning(self, "Erreur", "Données invalides pour la mise à jour.")




    def update_pointage(self):
        connection = self.create_connection()
        if not connection:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")
            return

        employe_name = self.update_employee_comboBox.currentText()
        employe_id = self.get_employe_id(employe_name)
        if not employe_id:
            QMessageBox.warning(self, "Erreur", "Employé non trouvé.")
            return

        service = self.update_poi_services_comboBox.currentText()
        heures_travaillees = self.update_heuresTravailles_lineEdit.text()
        date = self.update_poi_dob_dateEdit.date().toString("yyyy-MM-dd")

        # Validation des heures travaillées
        if not heures_travaillees.replace('.', '', 1).isdigit():
            QMessageBox.warning(self, "Erreur de saisie", "Veuillez entrer un nombre valide pour les heures travaillées.")
            return

        pointage_id = self.row_data[0]  # Assurez-vous que `pointage_id` est le bon index

        try:
            with connection.cursor() as cursor:
                update_query = """
                    UPDATE pointage_table
                    SET employe_id = %s, heures_travaillees = %s, date = %s
                    WHERE pointage_id = %s
                """
                cursor.execute(update_query, (employe_id, heures_travaillees, date, pointage_id))
                connection.commit()

            QMessageBox.information(self, "Mise à jour réussie", "Le pointage a été mis à jour avec succès.")
            
            self.close()
            self.data_update.emit()
        except pymysql.Error as e:
            QMessageBox.warning(self, "Erreur de mise à jour", f"Erreur lors de la mise à jour du pointage : {e}")
        finally:
            connection.close()


    def get_employe_id(self, employe_name):
        # Créer une connexion et un curseur
        connection = self.create_connection()
        if not connection:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")
            return None

        try:
            with connection.cursor() as cursor:
                # Afficher le nom de l'employé pour le débogage
                print(f"Recherche de l'employé avec le nom : {employe_name}")

                # Requête pour obtenir l'ID de l'employé à partir du nom
                query = "SELECT employe_id FROM employe_table WHERE names = %s"
                cursor.execute(query, (employe_name,))
                result = cursor.fetchone()

                # Afficher le résultat pour le débogage
                if result:
                    print(f"Employé trouvé : ID = {result[0]}")
                    return result[0]  # Retourner l'ID de l'employé
                else:
                    print("Employé non trouvé dans la base de données.")
                    QMessageBox.warning(self, "Erreur", "Employé non trouvé.")
                    return None
        except pymysql.Error as e:
            QMessageBox.warning(self, "Erreur de requête", f"Erreur lors de la récupération de l'ID de l'employé : {e}")
            return None
        finally:
            connection.close()

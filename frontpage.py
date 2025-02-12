from PySide6.QtWidgets import QMenu, QMainWindow, QTableWidgetItem, QWidget, QHBoxLayout, QPushButton,QMessageBox
from PySide6.QtGui import QAction, QIcon
from PySide6.QtCore import QSize
from ui_index import Ui_MainWindow
import pymysql
import os
from pymysql import OperationalError
from UpdateEmployeDialog import UpdateEmployeDialog
from updatePointage import Ui_UpdateEmployesDialog


class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")
        self.icon_only_widget.setHidden(True)
        self.employee_dropdown.setHidden(True)
        self.pointage_dropdown.setHidden(True)

        # Connexion des boutons
        self.dashboard_1.clicked.connect(self.switch_to_dashboard_page)
        self.dashboard_2.clicked.connect(self.switch_to_dashboard_page)
        self.institution_1.clicked.connect(self.switch_to_institution_page)
        self.institution_2.clicked.connect(self.switch_to_institution_page)
        self.pointage.clicked.connect(self.switch_to_pointage_page)
        self.historique.clicked.connect(self.switch_to_historique_page)
        self.employes.clicked.connect(self.switch_to_employes_page)
        self.administrateurs.clicked.connect(self.switch_to_administrateurs_page)
        self.setting_1.clicked.connect(self.switch_to_setting_page)
        self.setting_2.clicked.connect(self.switch_to_setting_page)
        self.employe_1.clicked.connect(self.employes_contact_menu)
        self.pointage_1.clicked.connect(self.pointage_contact_menu)
        self.addemployee_btn.clicked.connect(self.open_addemploye_dialog)

        # Configuration des tables
        self.employe_info_table.setColumnWidth(0, 100)
        self.employe_info_table.setColumnWidth(1, 70)
        self.employe_info_table.setColumnWidth(2, 100)
        self.employe_info_table.setColumnWidth(3, 80)
        self.employe_info_table.setColumnWidth(4, 80)
        self.employe_info_table.setColumnWidth(5, 80)
        self.employe_info_table.setColumnWidth(6, 90)
        self.employe_info_table.setColumnWidth(7, 150)
        self.employe_info_table.setColumnWidth(8, 150)

        self.employe_info_table_2.setColumnWidth(0, 250)
        self.employe_info_table_2.setColumnWidth(1, 250)
        self.employe_info_table_2.setColumnWidth(2, 200)
        self.employe_info_table_2.setColumnWidth(3, 200)
        # Connexion aux changements de sélection
        self.historique_table_info.setColumnWidth(0,200)
        self.historique_table_info.setColumnWidth(1,198)
        self.historique_table_info.setColumnWidth(2,201)
        
        self.select_services.currentIndexChanged.connect(self.load_employes_info)
        self.select_gender.currentIndexChanged.connect(self.load_employes_info)

        # Création de la connexion et de la table
        self.create_connection()
        self.create_employe_table()
        self.load_employes_info()
        self.search_employe.textChanged.connect(self.search_employee)
        self.create_pointage_table()
        self.save_pointage_btn.clicked.connect(self.open_addPointage_dialog)
        self.load_table_pointage()
        self.poin_select_services_2.currentIndexChanged.connect(self.load_table_pointage)
        self.pointage_dob_dateEdit_2.dateChanged.connect(self.load_table_pointage)
        self.poin_search_employe_2.textChanged.connect(self.search_employee_point)
        
        self.load_employees_data_tot()
        
        # Connecter les signaux des ComboBox pour recharger les données quand une sélection change
        self.select_month_2.currentIndexChanged.connect(self.load_employees_data_tot)
        self.select_year_2.currentIndexChanged.connect(self.load_employees_data_tot)
        
        self.search_employe_histo.textChanged.connect(self.search_employe_2)

            
        
    def switch_to_dashboard_page(self):
        self.stackedWidget.setCurrentIndex(0)

    def switch_to_institution_page(self):
        self.stackedWidget.setCurrentIndex(1)

    def switch_to_pointage_page(self):
        self.stackedWidget.setCurrentIndex(2)

    def switch_to_historique_page(self):
        self.stackedWidget.setCurrentIndex(3)

    def switch_to_employes_page(self):
        self.stackedWidget.setCurrentIndex(4)

    def switch_to_administrateurs_page(self):
        self.stackedWidget.setCurrentIndex(5)

    def switch_to_setting_page(self):
        self.stackedWidget.setCurrentIndex(6)

    def employes_contact_menu(self):
        self.show_custom_menu(self.employe_1, ["Employes", "Administrateurs"])

    def pointage_contact_menu(self):
        self.show_custom_menu(self.pointage_1, ["Pointage", "Historique"])

    def show_custom_menu(self, button, menu_items):
        menu = QMenu(self)
        menu.setStyleSheet("""
                           QMenu{
                            background-color:black;
                            color: white;
                            }
                            QMenu:selected{
                            background-color:white;
                            color:#12B298;
                            }
                           """)
        for item_txt in menu_items:
            action = QAction(item_txt, self)
            action.triggered.connect(self.handle_menu_items_clicks)
            menu.addAction(action)

        menu.move(button.mapToGlobal(button.rect().topRight()))
        menu.exec()

    def handle_menu_items_clicks(self):
        text = self.sender().text()
        if text == "Employes":
            self.switch_to_employes_page()
        elif text == "Administrateurs":
            self.switch_to_administrateurs_page()
        elif text == "Pointage":
            self.switch_to_pointage_page()
        elif text == "Historique":
            self.switch_to_historique_page()

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

    def create_employe_table(self):
        """Créer la table employe_table dans la base de données"""
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            create_employe_table_query = """
                CREATE TABLE IF NOT EXISTS employe_table (
                    employe_id INT AUTO_INCREMENT PRIMARY KEY,
                    names TEXT,
                    gender TEXT,
                    services TEXT,
                    birthday TEXT,
                    age INT,
                    address TEXT,
                    phone VARCHAR(15),
                    email VARCHAR(50)
                )
            """
            try:
                cursor.execute(create_employe_table_query)
                connection.commit()
                print("Table employe_table créée avec succès.")
            except OperationalError as e:
                print(f"Erreur lors de la création de la table : {e}")
            finally:
                cursor.close()
                connection.close()

    def open_addemploye_dialog(self):
        from EmployeDialog import Ui_EmployesDialog
        
        addEmploye_dialog = Ui_EmployesDialog(self)
        result = addEmploye_dialog.exec()
        
        if result == Ui_EmployesDialog.Accepted:
            self.load_employes_info()

    def load_employes_info(self):
        print("Chargement des informations des employés...")
        self.employe_info_table.setRowCount(0)  # Réinitialiser la table
        selected_service = self.select_services.currentText()
        selected_gender = self.select_gender.currentText()
        
        print(f"Filtres : Service = {selected_service}, Genre = {selected_gender}")
        
        # Récupérer les données filtrées de la base de données
        data = self.get_data_from_table(selected_service, selected_gender)
        
        print(f"Nombre d'enregistrements récupérés : {len(data)}")
        
        for row_index, row_data in enumerate(data):
            self.employe_info_table.insertRow(row_index)  # Insérer une nouvelle ligne
            for column_index, item in enumerate(row_data[1:]):  # Ignorer le premier élément
                table_item = QTableWidgetItem(str(item))
                self.employe_info_table.setItem(row_index, column_index, table_item)
                print(f"Ajout de la ligne {row_index}, colonne {column_index + 1} : {item}")
            
            # Ajouter le widget avec les boutons dans la dernière colonne
            action_widget = DoubleButtonWidgetEmployes(row_index, row_data,self)
            self.employe_info_table.setCellWidget(row_index, self.employe_info_table.columnCount() - 1, action_widget)
            self.employe_info_table.setRowHeight(row_index,50)


    def get_data_from_table(self, service_filter, gender_filter):
        connection = self.create_connection()
        if connection:
            cursor = connection.cursor()
            query = """
            SELECT employe_id, names, gender, services, birthday, age, address, phone, email 
            FROM employe_table 
            WHERE 
            (%s = 'SELECT SERVICE' OR services = %s OR %s = 'SELECT SERVICES') AND 
            (%s = 'SELECT GENDER' OR gender = %s OR %s = 'SELECT GENDER')
            """
            cursor.execute(query, (service_filter, service_filter, service_filter, 
                                gender_filter, gender_filter, gender_filter))
            data = cursor.fetchall()
            cursor.close()
            connection.close()
            
            print(f"Données récupérées de la base de données : {data}")
            
            return data
        else:
            print("Échec de la connexion à la base de données")
            return []

    def search_employee(self):
        self.employe_info_table.setRowCount(0)
        search_query=self.search_employe.text()
        
        cursor=self.create_connection().cursor()
        sql_query=f""" SELECT employe_id,names,gender,services,birthday,age,address,phone,email FROM employe_table 
                    WHERE names LIKE '%{search_query}%'"""
        cursor.execute(sql_query)
        results=cursor.fetchall()
        for row_index, row_data in enumerate(results):
            self.employe_info_table.insertRow(row_index)  # Insérer une nouvelle ligne
            for column_index, item in enumerate(row_data[1:]):  # Ignorer le premier élément
                table_item = QTableWidgetItem(str(item))
                self.employe_info_table.setItem(row_index, column_index, table_item)
                print(f"Ajout de la ligne {row_index}, colonne {column_index + 1} : {item}")
            
            # Ajouter le widget avec les boutons dans la dernière colonne
            action_widget = DoubleButtonWidgetEmployes(row_index, row_data,self)
            self.employe_info_table.setCellWidget(row_index, self.employe_info_table.columnCount() - 1, action_widget)
            self.employe_info_table.setRowHeight(row_index,50)
    def create_pointage_table(self):
        # Créer une connexion et un curseur
        connection = self.create_connection()
        cursor = connection.cursor()
        
        # Requête pour créer la table de pointage
        create_pointage_table_query = """
            CREATE TABLE IF NOT EXISTS pointage_table (
                pointage_id INT AUTO_INCREMENT PRIMARY KEY,
                employe_id int,
                date TEXT,
                heures_travaillees DECIMAL(5, 2),
                FOREIGN KEY (employe_id) REFERENCES employe_table(employe_id)
            )
        """
        
        # Exécuter la requête de création de table
        cursor.execute(create_pointage_table_query)
        
        # Commit les changements et fermer la connexion
        connection.commit()
        cursor.close()
        connection.close()

    def open_addPointage_dialog(self):
        from pointageDialog import Ui_PointageDialog
        addpointage_dialog=Ui_PointageDialog(self)
        result=addpointage_dialog.exec()
        
        if result==Ui_PointageDialog.accept:
            self.load_table_pointage()

    def load_table_pointage(self):
    # Réinitialiser le nombre de lignes du tableau
        self.employe_info_table_2.setRowCount(0)

        # Récupérer les valeurs sélectionnées dans les combobox et date edit
        selected_services = self.poin_select_services_2.currentText()
        selected_date = self.pointage_dob_dateEdit_2.date().toString("yyyy-MM-dd")  # Format de date standardisé

        # Récupérer les données en fonction des filtres
        data = self.get_data_from_pointTable(selected_services, selected_date)

        # Remplir le tableau avec les données récupérées
        for row_index, row_data in enumerate(data):
            self.employe_info_table_2.insertRow(row_index)
            # La colonne de la date est ignorée, donc elle n'est pas affichée
            for column_index, value in enumerate(row_data[1:]):  # Ignorer le premier élément (ID de pointage)
                self.employe_info_table_2.setItem(row_index, column_index, QTableWidgetItem(str(value)))
            
            # Ajouter les boutons d'action à la dernière colonne
            double_button_widget2 = DoubleButtonWidgetPintage(row_index, row_data, self)
            self.employe_info_table_2.setCellWidget(row_index, 3, double_button_widget2)  # Index de la colonne des actions
            self.employe_info_table_2.setRowHeight(row_index, 50)

    def get_data_from_pointTable(self, service_filter, date_filter):
        # Récupération des données en fonction des filtres appliqués
        connection = self.create_connection()
        if connection:
            try:
                with connection.cursor() as cursor:
                    # Requête SQL pour récupérer les pointages en fonction du service et de la date
                    query = """
                        SELECT pt.pointage_id, et.names, et.services, pt.heures_travaillees
                        FROM pointage_table pt
                        JOIN employe_table et ON pt.employe_id = et.employe_id
                        WHERE (et.services = %s OR %s = 'SELECT SERVICE') AND (pt.date = %s)
                    """
                    cursor.execute(query, (service_filter, service_filter, date_filter))
                    result = cursor.fetchall()
                    return result
            except pymysql.MySQLError as e:
                QMessageBox.critical(self, "Erreur de base de données", f"Erreur lors de la récupération des pointages : {e}")
                return []
            finally:
                connection.close()
        else:
            QMessageBox.warning(self, "Erreur de connexion", "Impossible de se connecter à la base de données.")
            return []
    def search_employee_point(self):
        search_text = self.search_line_edit.text().lower()
        
        # Réinitialisez la table
        self.employe_info_table.setRowCount(0)
        
        # Récupérez toutes les données (ou filtrez si possible)
        data = self.get_data_from_table('SELECT SERVICE', 'SELECT GENDER')  # Vous pouvez ajuster les filtres
        
        for row_index, row_data in enumerate(data):
            # Filtrer les données en fonction du texte de recherche
            if any(search_text in str(item).lower() for item in row_data):
                self.employe_info_table.insertRow(row_index)
                for column_index, item in enumerate(row_data[1:]):  # Ignorer le premier élément
                    table_item = QTableWidgetItem(str(item))
                    self.employe_info_table.setItem(row_index, column_index, table_item)
                
                # Ajouter le widget avec les boutons dans la dernière colonne
                action_widget = DoubleButtonWidgetEmployes(row_index, row_data, self)
                self.employe_info_table.setCellWidget(row_index, self.employe_info_table.columnCount() - 1, action_widget)
                self.employe_info_table.setRowHeight(row_index, 50)

    def load_employees_data_tot(self):
        # Récupérer le mois et l'année sélectionnés
        selected_month = self.select_month_2.currentText()
        selected_year = self.select_year_2.currentText()
        
        # Créer une connexion à la base de données
        connection = self.create_connection()
        if not connection:
            print("Erreur de connexion à la base de données.")
            return
        
        cursor = connection.cursor()
        
        # Convertir le mois en nombre pour filtrer dans la base de données (exemple pour janvier -> 01)
        month_mapping = {
            "Janvier": "1", "Février": "2", "Mars": "3", "Avril": "4", "Mai": "5", 
            "Juin": "6", "Juillet": "7", "Août": "8", "Septembre": "9", 
            "Octobre": "10", "Novembre": "11", "Décembre": "12"
        }
        selected_month_num = month_mapping.get(selected_month)
        
        if not selected_month_num:
            print("Mois invalide sélectionné.")
            return
        
        # Requête SQL pour récupérer les employés et les heures travaillées
        query = """
            SELECT e.names, e.services, SUM(p.heures_travaillees)
            FROM employe_table e
            JOIN pointage_table p ON e.employe_id = p.employe_id
            WHERE MONTH(p.date) = %s AND YEAR(p.date) = %s
            GROUP BY e.employe_id
        """
        
        # Exécuter la requête
        try:
            cursor.execute(query, (selected_month_num, selected_year))
            results = cursor.fetchall()
            
            # Vider le QTableWidget avant de remplir avec de nouvelles données
            self.historique_table_info.setRowCount(0)
            
            # Remplir le QTableWidget avec les résultats
            for row_number, row_data in enumerate(results):
                self.historique_table_info.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.historique_table_info.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except Exception as e:
            print(f"Erreur lors de la récupération des données : {e}")
        finally:
            cursor.close()
            connection.close()


    def search_employe_2(self):
        search_text = self.search_employe_histo.text()
        
        # Créer une connexion à la base de données
        connection = self.create_connection()
        if not connection:
            print("Erreur de connexion à la base de données.")
            return
        
        cursor = connection.cursor()
        
        # Requête SQL pour filtrer les employés
        query = """
            SELECT e.names, e.services, SUM(p.heures_travaillees)
            FROM employe_table e
            LEFT JOIN pointage_table p ON e.employe_id = p.employe_id
            WHERE e.names LIKE %s
            GROUP BY e.employe_id
        """
        
        try:
            cursor.execute(query, (f'%{search_text}%',))
            results = cursor.fetchall()
            
            # Vider le QTableWidget avant de remplir avec de nouvelles données
            self.historique_table_info.setRowCount(0)
            
            # Remplir le QTableWidget avec les résultats
            for row_number, row_data in enumerate(results):
                self.historique_table_info.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.historique_table_info.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        
        except Exception as e:
            print(f"Erreur lors de la récupération des données : {e}")
        finally:
            cursor.close()
            connection.close()


    def reload_data(self):
        self.search_employe_2()  # Appeler la méthode de recherche pour recharger les données

                    
                  
class DoubleButtonWidgetEmployes(QWidget): 
    def __init__(self, row_index, row_data,sideBar):
        super().__init__()
        self.row_index = row_index
        self.row_data = row_data
        self.sideBar=sideBar

        # Définir les chemins des icônes
        
        layout = QHBoxLayout(self)

        self.edit_button = QPushButton("", self)
        self.edit_button.setStyleSheet("background-color: blue;")
        self.edit_button.setFixedSize(61, 31)
        self.edit_button.clicked.connect(self.edit_employe)
        # Ajuster la taille de l'icône

        self.delete_button = QPushButton("", self)
        self.delete_button.setStyleSheet("background-color: red;")
        self.delete_button.setFixedSize(61, 31)
        
        icon=QIcon(":/icones/edit.png")
        self.edit_button.setIcon(icon)
        
        icon2=QIcon(":/icones/delete.png")
        self.delete_button.setIcon(icon2)
        

        layout.addWidget(self.edit_button)
        layout.addWidget(self.delete_button)

        #self.edit_button.clicked.connect(self.edit_employe)
        self.delete_button.clicked.connect(self.delete_employe)

    def edit_employe(self):
        self.update_dialog=UpdateEmployeDialog(self.row_index,self.row_data)
        self.update_dialog.data_updated.connect(self.sideBar.load_employes_info)
        self.update_dialog.exec()
        

    def delete_employe(self):
        cursor=self.create_connection().cursor()
        message=QMessageBox.question(
            self, 'Confirmation',
            'Are you sure you want to delete '+ self.row_data[1] +'?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if message==QMessageBox.StandardButton.Yes:
            delete_query="DELETE FROM employe_table WHERE employe_id=%s"
            cursor.execute(delete_query,(self.row_data[0],))
            self.mydb.commit()
            self.mydb.close()
            
            self.sideBar.load_employes_info()
        # Logique de suppression ici
        
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
        
class DoubleButtonWidgetPintage(QWidget): 
    def __init__(self, row_index, row_data,sideBar):
        super().__init__()
        self.row_index = row_index
        self.row_data = row_data
        self.sideBar=sideBar

        # Définir les chemins des icônes
        
        layout = QHBoxLayout(self)

        self.edit_button1= QPushButton("", self)
        self.edit_button1.setStyleSheet("background-color: blue;")
        self.edit_button1.setFixedSize(61, 31)
        self.edit_button1.clicked.connect(self.edit_pointage)
        # Ajuster la taille de l'icône

        self.delete_button1 = QPushButton("", self)
        self.delete_button1.setStyleSheet("background-color: red;")
        self.delete_button1.setFixedSize(61, 31)
        
        icon=QIcon(":/icones/edit.png")
        self.edit_button1.setIcon(icon)
        
        icon2=QIcon(":/icones/delete.png")
        self.delete_button1.setIcon(icon2)
        

        layout.addWidget(self.edit_button1)
        layout.addWidget(self.delete_button1)

        #self.edit_button.clicked.connect(self.edit_employe)
        self.delete_button1.clicked.connect(self.delete_pointage)

    def edit_pointage(self):
        self.update_dialog_poin=Ui_UpdateEmployesDialog(self.row_index,self.row_data)
        self.update_dialog_poin.data_update.connect(self.sideBar.load_table_pointage)
        self.update_dialog_poin.exec()
        

    def delete_pointage(self):
        cursor=self.create_connection().cursor()
        message=QMessageBox.question(
            self, 'Confirmation',
            'Are you sure you want to delete '+ self.row_data[1] +'?',
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        if message==QMessageBox.StandardButton.Yes:
            delete_query="DELETE FROM pointage_table WHERE pointage_id=%s"
            cursor.execute(delete_query,(self.row_data[0],))
            self.mydb.commit()
            self.mydb.close()
            
            self.sideBar.load_employes_info()
            self.sideBar.load_table_pointage()
        # Logique de suppression ici
        
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
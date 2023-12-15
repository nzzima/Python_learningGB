import sys
import psycopg2
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from PyQt6 import QtWidgets, QtGui, uic
from PyQt6.QtWidgets import QApplication, QDialog, QTableWidgetItem

class StartWindow(QDialog):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("C:/Users/nzzima/Desktop/Python_learningGB/sem8/telephone_book_gui/startWindow.ui", self)
        self.my_close = False
        self.start_button.clicked.connect(self.go_to_phone_book)
        
    def go_to_phone_book(self):
        ph_book = Phone_book()
        widget.addWidget(ph_book)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        
        
class Phone_book(QDialog):
    def __init__(self):
        super().__init__()
        
        uic.loadUi("C:/Users/nzzima/Desktop/Python_learningGB/sem8/telephone_book_gui/phoneBookWindow.ui", self)
        
        widget.setFixedHeight(800)
        widget.setFixedWidth(800)

        self.my_close = False
        self.tableWidget.hide()
        self.refresh_button.hide()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.add_button.hide()
        self.id.hide()
        self.name.hide()
        self.surname.hide()
        self.phone.hide()
        self.about.hide()
        self.confirm_add_button.hide()
        self.search_button.hide()
        self.search_tag.hide()
        self.search_info.hide()
        self.confirm_search_button.hide()
        self.change_button.hide()
        self.change_tag.hide()
        self.change_info.hide()
        self.change_id_person.hide()
        self.confirm_change_button.hide()
        self.delete_button.hide()
        self.delete_tag.hide()
        self.delete_info.hide()
        self.confirm_delete_button.hide()
        
        try:
            self.connection = psycopg2.connect(user="postgres",
                                               password="postgres",
                                               host="127.0.0.1",
                                               port="5432",
                                               database="phone_book")
            
            self.connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
            self.cursor = self.connection.cursor()
            print("Success connect to phone_book database!")
            
        except (Exception, Error) as error:
            print("Error connect to phone_book database!", error)
            
        self.explore_button.clicked.connect(self.click_explore)
        self.refresh_button.clicked.connect(self.refresh_book)
        self.add_button.clicked.connect(self.add_person)
        self.confirm_add_button.clicked.connect(self.confirm_adding)
        self.search_button.clicked.connect(self.search_persons)
        self.confirm_search_button.clicked.connect(self.confirm_searching)
        self.delete_button.clicked.connect(self.delete_person)
        self.confirm_delete_button.clicked.connect(self.confirm_deleting)
        self.change_button.clicked.connect(self.change_person)
        self.confirm_change_button.clicked.connect(self.confirm_changing)
        self.exit_button.clicked.connect(lambda: widget.close())
        
    def click_explore(self):
        self.explore_button.hide()
        self.tableWidget.show()
        self.tableWidget.clear()
        
        self.refresh_button.show()
        self.add_button.show()
        self.search_button.show()
        self.change_button.show()
        self.delete_button.show()
        
        self.tableWidget.clear()
        self.fill_table(self.tableWidget, self.cursor, f'''SELECT * FROM phone_book_table ORDER BY "ID_person";''')
        
    def refresh_book(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        self.fill_table(self.tableWidget, self.cursor, f'''SELECT * FROM phone_book_table ORDER BY "ID_person";''')
        print("Success refresh")
    
    def fill_table(self, table_widget, my_cursor, request):
        my_cursor.execute(f'''SELECT column_name FROM information_schema.columns WHERE table_name = 'phone_book_table' ORDER BY ORDINAL_POSITION;''')
        result_header = my_cursor.fetchall()
        table_widget.setColumnCount(len(result_header))
        
        i = 0
        for row in result_header:
            for item in row:
                temp = QTableWidgetItem()
                temp.setText(item)
                table_widget.setHorizontalHeaderItem(i, temp)
            i += 1
        
        my_cursor.execute(request)
        result_table = my_cursor.fetchall()
        
        for row, form in enumerate(result_table):
            table_widget.insertRow(row)
            for column, item in enumerate(form):
                table_widget.setItem(row, column, QTableWidgetItem(str(item)))
                
    def add_person(self):
        self.id.show()
        self.name.show()
        self.surname.show()
        self.phone.show()
        self.about.show()
        self.confirm_add_button.show()
        
    def confirm_adding(self):
        id_person = self.id.toPlainText()
        name_person = self.name.toPlainText()
        surname_person = self.surname.toPlainText()
        phone_person = self.phone.toPlainText()
        about_person = self.about.toPlainText()
        
        self.cursor.execute(f'''INSERT INTO phone_book_table ("ID_person", "name", "surname", "phone", "about_info")
                                VALUES ({id_person}, '{name_person}', '{surname_person}', {phone_person}, '{about_person}');''')
        
        self.id.hide()
        self.name.hide()
        self.surname.hide()
        self.phone.hide()
        self.about.hide()
        self.confirm_add_button.hide()
        print("Success ADD")
        
    def search_persons(self):
        self.search_tag.show()
        self.search_info.show()
        self.confirm_search_button.show()
        
    def confirm_searching(self):
        self.tableWidget.clear()
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(0)
        
        tag = self.search_tag.toPlainText()
        inf = self.search_info.toPlainText()
        
        if tag == "phone" or tag == "ID_person":
            self.fill_table(self.tableWidget, self.cursor, f'''SELECT * FROM phone_book_table WHERE "{tag}" = {inf};''')
        elif tag == "name" or tag == "surname" or tag == "about_info":
            self.fill_table(self.tableWidget, self.cursor, f'''SELECT * FROM phone_book_table WHERE "{tag}" = '{inf}';''')
        
        self.search_tag.hide()
        self.search_info.hide()
        self.confirm_search_button.hide()
        print("Success SEARCH")
        
    def change_person(self):
        self.change_tag.show()
        self.change_info.show()
        self.change_id_person.show()
        self.confirm_change_button.show()
        
    def confirm_changing(self):
        id = self.change_id_person.toPlainText()
        tag = self.change_tag.toPlainText()
        inf = self.change_info.toPlainText()
        
        if tag == "phone" or tag == "ID_person":
            self.cursor.execute(f'''UPDATE phone_book_table SET "{tag}" = {inf} WHERE "ID_person" = {id};''')
        elif tag == "name" or tag == "surname" or tag == "about_info":
            self.cursor.execute(f'''UPDATE phone_book_table SET "{tag}" = '{inf}' WHERE "ID_person" = {id};''')
            
        self.change_tag.hide()
        self.change_info.hide()
        self.change_id_person.hide()
        self.confirm_change_button.hide()
        print("Success CHANGE")
        
    def delete_person(self):
        self.delete_tag.show()
        self.delete_info.show()
        self.confirm_delete_button.show()
        
    def confirm_deleting(self):
        tag = self.delete_tag.toPlainText()
        inf = self.delete_info.toPlainText()
        
        if tag == "phone" or tag == "ID_person":
            self.cursor.execute(f'''DELETE FROM phone_book_table WHERE "{tag}" = {inf};''')
        elif tag == "name" or tag == "surname" or tag == "about_info":
            self.cursor.execute(f'''DELETE FROM phone_book_table WHERE "{tag}" = '{inf}';''')
        
        self.delete_tag.hide()
        self.delete_info.hide()
        self.confirm_delete_button.hide()
        print("Success DELETE")
        
        
app = QApplication(sys.argv)
startWindow = StartWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(startWindow)
widget.setWindowTitle("Phone-Book")
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
app.exec()
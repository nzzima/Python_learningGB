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
        self.my_close = False
        self.tableWidget.hide()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.EditTrigger.NoEditTriggers)
        self.add_button.hide()
        self.search_button.hide()
        self.change_button.hide()
        self.delete_button.hide()
        
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
        self.exit_button.clicked.connect(lambda: widget.close())
        
    def click_explore(self):
        self.tableWidget.show()
        
        self.add_button.show()
        self.search_button.show()
        self.change_button.show()
        self.delete_button.show()
        
        self.tableWidget.clear()
        self.fill_table(self.tableWidget, self.cursor)
    
    def fill_table(self, table_widget, my_cursor):
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
        
        my_cursor.execute(f'''SELECT * FROM phone_book_table ORDER BY "ID_person";''')
        result_table = my_cursor.fetchall()
        
        for row, form in enumerate(result_table):
            table_widget.insertRow(row)
            for column, item in enumerate(form):
                table_widget.setItem(row, column, QTableWidgetItem(str(item)))
        
app = QApplication(sys.argv)
startWindow = StartWindow()
widget = QtWidgets.QStackedWidget()
widget.addWidget(startWindow)
widget.setWindowTitle("Phone-Book")
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()
app.exec()
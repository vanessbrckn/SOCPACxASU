import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import MySQLdb as mdb



class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "SOCPAC Dashboard"
        self.top = 500
        self.left = 800
        self.width = 600
        self.height = 500

        self.initWindow()

    def initWindow(self):
        self.button = QPushButton('OK', self)
        self.button.setGeometry(100, 300, 200, 50)
        self.button.clicked.connect(self.DBConnection)

        self.setWindowIcon(QtGui.QIcon("logo.jpg"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.Orgin = QLabel(self)
        self.Destination = QLabel(self)

        self.Orgin.setText('Orgin: ')
        self.Destination.setText('Destination: ')

        self.OrginAnswer = QLineEdit(self)
        self.DestAnswer = QLineEdit(self)

        self.OrginAnswer.move(120,20)
        self.DestAnswer.move(120,60)

        self.OrginAnswer.resize(200,32)
        self.DestAnswer.resize(200,32)

        self.Orgin.move(20, 20)
        self.Destination.move(20,60)

        self.show()


    def DBConnection(self):
        db = mdb.connect(host="bkiazvlmf2da3jw6cpwq-mysql.services.clever-cloud.com", user="u0q348qzs0ebwle4",
                         password="7KemNoGxkh1NcsoTlytG", database="bkiazvlmf2da3jw6cpwq")

        userOrgin = self.OrginAnswer.text()
        userDestination = self.DestAnswer.text()

        #This query will be based on user input from previous screens. i.e map and questionne answers

        userQuery = "SELECT p.planeID, p.modelNum FROM bkiazvlmf2da3jw6cpwq.plane p  " \
                    "WHERE p.location=1;"

        cursor = db.cursor()
        cursor.execute(userQuery)
        records = cursor.fetchall()

        rows = "plane ID  Model Number\n"
        for row in records:
            rows+=str(row[0])+"\t\t"+str(row[1])+"\n"

        self.label = QLabel(rows, self)
        self.label.move(120, 100)
        self.label.show()



App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())




from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem
from Designer import Ui_Form
import sys
import sqlite3


class Window(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.con = sqlite3.connect("coffee.db")

        self.update_btn.clicked.connect(self.updates)
        self.change_btn.clicked.connect(self.changes)
        self.create_btn.clicked.connect(self.creates)

    def updates(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM coffee").fetchall()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(len(result[0]))
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def creates(self):
        pass

    def changes(self):
        pass


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()

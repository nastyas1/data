import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem, QDialog



class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/nastya/Documents/code/test-5/sql2/untitled2.ui", self)
        self.con = sqlite3.connect("/home/nastya/Documents/code/test-5/kofe.sqlite")
        self.save.clicked.connect(self.update_result)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.change.clicked.connect(self.save_results)
        self.modified = {}
        self.titles = None

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute("SELECT * FROM kofee WHERE id=?",
                            (item_id := self.textEdit.toPlainText(), )).fetchall()
        self.tableWidget.setRowCount(len(result))
        if not result:
            self.statusBar().showMessage('Ничего не нашлось')
            return
        else:
            self.statusBar().showMessage(f"Нашлась запись с id = {item_id}")
        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))
        self.modified = {}
    def item_changed(self, item):
        self.modified[self.titles[item.column()]] = item.text()

    def save_results(self):
        if self.modified:
            cur = self.con.cursor()
            que = "UPDATE kofee SET\n"
            que += ", ".join([f"{key}='{self.modified.get(key)}'"
                            for key in self.modified.keys()])
            que += "WHERE id = ?"
            print(que)
            cur.execute(que, (self.textEdit.toPlainText(),))
            self.con.commit()
            self.modified.clear()

    def generate_new_elems(self, ids):
        cur = self.con.cursor()
        for i in ids:
            data = cur.execute(f'SELECT * FROM kofee WHERE id = {i}').fetchall()
            new_data = (data[0], data[1][::-1], data[2] + 1000, data[3], data[4] * 2)
            cur.execute('DELETE FROM kofee WHERE id = {}'.format(data[0]))
            cur.execute('INSERT INTO kofee VALUES (?,?,?,?,?)', new_data)
        self.con.commit()
    
    def update_elems(self):
        rows = list(set([i.row for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(self, '', 'Действительно заменить элементы с id' + ','.join(ids), QMessageBox.Yes,
                QMessageBox.No)
        if valid == QMessageBox.Yes:
            self.generate_new_elems(ids)
            
    def delete_elem(self):
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        if valid == QMessageBox.Yes:
            cur = self.con.cursor()
            cur.execute("DELETE FROM kofee WHERE id IN (" + ", ".join(
                '?' * len(ids)) + ")", ids)
            self.con.commit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
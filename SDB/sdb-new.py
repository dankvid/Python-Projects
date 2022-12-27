import json
from pathlib import Path

from PyQt6 import QtCore, QtWidgets
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QComboBox, QGridLayout, QLabel, QLineEdit,
                             QListWidget, QMainWindow, QMessageBox,
                             QPushButton, QWidget)


class Window(QMainWindow):
    def __init__(self):

        super().__init__()
        self.setMinimumSize(QSize(350, 200))
        self.setWindowTitle('Series Database')
        
        # Grid-Layout
        wid = QWidget(self)
        self.setCentralWidget(wid)
        grid = QGridLayout()
        wid.setLayout(grid)

        # ComboBox
        self.cb = QComboBox()
        self.setCentralWidget(wid)
        for series in data:
            self.cb.addItem(series['title'])
        self.cb.currentIndexChanged.connect(self.comboIndexChanged)
        grid.addWidget(self.cb, 1, 1)

        # Labels and Buttons
        self.lbl1 = QLabel('Series')
        grid.addWidget(self.lbl1, 2, 1)
        self.lbl2 = QLabel('Season')
        grid.addWidget(self.lbl2, 3, 1)
        self.lbl3 = QLabel('Episode')
        grid.addWidget(self.lbl3, 4, 1)
        b = QPushButton('Quit')
        b.clicked.connect(self.quit)
        grid.addWidget(b, 5, 2, Qt.AlignmentFlag.AlignRight)
        a = QPushButton('Save')
        a.clicked.connect(self.save)
        grid.addWidget(a, 5, 1, Qt.AlignmentFlag.AlignLeft)
        c = QPushButton('Add')
        c.clicked.connect(self.add)
        grid.addWidget(c, 1, 2, Qt.AlignmentFlag.AlignRight)

        # textfields
        self.txt1 = QLineEdit()
        grid.addWidget(self.txt1, 2, 2)
        self.txt2 = QLineEdit()
        grid.addWidget(self.txt2, 3, 2)
        self.txt3 = QLineEdit()
        grid.addWidget(self.txt3, 4, 2)

    # choose ComboBox
    def comboIndexChanged(self, index):
        self.txt1.setText(data[index]['title'])
        self.txt2.setText(str(data[index]['season']))
        self.txt3.setText(str(data[index]['episode']))

    # save DB
    def save(self):
        comboindex = self.cb.currentIndex()
        data[comboindex]['title'] = self.txt1.text()
        data[comboindex]['season'] = int(self.txt2.text())
        data[comboindex]['episode'] = int(self.txt3.text())
        json.dump(data, open('series.json', 'w'),indent=4,sort_keys=True)
        print('data saved')

    def add(self):
        title = self.txt1.text()
        season = int(self.txt2.text())
        episode = int(self.txt3.text())

        data.append({
            'title': title,
            'season': season,
            'episode': episode
        })
        json.dump(data, open('series.json', 'w'),indent=4,sort_keys=True)
        print('data saved')
        self.cb.addItem(title)

    # Quit-Button
    def quit(self):
        app.quit()


# receive data from JSON
f = open('series.json', 'r')
data = json.load(f)
f.close()

# quit if window closed        
app = QtWidgets.QApplication([])
app.setStyleSheet(Path("sdbStyle.qss").read_text())
win = Window()
win.show()
app.exec()

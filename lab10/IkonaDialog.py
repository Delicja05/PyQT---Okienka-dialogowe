from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from modulGlowny import *

class IkonaDialog(QDialog):
    def __init__(self, parent = None):
        super(IkonaDialog, self).__init__(parent)
        QDialog.__init__(self, parent)
        self.setModal(True)        

        self.plik = parent.getPlik()

        mainLayout = QHBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0,0,0,0)

        self.vbox1 = QVBoxLayout()
        self.vbox1.setSpacing(15)

        self.label1 = QLabel("Wybierz ikone")

        self.radio_button_wesola = QRadioButton('wesola')
        self.radio_button_normalna = QRadioButton('normalna')
        self.radio_button_smutna = QRadioButton('smutna')        

        self.radio_button_group = QButtonGroup()
        self.radio_button_group.addButton(self.radio_button_wesola)
        self.radio_button_group.addButton(self.radio_button_normalna)
        self.radio_button_group.addButton(self.radio_button_smutna)

        self.radio_button_wesola.toggled.connect(self.toggle)
        self.radio_button_normalna.toggled.connect(self.toggle)
        self.radio_button_smutna.toggled.connect(self.toggle)

        self.label2 = QLabel("Wybierz ikone")

        self.checkBox_wesola = QCheckBox('wesola')
        self.checkBox_normalna = QCheckBox('normalna')
        self.checkBox_smutna = QCheckBox('smutna')

        self.setstyl(self.checkBox_wesola)
        self.setstyl(self.checkBox_smutna)
        self.setstyl(self.checkBox_normalna)

        self.bg = QButtonGroup()
        self.bg.addButton(self.checkBox_wesola,1)
        self.bg.addButton(self.checkBox_normalna,2)
        self.bg.addButton(self.checkBox_smutna,3)

        self.vbox1.addWidget(self.label1)

        self.vbox1.addWidget(self.radio_button_wesola)
        self.vbox1.addWidget(self.radio_button_normalna)
        self.vbox1.addWidget(self.radio_button_smutna)

        self.vbox1.addWidget(self.label2)

        self.vbox1.addWidget(self.checkBox_wesola)
        self.vbox1.addWidget(self.checkBox_normalna)
        self.vbox1.addWidget(self.checkBox_smutna)

        widget1 = QWidget()
        widget1.setLayout(self.vbox1)
        widget1.setFixedWidth(100)
        
        mainLayout.addWidget(widget1, 0, Qt.AlignTop)

        self.vbox2 = QVBoxLayout()
        self.vbox2.setSpacing(5)

        self.photo = QLabel(self)
        self.fileName = self.plik

        self.progressBar = QProgressBar()
        self.progressBar.setOrientation(Qt.Vertical)
        self.label3 = QLabel("Wskaznik zadowolenia")

        self.vbox2.addWidget(self.photo)
        self.vbox2.addWidget(self.progressBar)
        self.vbox2.addWidget(self.label3)

        widget2 = QWidget()
        widget2.setLayout(self.vbox2)
        widget2.setFixedWidth(150)
        
        mainLayout.addWidget(widget2, 1, Qt.AlignTop)

        self.vbox3 = QVBoxLayout()
        self.vbox3.setSpacing(5)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Vertical, self)

        self.buttons.accepted.connect(self.clickok)
        self.buttons.rejected.connect(self.clickcancel)

        self.vbox3.addWidget(self.buttons)

        widget3 = QWidget()
        widget3.setLayout(self.vbox3)
        
        mainLayout.addWidget(widget3, 2, Qt.AlignTop)

        self.przycisk1 = ''

        self.setLayout(mainLayout)

        self.setWindowTitle("Wybierz ikone")
        self.setGeometry(150, 150, 250, 10)
        self.zaznacz()
        self.toggle()

    def setstyl(self,check):
        check.setStyleSheet('color: black')
        check.setEnabled(False)

    def zaznacz(self):
        if 'wesola' in self.plik:
            self.radio_button_wesola.setChecked(True)
            #self.checkBox_wesola.setChecked(True)
        elif 'normalna' in self.plik:
            self.radio_button_normalna.setChecked(True)
            #self.checkBox_normalna.setChecked(True)
        elif 'smutna' in self.plik:
            self.radio_button_smutna.setChecked(True)
            #self.checkBox_normalna.setChecked(True)

    def toggle(self):
        if self.radio_button_wesola.isChecked() == True:            
            self.checkBox_wesola.setChecked(True)
            self.progressBar.setValue(100)
            self.photo.setPixmap(QPixmap('wesola.png'))
            self.fileName = 'wesola.png'
        if self.radio_button_normalna.isChecked() == True:            
            self.checkBox_normalna.setChecked(True)
            self.progressBar.setValue(50)
            self.photo.setPixmap(QPixmap('normalna.png'))
            self.fileName = 'normalna.png'
        if self.radio_button_smutna.isChecked() == True:
            self.checkBox_smutna.setChecked(True)
            self.progressBar.setValue(10)
            self.photo.setPixmap(QPixmap('smutna.png'))
            self.fileName = 'smutna.png'

    def clickok(self):
        self.przycisk1 = 'Ok'
        self.accept()

    def clickcancel(self):
        self.przycisk1 = 'Cancel'
        self.reject()

    def getIkona(self):
        if self.przycisk1 == 'Ok':
            return self.fileName
        else:
            return ''

    def main(parent = None, plik = None):
        dialog = IkonaDialog(parent)
        dialog.show()
        dialog.exec()
        file = dialog.getIkona()
        return (file)

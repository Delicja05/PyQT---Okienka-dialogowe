from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from modulGlowny import *

class KoloDialog(QDialog):
    def __init__(self, parent = None):
        super(KoloDialog, self).__init__(parent)
        QDialog.__init__(self, parent)
        self.setModal(True)        

        mainLayout = QVBoxLayout()
        mainLayout.setSpacing(0)
        mainLayout.setContentsMargins(0,0,0,0)

        self.hbox0 = QHBoxLayout()
        self.hbox0.setSpacing(5)
        self.hbox0.setContentsMargins(0,0,0,0)

        self.vbox1 = QVBoxLayout()
        self.vbox1.setSpacing(5)

        self.hbox1 = QHBoxLayout()
        self.hbox1.setSpacing(5)

        self.label1 = QLabel("Na zewnatrz")

        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.setMaximum(100)
        self.slider1.valueChanged.connect(self.valuechange)
        
        self.line1 = QLineEdit()
        self.line1.setFixedWidth(25)
        self.line1.setValidator(QIntValidator())
        self.line1.textChanged.connect(self.textchanged)

        self.hbox1.addWidget(self.label1)
        self.hbox1.addWidget(self.slider1)
        self.hbox1.addWidget(self.line1)

        self.hbox2 = QHBoxLayout()
        self.hbox2.setSpacing(5)

        self.label2 = QLabel("   Wewnatrz")

        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMaximum(100)
        self.slider2.valueChanged.connect(self.valuechange)

        self.line2 = QLineEdit()
        self.line2.setFixedWidth(25)
        self.line2.setValidator(QIntValidator())
        self.line2.textChanged.connect(self.textchanged)

        self.hbox2.addWidget(self.label2)
        self.hbox2.addWidget(self.slider2)
        self.hbox2.addWidget(self.line2)

        widget1 = QWidget()
        widget1.setLayout(self.hbox1)
        widget1.setFixedWidth(200)

        widget2 = QWidget()
        widget2.setLayout(self.hbox2)
        widget2.setFixedWidth(200)
        
        self.vbox1.addWidget(widget1, 0, Qt.AlignTop)
        self.vbox1.addWidget(widget2, 1, Qt.AlignTop)

        widget3 = QWidget()
        widget3.setLayout(self.vbox1)
        widget3.setFixedWidth(200)
        
        self.hbox0.addWidget(widget3, 0, Qt.AlignTop)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 110, 110)

        self.Margin, self.Radius, self.Grubo = parent.getDane()

        self.ellipse = QGraphicsEllipseItem(QRectF(self.Margin, self.Margin, self.Radius, self.Radius))
        self.Pen = QPen(Qt.black, self.Grubo, Qt.SolidLine)
        self.ellipse.setPen(self.Pen)
        self.Brush = QBrush(Qt.green, Qt.SolidPattern)
        self.ellipse.setBrush(self.Brush)

        self.scene.addItem(self.ellipse)

        self.view = QGraphicsView()
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setScene(self.scene)
        self.view.setFocusPolicy(Qt.NoFocus)

        self.hbox0.addWidget(self.view, 1, Qt.AlignTop)

        widget0 = QWidget()
        widget0.setLayout(self.hbox0)

        mainLayout.addWidget(widget0, 0, Qt.AlignCenter)

        self.buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel, Qt.Horizontal, self)

        self.buttons.accepted.connect(self.clickok)
        self.buttons.rejected.connect(self.clickcancel)

        mainLayout.addWidget(self.buttons, 1, Qt.AlignCenter)

        self.przycisk = ''

        self.setLayout(mainLayout)

        self.setWindowTitle("Ustaw kola")
        self.setGeometry(150, 150, 320, 160)
        self.ustaw()

    def ustaw(self):
        grubo = self.Grubo
        self.line1.insert(str(round(self.Radius)))
        self.line2.insert(str(round(grubo)))

    def textchanged(self,text):
        if self.line1.text() != '':
            self.slider1.setValue(int(self.line1.text()))
            self.Radius = self.slider1.value()
            self.Margin = (110 - self.Radius)/2
            self.slider2.setMaximum(int(self.line1.text()))
        if self.line2.text() != '':
            self.slider2.setValue(int(self.line2.text()))
            self.Grubo = self.slider2.value()

        self.nowaScena(self.Margin, self.Radius, self.Grubo)

    def nowaScena(self, M, R, G):
        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(0, 0, 110, 110)

        self.ellipse = QGraphicsEllipseItem(QRectF(M, M, R, R))
        self.Pen = QPen(Qt.black, G, Qt.SolidLine)
        self.ellipse.setPen(self.Pen)
        self.Brush = QBrush(Qt.green, Qt.SolidPattern)
        self.ellipse.setBrush(self.Brush)

        self.scene.addItem(self.ellipse)
        self.view.setScene(self.scene)

    def valuechange(self):
        self.line1.setText(str(self.slider1.value()))
        self.line2.setText(str(self.slider2.value()))

    def clickok(self):
        self.przycisk = 'Ok'
        self.accept()

    def clickcancel(self):
        self.przycisk = 'Cancel'
        self.reject()

    def pobierzDane(self):
        if self.przycisk == 'Ok':
            return (self.Radius, self.Grubo)
        else:
            return ('', '')

    def main(parent = None, radius = None, grubo = None):
        dialog = KoloDialog(parent)
        dialog.show()
        dialog.exec()
        d1, d2 = dialog.pobierzDane()
        return (d1, d2)

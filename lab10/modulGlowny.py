from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
from IkonaDialog import *
from KoloDialog import *

class modulGlowny(QMainWindow):
    def __init__(self, partent = None):
        super(modulGlowny, self).__init__(partent)

        self.setupMenus()
        self.interfejs()

    def interfejs(self):
        
        self.mainLayout = QHBoxLayout()
        self.mainLayout.setSpacing(0)
        self.mainLayout.setContentsMargins(0,0,0,0)

        self.scene = QGraphicsScene(self)
        self.scene.setSceneRect(40, 40, 210, 210)
        self.scene.setBackgroundBrush(Qt.green)

        self.margin = 100
        self.radius = 100
        self.grubo = 20

        self.rectf = QRectF(self.margin, self.margin, self.radius, self.radius)
        self.ellipse = QGraphicsEllipseItem(self.rectf)
        self.pen = QPen(Qt.black, self.grubo, Qt.SolidLine)
        self.ellipse.setPen(self.pen)
        self.brush = QBrush(Qt.green, Qt.SolidPattern)
        self.ellipse.setBrush(self.brush)

        self.scene.addItem(self.ellipse)

        self.view = QGraphicsView()
        self.view.setRenderHint(QPainter.Antialiasing)
        self.view.setScene(self.scene)
        self.view.setFocusPolicy(Qt.NoFocus)

        self.mainLayout.addWidget(self.view)

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)
                

        self.items = QListWidget()
        self.lista = ['Nazwa1', 'Nazwa2', 'Nazwa3']
        self.items.addItems(self.lista)

        self.plik = 'wesola.png'

        self.input = QInputDialog()
        self.input.setOption(QInputDialog.NoButtons)
        self.input.setComboBoxItems(self.lista)
        self.input.setComboBoxEditable(True)
        self.input.setWindowTitle('Nazwa okna glownego ...')
        self.input.setLabelText('Nazwa:')
        self.input.resize(300, 50)
        self.input.move(150,150)
        self.input.installEventFilter(self)

        self.setGeometry(70, 70, 450, 300)
        self.setWindowIcon(QIcon(self.plik))
        self.setWindowTitle("Dialogi")  
    

    def nazwaMenu(self, state):
    	if state:
    		self.input.show()
    	else:
    		self.input.hide()

    def eventFilter(self, obj, event):
    	if obj is self.input:
    		if event.type() == QEvent.KeyPress:
    			if event.key() in (Qt.Key_Return, Qt.Key_Escape, Qt.Key_Enter):
    				self.setWindowTitle(self.input.textValue())
    				return True
    		if event.type() == QEvent.Close:
    			event.ignore()
    			return True
    	return super(modulGlowny, self).eventFilter(obj, event)

    def koloMenu(self):
    	zm1, zm2 = KoloDialog.main(self, self.radius, self.grubo)
    	if zm1 != '':
            self.margin = (210-zm1*2)/2
            self.radius = zm1*2
            self.grubo = zm2*2

            self.scena(self.margin, self.radius, self.grubo)            

    def scena(self, m, r, g):
    	self.scene = QGraphicsScene(self)
    	self.scene.setSceneRect(0, 0, 210, 210)
    	self.scene.setBackgroundBrush(Qt.green)

    	self.rectf = QRectF(m, m, r, r)
    	self.ellipse = QGraphicsEllipseItem(self.rectf)
    	self.pen = QPen(Qt.black, g, Qt.SolidLine)
    	self.ellipse.setPen(self.pen)
    	self.brush = QBrush(Qt.green, Qt.SolidPattern)
    	self.ellipse.setBrush(self.brush)

    	self.scene.addItem(self.ellipse)
    	self.view.setScene(self.scene)

    def getDane(self):
        return ((110 - self.radius/2)/2, self.radius/2, self.grubo/2)

    def ikonaMenu(self):
    	zmienna = IkonaDialog.main(self, self.plik)
    	if zmienna != '':
            self.plik = zmienna
            self.setWindowIcon(QIcon(zmienna))

    def getPlik(self):
    	return self.plik

    def setupMenus(self):

        self.dialogMenu = self.menuBar().addMenu("Dialog")
        self.dialogMenu.addSeparator()
        
        self.nazwaAction = QAction("Nazwa okna glownego", self, checkable = True)
        self.koloAction = QAction("Ustaw kola", self)
        self.ikonaAction = QAction("Zmien ikone", self)

        self.nazwaAction.triggered.connect(self.nazwaMenu)
        self.koloAction.triggered.connect(self.koloMenu)
        self.ikonaAction.triggered.connect(self.ikonaMenu)
        
        self.dialogMenu.addAction(self.nazwaAction)
        self.dialogMenu.addAction(self.koloAction)
        self.dialogMenu.addAction(self.ikonaAction)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    okno = modulGlowny()
    okno.show()
    sys.exit(app.exec_())

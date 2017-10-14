from PyQt5.QtWidgets import QMainWindow, QDockWidget, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QGraphicsProxyWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen, QColor, QCursor, QWindow
from PyQt5.QtCore import *
from NodeGraphicsView import FFNodeGraphicsView
from PinItem import  FFPinItem
from PyQt5.QtWinExtras import QtWin
from TabTest import FFTabWidget

class FFMainWindow(QMainWindow):
    def __init__(self):
        super(FFMainWindow, self).__init__()

    def createMenus(self):
        self.menuBar().addMenu(self.tr("&File"))

    def createToolbar(self):
        self.addToolBar(self.tr("&File"))

    def setUp(self):
        self.resize(1024, 768)
        self.createMenus()
        self.createToolbar()
        #widget = QWidget(self)

        tabs = QTabWidget(self)
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.move(100, 100)

        #centerDockWidget = QDockWidget(self.tr("Workspace"), self)
        #self.addDockWidget(Qt.RightDockWidgetArea)
        '''workSpaceView = FFNodeGraphicsView(self)
        self.setCentralWidget(workSpaceView)
        workSpaceView.lower()'''

        tabWidget = FFTabWidget(self)
        self.setCentralWidget(tabWidget)

        dockProject = QDockWidget(self.tr("工程"), self)
        treeView = QTreeView(self)
        dockProject.setWidget(treeView)
        self.addDockWidget(Qt.LeftDockWidgetArea, dockProject)
        dockProject.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        dockProject.setFeatures(QDockWidget.DockWidgetMovable)

        dockInspector = QDockWidget(self.tr("属性"), self)
        tableWidget = QTableWidget(0, 2)
        dockInspector.setWidget(tableWidget)
        self.addDockWidget(Qt.RightDockWidgetArea, dockInspector)
        dockInspector.setAllowedAreas(Qt.RightDockWidgetArea | Qt.LeftDockWidgetArea)
        dockInspector.setFeatures(QDockWidget.DockWidgetMovable)

        '''attachWindow = QWindow.fromWinId(0x00F012AC)#Qt.FramelessWindowHint |
        attachWindow.setFlags(Qt.CustomizeWindowHint | Qt.WindowTitleHint)
        winContainer = QWidget.createWindowContainer(attachWindow, self)
        winContainer.setFixedSize(800, 600)
        winContainer.move(100, 100)'''

        '''
        unityItem = QGraphicsProxyWidget()
        unityItem.setWidget(winContainer)
        wordScene.addItem(unityItem)
        unityItem.setPos(10050, 10050)'''

        '''self.setObjectName("MainWindow")
        self.resize(800, 600)
        self.centralwidget1 = QWidget(self)
        self.centralwidget1.setObjectName("centralwidget")
        self.graphicsView_2 = QGraphicsView(self.centralwidget1)
        self.graphicsView_2.setGeometry(QRect(270, 210, 391, 192))
        self.graphicsView_2.setObjectName("graphicsView_2")
        self.setCentralWidget(self.centralwidget1)

        self.retranslateUi(self)
        QMetaObject.connectSlotsByName(self)'''

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

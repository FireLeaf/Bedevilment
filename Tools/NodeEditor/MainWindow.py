from PyQt5.QtWidgets import QMainWindow, QDockWidget, QGraphicsView, QGraphicsScene, QGraphicsLineItem, QWidget, QGraphicsProxyWidget
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPen, QColor, QCursor, QWindow
from PyQt5.QtCore import *
from NodeGraphicsView import FFNodeGraphicsView
from PinItem import  FFPinItem
from PyQt5.QtWinExtras import QtWin

class FFDragableGraphicItem(QGraphicsItem):
    def __init__(self, parent, *args, **kwargs):
        super(QGraphicsItem, self).__init__(parent, *args, **kwargs)
        #self.setAcceptHoverEvents(True)
        self._isMouseDown = False
        self._isSelected = False

    def boundingRect(self):
        return QRectF(0, 0, 200, 150)

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.fillRect(self.boundingRect(), QColor(255, 215, 0))
        if self._isSelected:
            painter.setPen(QColor(0, 255, 0))
            painter.drawRect(self.boundingRect())
        #pass

    def hoverEnterEvent(self, event):
        cursor = QCursor(Qt.OpenHandCursor)
        QApplication.instance().setOverrideCursor(cursor)
        print("Here1")

    def hoverLeaveEvent(self, event):
        QApplication.instance().restoreOverrideCursor()
        print("Here3")

    def mouseMoveEvent(self, event):
        if self._isMouseDown:
            QApplication.instance().restoreOverrideCursor()
            cursor = QCursor(Qt.OpenHandCursor)
            QApplication.instance().setOverrideCursor(cursor)
            new_pos = event.scenePos()
            delta_pos = new_pos - self.oldScenePos
            self.oldScenePos = new_pos

            self.setPos(self.scenePos() + delta_pos)
            '''
            rect = self.boundingRect()
            old_pos = self.scenePos()
            old_pos += delta_pos
            #new_pos.setX(old_pos.x() + delta_pos)
            #new_pos.setY(old_pos.y() - rect.height() / 2)
            #self.setPos(old_pos)
            scene = self.scene()
            views = scene.views()
            view = views[0]
            old_view_pos = view.pos()
            view_pos = QPointF(old_view_pos) + (delta_pos)
            #view.move(view_pos.toPoint())

            trans = view.transform()
            lx = delta_pos.x() + trans.dx()
            ly = delta_pos.y() + trans.dy()
            view.centerOn(lx, ly)
            print(lx, ly)
            print("Here2")'''
    def setSelected(self, isSelected):
        if isSelected != self._isSelected:
            self._isSelected = isSelected
            self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._isSelected = not self._isSelected
            self._isMouseDown = True
            self.oldScenePos = event.scenePos()
            self.update()
        #pass

    def mouseReleaseEvent(self, event):
        self._isMouseDown = False
        QApplication.instance().restoreOverrideCursor()
        #pass

class FFMainWindow(QMainWindow):
    def __init__(self):
        super(FFMainWindow, self).__init__()

    def createNodeItem(self):
        nodeItem = FFDragableGraphicItem(None)  # QGraphicsRectItem()

        nodeItem.setFlags(QGraphicsItem.ItemIsSelectable |
                          QGraphicsItem.ItemIsMovable)

        buttonItem = QGraphicsProxyWidget(nodeItem)
        button = QPushButton()
        buttonItem.setWidget(button)
        buttonItem.setPos(100, 100)

        labelItem = QGraphicsProxyWidget(nodeItem)
        label = QLabel()
        label.setText("Hello World")
        labelItem.setWidget(label)
        labelItem.setPos(50, 50)

        inputItem = QGraphicsProxyWidget(nodeItem)
        input = QLineEdit()
        inputItem.setWidget(input)

        pinItem = FFPinItem(nodeItem)
        pinItem.setPos(0, 80)

        pinItem = FFPinItem(nodeItem)
        pinItem.setPos(188, 80)

        return nodeItem

    def setUp(self):
        self.resize(1024, 768)

        #widget = QWidget(self)

        tabs = QTabWidget(self)
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.addTab(QLabel("Hello"), "Hello")
        tabs.move(100, 100)

        #centerDockWidget = QDockWidget(self.tr("WorkSpace"), self)
        #self.addDockWidget(Qt.RightDockWidgetArea)
        workSpaceView = FFNodeGraphicsView(self)
        wordScene = QGraphicsScene()
        workSpaceView.setScene(wordScene)
        workSpaceView.setSceneRect(0, 0, 100000, 100000)
        #workSpace.setBaseSize(1000, 1000)
        self.setCentralWidget(workSpaceView)
        lineItem = QGraphicsLineItem()
        lineItem.setLine(0, 0, 100, 100)
        lineItem.setPen(QPen(Qt.black))
        wordScene.addItem(lineItem)
        lineItem.setPos(10000, 10000)

        nodeItem = self.createNodeItem()
        wordScene.addItem(nodeItem)
        nodeItem.setPos(10000, 10000)

        nodeItem = self.createNodeItem()
        wordScene.addItem(nodeItem)
        nodeItem.setPos(10050, 10050)

        #wordScene.setFocusItem(lineItem)
        workSpaceView.centerOn(nodeItem)
        workSpaceView.scale(2.0, 2.0)
        workSpaceView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        workSpaceView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        workSpaceView.lower()

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

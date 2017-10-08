from PyQt5.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsPathItem, QGraphicsRectItem, QTabBar, QGraphicsScene, QGraphicsLineItem
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.Qt import QWheelEvent, QPainterPath
from PyQt5.QtGui import *
from PinItem import  FFPinItem
from Utility.Log import FFLog

import MainWindow

class FFDragableGraphicItem(QGraphicsItem):
    def __init__(self, parent, *args, **kwargs):
        super(FFDragableGraphicItem, self).__init__(parent, *args, **kwargs)
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

    def itemChange(self, change, Any):
        if change == QGraphicsItem.ItemPositionHasChanged:
            FFLog.Logger().info("Position changed")
        return super(FFDragableGraphicItem, self).itemChange(change, Any)

    def hoverEnterEvent(self, event):
        cursor = QCursor(Qt.OpenHandCursor)
        QApplication.instance().setOverrideCursor(cursor)
        FFLog.Logger().debug("Here1")

    def hoverLeaveEvent(self, event):
        QApplication.instance().restoreOverrideCursor()
        FFLog.Logger().debug("Here3")

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

class FFNodeGraphicsView(QGraphicsView):
    def __init__(self, parent):
        super(FFNodeGraphicsView, self).__init__(parent)
        self._press = False
        self.bezierItem = None
        self.regionItem = None

        wordScene = QGraphicsScene()
        self.wordScene = wordScene
        self.setScene(wordScene)
        self.setSceneRect(0, 0, 100000, 100000)
        # workSpace.setBaseSize(1000, 1000)

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

        # wordScene.setFocusItem(lineItem)
        self.centerOn(nodeItem)
        self.scale(2.0, 2.0)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

    def createNodeItem(self):
        nodeItem = FFDragableGraphicItem(None)  # QGraphicsRectItem()

        nodeItem.setFlags(QGraphicsItem.ItemSendsGeometryChanges)

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

        pinItem = FFPinItem()
        pinItem.setPos(0, 80)
        pinItem.setParentItem(nodeItem)

        pinItem = FFPinItem()
        pinItem.setPos(188, 80)
        pinItem.setParentItem(nodeItem)

        return nodeItem

    def wheelEvent(self, event):
        #QGraphicsView.wheelEvent(self, event)
        if True or event.isAccepted():
            delta = event.angleDelta().y()
            #self.transform().
            if delta > 0:
                self.scale(1.1, 1.1)
            else:
                self.scale(0.9, 0.9)

            print(event.angleDelta())

    def mouseMoveEvent(self, event):

        if self.bezierItem != None:
            self.rebuildBerizer(event)
        elif self.regionItem != None:
            self.rebuildRect(event)
        elif not self._press:
            QGraphicsView.mouseMoveEvent(self, event)
        elif True or not event.isAccepted():
            self._oldCenter = self.mapToScene(self.viewport().rect().center())
            newMousePos = event.pos()
            deltaPos = self.mapToScene(newMousePos) - self.mapToScene(self._oldMousePos)
            #self._oldMousePos = newMousePos
            self.centerOn(self._oldSceneCenter - deltaPos)
            #self._oldSceneCenter = self.mapToScene(self.viewport().rect().center())
            #print(deltaPos, center + deltaPos)
    def rebuildBerizer(self, event):
        bezierPath = QPainterPath()
        bezierPath.moveTo(0, 0)
        endPos = self.bezierItem.mapFromScene(self.mapToScene(event.pos()))
        factor = 0.6
        ctrl1 = QPointF(endPos.x() * factor, 0)
        ctrl2 = QPointF(endPos.x() * (1 - factor), endPos.y())
        bezierPath.cubicTo(ctrl1, ctrl2, endPos)
        self.bezierItem.setPath(bezierPath)

    def rebuildRect(self, event):
        #rect = QRectF()
        endPos = self.regionItem.mapFromScene(self.mapToScene(event.pos()))
        self.regionItem.setRect(0, 0, endPos.x(), endPos.y())

    def mousePressEvent(self, event):
        QGraphicsView.mousePressEvent(self, event)
        if not event.isAccepted():
            if event.button() == Qt.MiddleButton:
                print("view press")
                self._press = True
                #self._oldCenter = self.viewport().rect().center()
                self._oldMousePos = event.pos()
                self._oldSceneCenter = self.mapToScene(self.viewport().rect().center())
            elif event.button() == Qt.LeftButton:
                selectItems = self.scene().items(self.mapToScene(event.pos()), Qt.IntersectsItemShape)
                for item in selectItems:
                    if isinstance(item, QGraphicsPathItem):
                        pen = QPen(QColor(0x00, 0xff, 0x00))
                        pen.setWidth(2)
                        item.setPen(pen)
                return ;

                startPos = self.mapToScene(event.pos())
                self.bezierItem = QGraphicsPathItem()
                path = QPainterPath()
                self.bezierItem.setPath(path)
                self.scene().addItem(self.bezierItem)
                self.bezierItem.setPos(startPos)
                self.rebuildBerizer(event)
            elif event.button() == Qt.RightButton:
                startPos = self.mapToScene(event.pos())
                self.regionItem = QGraphicsRectItem()
                self.scene().addItem(self.regionItem)
                self.regionItem.setPos(startPos)
                self.rebuildRect(event)

    def mouseReleaseEvent(self, event):
        QGraphicsView.mouseReleaseEvent(self, event)
        if self._press:
            print("view release")
            self._press = False
        if self.bezierItem != None:
            self.bezierItem = None
        if self.regionItem != None:
            rect = self.regionItem.mapToScene(self.regionItem.rect())
            selectItems = self.scene().items(rect, Qt.ContainsItemBoundingRect)
            for item in selectItems:
                if isinstance(item, MainWindow.FFDragableGraphicItem):
                    item.setSelected(True)
            self.scene().removeItem(self.regionItem)
            self.regionItem = None

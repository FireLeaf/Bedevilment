from PyQt5.QtWidgets import QGraphicsView, QGraphicsPathItem, QGraphicsRectItem
from PyQt5.QtCore import *
from PyQt5.Qt import QWheelEvent, QPainterPath
from PyQt5.QtGui import *

import MainWindow

class FFNodeGraphicsView(QGraphicsView):
    def __init__(self, parent):
        super(FFNodeGraphicsView, self).__init__(parent)
        self._press = False
        self.bezierItem = None
        self.regionItem = None

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

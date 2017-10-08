from PyQt5.QtWidgets import  *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.Qt import *

class FFPinItem(QGraphicsPixmapItem):
    def __init__(self):
        super(FFPinItem, self).__init__()
        pixmap = QPixmap()
        pixmap.load("Res/pin.png")
        self.setPixmap(pixmap)
        self.bezierItem = None

    def rebuildBerizer(self, event):
        bezierPath = QPainterPath()
        bezierPath.moveTo(0, 0)
        endPos = self.bezierItem.mapFromScene(self.mapToScene(event.pos()))
        factor = 0.6
        ctrl1 = QPointF(endPos.x() * factor, 0)
        ctrl2 = QPointF(endPos.x() * (1 - factor), endPos.y())
        bezierPath.cubicTo(ctrl1, ctrl2, endPos)
        self.bezierItem.setPath(bezierPath)

    def mousePressEvent(self, event):
        startPos = self.mapToScene(event.pos())
        self.bezierItem = QGraphicsPathItem()
        path = QPainterPath()
        self.bezierItem.setPath(path)
        self.scene().addItem(self.bezierItem)
        br = self.boundingRect()
        #QRectF.height()
        deltaPos = QPointF(br.width() / 2, br.height() / 2)
        self.bezierItem.setPos(self.scenePos() + deltaPos)
        self.rebuildBerizer(event)
        pen = self.bezierItem.pen()
        pen.setWidth(2)
        self.bezierItem.setPen(pen)
        event.accept()

    def mouseMoveEvent(self, event):
        if self.bezierItem != None:
            self.rebuildBerizer(event)
            event.accept()

    def mouseReleaseEvent(self, event):

        selectItems = self.scene().items(event.scenePos(), Qt.ContainsItemBoundingRect)
        for item in selectItems:
            if isinstance(item, FFPinItem):
                self.bezierItem = None
                break
        if self.bezierItem != None:
            self.scene().removeItem(self.bezierItem)
            self.bezierItem = None
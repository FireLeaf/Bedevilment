from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QColor, QCursor
from PyQt5.QtCore import QRect
from PyQt5.Qt import Qt, QApplication
import time

class FFNodeGraphicsItem(QGraphicsItem):
    def __init__(self, parent, *args, **kwargs):
        super(QGraphicsItem, self).__init__(parent, *args, **kwargs)
        # self.setAcceptHoverEvents(True)
        self._IsLeftMouseDown = False
        self._IsMidMouseDown = False
        self._IsRightMouseDown = False
        self._LastMouseDownTime = 0
        self._IsSelected = False
        self._BoundingRect = QRect(0, 0, 0, )

    def boundingRect(self):
        return self._BoundingRect

    def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
        painter.fillRect(self.boundingRect(), QColor(255, 215, 0))
        if self._isSelected:
            painter.setPen(QColor(0, 255, 0))
            painter.drawRect(self.boundingRect())
            # pass

    def itemChange(self, change, Any):
        if change == QGraphicsItem.ItemPositionHasChanged:
            print("Position changed")
        return super(FFNodeGraphicsItem, self).itemChange(change, Any)

    def cloneItem(self):
        pass

    def mouseMoveEvent(self, event):
        if self._isMouseDown:
            QApplication.instance().restoreOverrideCursor()
            cursor = QCursor(Qt.OpenHandCursor)
            QApplication.instance().setOverrideCursor(cursor)
            new_pos = event.scenePos()
            delta_pos = new_pos - self.oldScenePos
            self.oldScenePos = new_pos
            self.setPos(self.scenePos() + delta_pos)

    def setSelected(self, isSelected):
        if isSelected != self._isSelected:
            self._isSelected = isSelected
            self.update()

    def mousePressEvent(self, event):
        self._LastMouseDownTime = time.time()
        self.oldScenePos = event.scenePos()

        if event.button() == Qt.LeftButton:
            self._IsLeftMouseDown   = True
            self._IsMidMouseDown    = False
            self._IsRightMouseDown  = False
        elif event.button() == Qt.MiddleButton:
            self._IsLeftMouseDown   = False
            self._IsMidMouseDown    = True
            self._IsRightMouseDown  = False
        elif event.button() == Qt.RightButton:
            self._IsLeftMouseDown   = False
            self._IsMidMouseDown    = False
            self._IsRightMouseDown  = True

    def mouseReleaseEvent(self, event):
        # 如果距离点击的事件不到200ms，那么判定为点击事件
        if (time.time() - self._LastMouseDownTime < 0.2):
            self.customMouseClickEvent(event)
        self._IsLeftMouseDown   = False
        self._IsMidMouseDown    = False
        self._IsRightMouseDown  = False
        QApplication.instance().restoreOverrideCursor()
        # pass

    def customMouseClickEvent(self, event):
        pass

    def mouseDoubleClickEvent(self, event):
        pass

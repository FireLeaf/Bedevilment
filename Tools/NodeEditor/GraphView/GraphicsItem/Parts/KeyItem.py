from PyQt5.QtWidgets import  QGraphicsPixmapItem
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPainterPath
from PyQt5.Qt import *

from GraphView.Help.ResUtil import FFResUtil

class FFKeyItem(QGraphicsPixmapItem):
	def __init__(self, parent, *args, **kwargs):
		super(FFKeyItem, self).__init__(parent, *args, **kwargs)
		self._BezierItem = None

	'''
		是不是输入的key， 例如 inpin, inflow
	'''
	def IsKeyIn(self):
		return False

	def RebuildBerizer(self, event):
		bezierPath = QPainterPath()
		bezierPath.moveTo(0, 0)

		endPos = self._BezierItem.mapFromScene(self.mapToScene(event.pos()))
		#print(endPos)

		xDelta = abs(endPos.x())
		if xDelta < 150:
			xDelta = 150

		cx1, cx2 = 0, 0
		factor = 0.6
		if self.IsKeyIn():
			cx1 = -xDelta * factor
			cx2 = endPos.x() + xDelta * (1.0 - factor)
		else:
			cx1 = xDelta * factor
			cx2 = endPos.x() - xDelta * (1.0 - factor)

		ctrl1 = QPointF(cx1, 0)
		ctrl2 = QPointF(cx2, endPos.y())
		bezierPath.cubicTo(ctrl1, ctrl2, endPos)
		self._BezierItem.setPath(bezierPath)

	def paint(self, QPainter, QStyleOptionGraphicsItem, QWidget):
		#QPainter.drawRect(self.boundingRect())
		super(FFKeyItem, self).paint(QPainter, QStyleOptionGraphicsItem, QWidget)

	def CreateBezierItem(self):
		self._BezierItem = QGraphicsPathItem()
		pen = self._BezierItem.pen()
		pen.setWidth(2)
		self._BezierItem.setPen(pen)
		path = QPainterPath()
		self._BezierItem.setPath(path)

	def mousePressEvent(self, event):
		startPos = self.mapToScene(event.pos())
		self.CreateBezierItem()

		self.scene().addItem(self._BezierItem)
		br = self.boundingRect()
		deltaPos = QPointF(br.width() / 2, br.height() / 2)
		self._BezierItem.setPos(self.scenePos() + deltaPos)
		self.RebuildBerizer(event)
		event.accept()

	def OnHoverItems(self, items):
		pass

	def OnReleaseItems(self, items):
		pass

	def mouseMoveEvent(self, event):
		if self._BezierItem != None:
			selectItems = self.scene().items(event.scenePos(), Qt.ContainsItemBoundingRect)
			self.OnHoverItems(selectItems)
			self.RebuildBerizer(event)
			event.accept()
		super(FFKeyItem, self).mouseMoveEvent(event)

	def mouseReleaseEvent(self, event):
		selectItems = self.scene().items(event.scenePos(), Qt.ContainsItemBoundingRect)
		self.OnReleaseItems(selectItems)

		if self._BezierItem != None:
			self.scene().removeItem(self._BezierItem)
			self._BezierItem = None
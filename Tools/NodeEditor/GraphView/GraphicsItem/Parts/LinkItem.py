from PyQt5.QtWidgets import QGraphicsPathItem, QGraphicsPixmapItem
from PyQt5.QtCore import QRectF, QPointF
from PyQt5.QtGui import QPainterPath

'''
	连接线
'''

class FFLinkItem(QGraphicsPathItem):
	def __init__(self, linkRef, inItem, outItem):
		super(FFLinkItem, self).__init__()
		self._LinkRef = linkRef
		self._InItem = inItem
		self._OutItem = outItem
		self.trackLink()
		self.setZValue(-1)

	def trackLink(self):
		pos = self._OutItem.scenePos()
		pos.setX(pos.x() + self._OutItem.boundingRect().width() / 2)
		pos.setY(pos.y() + self._OutItem.boundingRect().height() / 2)
		self.setPos(pos)

		bezierPath = QPainterPath()
		bezierPath.moveTo(0, 0)

		endPos = self.mapFromScene(self._InItem.scenePos())
		endPos.setX(endPos.x() + self._InItem.boundingRect().width() / 2)
		endPos.setY(endPos.y() + self._InItem.boundingRect().height() / 2)

		xDelta = abs(endPos.x())
		if xDelta < 150:
			xDelta = 150

		cx1, cx2 = 0, 0
		factor = 0.6
		if False:
			cx1 = -xDelta * factor
			cx2 = endPos.x() + xDelta * (1.0 - factor)
		else:
			cx1 = xDelta * factor
			cx2 = endPos.x() - xDelta * (1.0 - factor)

		ctrl1 = QPointF(cx1, 0)
		ctrl2 = QPointF(cx2, endPos.y())
		bezierPath.cubicTo(ctrl1, ctrl2, endPos)
		self.setPath(bezierPath)

		#self.update()
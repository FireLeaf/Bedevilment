from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF

from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFCallNodeItem(FFFlowNodeItem):
	def __init__(self, nodeRef):
		super(FFCallNodeItem, self).__init__(nodeRef)
		self._InPinItems = []
		self._OutPinItems = []

		self.createAllPinItems()

		self.layoutItems()
		self.repositionHead()

	def createAllPinItems(self):
		for inPin in self._NodeRef._InPins:
			pinGroupItems = FFPinGroupItem(self, inPin)
			self._InPinItems.append(pinGroupItems)
		for outPin in self._NodeRef._OutPins:
			pinGroupItems = FFPinGroupItem(self, outPin)
			self._InPinItems.append(pinGroupItems)

	def leftItems(self):
		return self._InPinItems

	def rightItems(self):
		return  self._OutPinItems

	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.setPen(QColor(0, 0, 0))
		painter.drawText(4, 16, "")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()
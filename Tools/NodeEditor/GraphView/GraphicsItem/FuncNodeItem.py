from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF


from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFFuncBeginNodeItem(FFNodeGraphicsItem):
	def __init__(self, nodeRef):
		super(FFFuncBeginNodeItem, self).__init__(nodeRef)
		self._OutFlowItem = FFFlowGroupItem(self, nodeRef._OutFlow)
		self._OutPinItems = []
		self.createAllPinItems()
		self.layoutItems()
		self.repositionHead()

	def leftItems(self):
		return []

	def rightItems(self):
		return self._OutPinItems

	def createAllPinItems(self):
		for outPin in self._NodeRef._OutPins:
			pinGroupItems = FFPinGroupItem(self, outPin)
			self._OutPinItems.append(pinGroupItems)

	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.drawText(4, 16, "[E]")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()


class FFFuncEndNodeItem(FFNodeGraphicsItem):
	def __init__(self, nodeRef):
		super(FFFuncEndNodeItem, self).__init__(nodeRef)
		self._InFlowItem = FFFlowGroupItem(self, nodeRef._InFlow)
		self._InPinItems = []
		self.createAllPinItems()
		self.layoutItems()
		self.repositionHead()

	def leftItems(self):
		return self._InPinItems

	def rightItems(self):
		return []

	def createAllPinItems(self):
		for outPin in self._NodeRef._InPins:
			pinGroupItems = FFPinGroupItem(self, outPin)
			self._InPinItems.append(pinGroupItems)

	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.setPen(QColor(0, 0, 0))
		painter.drawText(4, 16, "[E]")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()
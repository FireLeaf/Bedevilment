from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF


from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFEventNodeItem(FFNodeGraphicsItem):
	def __init__(self, nodeRef):
		super(FFEventNodeItem, self).__init__(nodeRef)
		self._OutFlowItem = FFFlowGroupItem(self, nodeRef._OutFlow)
		self._OutPinItems = []
		self.createAllPinItems()
		self.layoutItems()
		self.repositionHead()

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

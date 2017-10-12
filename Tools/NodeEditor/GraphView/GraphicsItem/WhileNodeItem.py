from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF

from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFWhileNodeItem(FFFlowNodeItem):
	def __init__(self, nodeRef):
		super(FFWhileNodeItem, self).__init__(nodeRef)

		self._CondPinItem = FFPinGroupItem(self, nodeRef._CondPin)
		self._LoopBodyFlowItem = FFFlowGroupItem(self, nodeRef._LoopBodyFlow)

		self.createAllPinItems()

		self.layoutItems()
		self.repositionHead()

	def createAllPinItems(self):
		pass

	def leftItems(self):
		return [self._CondPinItem]

	def rightItems(self):
		return  [self._LoopBodyFlowItem]

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
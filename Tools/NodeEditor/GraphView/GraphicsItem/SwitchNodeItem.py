from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF

from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFSwitchNodeItem(FFFlowNodeItem):
	def __init__(self, nodeRef):
		super(FFSwitchNodeItem, self).__init__(nodeRef)
		self._TrueFlowItem = FFFlowGroupItem(self, self._NodeRef._TrueFlow)
		self._FalseFlowItem = FFFlowGroupItem(self, self._NodeRef._FalseFlow)
		self._CondPinGroupItem = FFPinGroupItem(self, self._NodeRef._CondPin)
		#self.rebuildAllItems()
		self.layoutItems()
		self.repositionHead()

	def leftItems(self):
		return [self._CondPinGroupItem]

	def rightItems(self):
		return  [self._TrueFlowItem, self._FalseFlowItem]

	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.drawText(4, 16, "-[")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()
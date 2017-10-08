from PyQt5.QtGui import QColor, QStaticText, QPainter
from PyQt5.QtCore import QRectF

from GraphView.GraphicsItem.Base.FlowNodeItem import FFFlowNodeItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFForNodeItem(FFFlowNodeItem):
	def __init__(self, nodeRef):
		super(FFForNodeItem, self).__init__(nodeRef)
		self._StartIdxPinItem = FFPinGroupItem(self, nodeRef._StartIdxPin)
		self._EndIdxPinItem = FFPinGroupItem(self, nodeRef._EndIdxPin)
		self._StepIdxPinItem = FFPinGroupItem(self, nodeRef._StepIdxPin)
		self._LoopBodyFlowItem = FFFlowGroupItem(self, nodeRef._LoopBodyFlow)

		self.createAllPinItems()

		self.layoutItems()
		self.repositionHead()

	def createAllPinItems(self):
		pass

	def leftItems(self):
		return [self._StartIdxPinItem, self._EndIdxPinItem, self._StepIdxPinItem]

	def rightItems(self):
		return  [self._LoopBodyFlowItem]

	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.drawText(4, 16, "")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()
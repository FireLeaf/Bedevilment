from PyQt5.QtGui import QPainter, QColor

from Graph.Help.Util import *

from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
from GraphView.GraphicsItem.Parts.PinGroupItem import FFPinGroupItem
from GraphView.Help.ResUtil import FFResUtil

class FFOperationNodeItem(FFNodeGraphicsItem):
	def __init__(self, nodeRef):
		super(FFOperationNodeItem, self).__init__(nodeRef)
		self._InPinItems = []
		self._OutPinItem = None

		self.createAllPinItems()

		self.layoutItems()
		self.repositionHead()

	def leftItems(self):
		return self._InPinItems

	def rightItems(self):
		return [self._OutPinItem]

	def createAllPinItems(self):
		for pin in self._NodeRef._InPins:
			self._InPinItems.append(FFPinGroupItem(self, pin))
		self._OutPinItem = FFPinGroupItem(self, self._NodeRef._OutPin)

	'''OperationNodeRes = {
		FFNodeSubType.NST_ARITHMETIC_ADD : ,
		FFNodeSubType.NST_ARITHMETIC_SUB: ,
		FFNodeSubType.NST_ARITHMETIC_MUL: ,
		FFNodeSubType.NST_ARITHMETIC_DIV: ,

		FFNodeSubType.NST_LOGIC_AND: ,
		FFNodeSubType.NST_LOGIC_OR: ,
		FFNodeSubType.NST_LOGIC_NOT: ,

		FFNodeSubType.NST_RELATION_GT: ,
		FFNodeSubType.NST_RELATION_GE: ,
		FFNodeSubType.NST_RELATION_LT: ,
		FFNodeSubType.NST_RELATION_LE: ,
		FFNodeSubType.NST_RELATION_EQ: ,
		FFNodeSubType.NST_RELATION_NEQ: ,
	}'''
	def drawTitle(self, painter):
		#QPainter.drawPixmap(4, 4, FFResUtil.)
		painter.setPen(QColor(0, 0, 0))
		painter.drawText(4, 16, "B")
		painter.drawText(24 + 4, 16, self._NodeRef.GetName())
		painter.drawLine(0, 24, self._BoundingRect.width(), 24)

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.drawTitle(painter)
		self.trackAllLink()
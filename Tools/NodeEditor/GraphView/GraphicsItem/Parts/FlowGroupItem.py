from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel, QCheckBox, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRect, QRectF

from Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.FlowItem import FFFlowItem

class FFFlowGroupItem(QGraphicsItem):
	def __init__(self, parentItem, flowRef):
		super(FFFlowGroupItem, self).__init__()
		self._FlowRef = flowRef
		self._FlowItem = FFFlowItem(flowRef)
		self._FlowItem.setParentItem(self)
		self._NameItem = self.CreateNameItem()
		self._BoundRect = QRectF(0, 0, 0, 0)
		self.layoutWidget()
		self.setParentItem(parentItem)

	def CreateNameItem(self):
		if self._FlowRef._FlowName != "":
			nameItem = QGraphicsProxyWidget()
			nameItem.setWidget(QLabel(self._FlowRef._FlowName))
			nameItem.setParentItem(self)
			return nameItem
		return None
	GAP = 4
	def layoutWidget(self):
		w, h = 0, 0
		if self._FlowRef._FlowFlag == FFFlag.FLAG_FLOW_IN:
			self._FlowItem.setPos(self.GAP, 0)
			flowRect = self._FlowItem.boundingRect()
			nameWidth, nameHeight = 0, 0
			if self._NameItem != None:
				self._NameItem.setPos(self.GAP + flowRect.width() + self.GAP, 0)
				nameWidth = self.GAP + self._NameItem.boundingRect().width()
				nameHeight = self._NameItem.boundingRect().height()

			w = self.GAP + flowRect.width() + nameWidth
			h = max(nameHeight, flowRect.height())
		else:
			flowRect = self._FlowItem.boundingRect()
			self._FlowItem.setPos(- flowRect.width() - self.GAP, 0)
			nameWidth, nameHeight = 0, 0
			if self._NameItem != None:
				nameRect = self._NameItem.boundingRect()
				self._NameItem.setPos(- flowRect.width() - self.GAP - nameRect.width() - self.GAP, 0)
				nameWidth, nameHeight = nameRect.width() + self.GAP, nameRect.height()
			w = self.GAP + flowRect.width() + nameWidth
			h = max(flowRect.height(), nameHeight)
		self._BoundRect = QRectF(0, 0, w, h)

	def maxItemWidthHeight(self):
		gapCount = 1
		pinRect = self._PinItem.boundingRect()
		nameWidth, nameHeight = 0, 0
		if self._NameItem != None:
			nameRect = self._NameItem.boundingRect()
			nameWidth, nameHeight = nameRect.width(), nameRect.height()
			gapCount += 1
		return  int(pinRect.width() + nameWidth + gapCount * self.GAP), int(max(pinRect.height(), nameHeight))

	def boundingRect(self):
		return self._BoundRect

	def paint(self, paint, styleOption, widget=None):
		pass
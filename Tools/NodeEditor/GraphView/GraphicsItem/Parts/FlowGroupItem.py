from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel, QCheckBox, QLineEdit
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRect, QRectF

from Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.FlowItem import FFFlowItem
from GraphView.GraphicsItem.Parts.HLayoutItem import FFHLayoutItem

class FFFlowGroupItem(FFHLayoutItem):

	FLOW_GAP = 4

	def __init__(self, parentItem, flowRef):
		super(FFFlowGroupItem, self).__init__(self.FLOW_GAP)
		self._FlowRef = flowRef
		self._FlowItem = FFFlowItem(flowRef)
		self._FlowItem.setParentItem(self)
		self._NameItem = self.CreateNameItem()
		self._BoundRect = QRectF(0, 0, 0, 0)
		locationLeft = (self._FlowRef.IsInFlow())
		self.SetItems([self._FlowItem, self._NameItem], locationLeft)
		#self.layoutWidget()
		self.setParentItem(parentItem)

	def CreateNameItem(self):
		if self._FlowRef._FlowName != "":
			nameItem = QGraphicsProxyWidget()
			nameItem.setWidget(QLabel(self._FlowRef._FlowName))
			nameItem.setParentItem(self)
			return nameItem
		return None

	def paint(self, paint, styleOption, widget=None):
		pass
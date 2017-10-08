from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel, QCheckBox, QLineEdit, QGraphicsLinearLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRect, QRectF

from Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.PinItem import FFPinItem

class FFPinGroupItem(QGraphicsItem):
	GAP = 4
	def __init__(self, parentItem, pinRef):
		super(FFPinGroupItem, self).__init__()
		self._PinRef = pinRef
		self._PinItem = FFPinItem(pinRef)
		self._PinItem.setParentItem(self)
		self._NameItem = QGraphicsProxyWidget()
		self._NameItem.setWidget(QLabel(pinRef._PinName))
		self._NameItem.setParentItem(self)
		self._ValueItem = self.createValueItem()
		if self._ValueItem:
			self._ValueItem.setParentItem(self)
		self._BoundRect = QRectF(0, 0, 0, 0)
		self.layoutWidget()
		self.setParentItem(parentItem)

	def layoutWidget(self):
		w, h = 0, 0
		if self._PinRef._PinFlag == FFFlag.FLAG_PIN_IN:
			self._PinItem.setPos(self.GAP, 0)
			pinRect = self._PinItem.boundingRect()
			self._NameItem.setPos(self.GAP + pinRect.width() + self.GAP, 0)
			nameRect = self._NameItem.boundingRect()
			valueWidth, valueHeight = 0, 0
			if self._ValueItem != None:
				self._ValueItem.setPos(self.GAP + pinRect.width() + self.GAP + nameRect.width() + self.GAP, 0)
				valueWidth = self.GAP + self._ValueItem.boundingRect().width()
				valueHeight = self._ValueItem.boundingRect().height()

			w = self.GAP + pinRect.width() + self.GAP + nameRect.width() + valueWidth
			h = max(valueHeight, pinRect.height(), nameRect.height())
		else:
			pinRect = self._PinItem.boundingRect()
			self._PinItem.setPos(- pinRect.width() - self.GAP, 0)
			nameRect = self._NameItem.boundingRect()
			self._NameItem.setPos(- pinRect.width() - self.GAP - nameRect.width() - self.GAP, 0)
			w = pinRect.width() + self.GAP + nameRect.width() + self.GAP
			h = max(pinRect.height(), nameRect.height())
		self._BoundRect = QRectF(0, 0, w, h)

	def maxItemWidthHeight(self):
		gapCount = 1
		pinRect = self._PinItem.boundingRect()
		nameRect = self._NameItem.boundingRect()
		valueWidth, valueHeight = 0, 0
		if self._ValueItem != None:
			valueRect = self._ValueItem.boundingRect()
			valueWidth, valueHeight = valueRect.width(), valueRect.height()
			gapCount += 1
		return  int(pinRect.width() + nameRect.width() + valueWidth + 2 * self.GAP), int(max(pinRect.height(), nameRect.height(), valueHeight))

	def createValueItem(self):
		if self._PinRef._PinFlag != FFFlag.FLAG_PIN_IN: return

		valueWidget = None
		valueType = self._PinRef._PinValueType
		if valueType == FFType.TYPE_BOOLEAN:
			valueWidget = QCheckBox()
		elif valueType == FFType.TYPE_INT:
			valueWidget = QLineEdit()
			valueWidget.setValidator(QIntValidator())
		elif valueType == FFType.TYPE_REAL:
			valueWidget = QLineEdit()
			valueWidget.setValidator(QDoubleValidator())
		elif valueType == FFType.TYPE_NUMBER:
			valueWidget = QLineEdit()
			valueWidget.setValidator(QDoubleValidator())
		elif valueType == FFType.TYPE_STRING:
			valueWidget = QLineEdit()


		if valueWidget != None:
			valueItem = QGraphicsProxyWidget()
			valueItem.setWidget(valueWidget)
			return  valueItem
		return  None

	def boundingRect(self):
		return self._BoundRect

	def paint(self, paint, styleOption, widget=None):
		pass
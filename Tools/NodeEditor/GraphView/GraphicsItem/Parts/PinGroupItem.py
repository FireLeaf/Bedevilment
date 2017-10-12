from PyQt5.QtWidgets import QGraphicsItem, QGraphicsProxyWidget, QLabel, QCheckBox, QLineEdit, QGraphicsLinearLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtCore import QRect, QRectF

from Graph.Help.Util import *
from GraphView.GraphicsItem.Parts.PinItem import FFPinItem
from GraphView.GraphicsItem.Parts.HLayoutItem import FFHLayoutItem

class FFPinGroupItem(FFHLayoutItem):
	PIN_GAP = 4
	def __init__(self, parentItem, pinRef):
		super(FFPinGroupItem, self).__init__(self.PIN_GAP)
		self._PinRef = pinRef
		self._PinItem = FFPinItem(pinRef)
		self._PinItem.setParentItem(self)
		self._NameItem = QGraphicsProxyWidget()
		self._NameItem.setWidget(QLabel(pinRef._PinName))
		self._NameItem.setParentItem(self)
		self._ValueItem = self.createValueItem()
		if self._ValueItem:
			self._ValueItem.setParentItem(self)

		locationLeft = self._PinRef.IsInPin()
		self.SetItems([self._PinItem, self._NameItem, self._ValueItem], locationLeft)
		self.setParentItem(parentItem)


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

	def paint(self, paint, styleOption, widget=None):
		pass
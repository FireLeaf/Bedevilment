from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtGui import QColor, QCursor, QStaticText
from PyQt5.QtCore import QRect, QRectF
from PyQt5.Qt import Qt, QApplication
import time

class FFNodeGraphicsItem(QGraphicsItem):
	DEFAULT_TITLE_HEIGHT = 24 # 默认title的高度
	DEFAULT_TITLE_PIXMAP_WIDTH = 24 # 默认title里面pixmap的宽度
	DEFAULT_FLOW_HEIGHT = 24 # 默认flow的高度
	DEFAULT_FLOW_WIDTH = 24  # 默认flow的宽度
	DEFAULT_PIN_HEIGHT = 24 # 默认pin的高度
	DEFAULT_PIN_WIDTH = 24 # 默认pin的宽度

	def __init__(self, nodeRef):
		super(FFNodeGraphicsItem, self).__init__()
		# self.setAcceptHoverEvents(True)
		self._MouseBtnDown = 0
		self._LastMouseDownTime = 0
		self._IsSelected = False
		self._BoundingRect = QRect(0, 0, 0, 0)
		self._NodeRef = nodeRef
		self._PinLinks = []
		self._FlowLinks = []

		self._PinGroupItems = []
		self._LinkItems = []

	def boundingRect(self):
		return QRectF(self._BoundingRect)

	'''
		头部重定位
	'''
	def repositionHead(self):
		pass

	'''
		头部的长宽，默认只包括标题栏
	'''
	def headWidthAndHeight(self):
		titleWidth = self.DEFAULT_TITLE_PIXMAP_WIDTH + int(QStaticText(self._NodeRef.GetName()).textWidth())
		return  titleWidth, self.DEFAULT_TITLE_HEIGHT

	'''
		计算一组item的总高度以及最大宽度
	'''
	def calcHeightAndMaxWidth(self, items):
		height = 0
		maxWidth = 0
		for item in items:
			rect = item.boundingRect()
			height += rect.height()
			if maxWidth < rect.width():
				maxWidth = rect.width()
		return height, maxWidth

	'''
		排列在head以下的所有items，分左右
	'''
	def layoutItems(self):
		lefts = self.leftItems()
		rights = self.rightItems()

		headWidth, headHeight = self.headWidthAndHeight()

		leftItemsHeight, leftMaxWidth = self.calcHeightAndMaxWidth(lefts)
		rightItemsHeight, rightMaxWidth = self.calcHeightAndMaxWidth(rights)

		maxItemsHeight = max(leftItemsHeight + len(lefts) * 4, rightItemsHeight + len(rights) * 4) # 添加gap之后的高度

		leftStep = (maxItemsHeight - leftItemsHeight)  / (len(lefts) + 1)
		stepSum = headHeight + leftStep
		for itemIdx in range(0, len(lefts)):
			lefts[itemIdx].setPos(0, stepSum)
			stepSum += lefts[itemIdx].boundingRect().height() + leftStep

		maxWidth = max(headWidth, leftMaxWidth + 20 + rightMaxWidth)

		rightStep = (maxItemsHeight - rightItemsHeight) / (len(rights) + 1)
		stepSum = headHeight + rightStep
		for itemIdx in range(0, len(rights)):
			rights[itemIdx].setPos(maxWidth, stepSum)
			stepSum += rights[itemIdx].boundingRect().height() + rightStep

		self._BoundingRect.setRect(0, 0, maxWidth, maxItemsHeight + headHeight)

	'''
		获取head以下左边显示的所有item
	'''
	def leftItems(self):
		return []

	'''
		获取head以下右边显示的所有item
	'''
	def rightItems(self):
		return  []

	def drawBackground(self, painter):
		painter.fillRect(self._BoundingRect, QColor(255, 215, 0))
		if self._IsSelected:
			painter.setPen(QColor(0, 255, 0))
			painter.drawRect(self._BoundingRect)

	def drawTitle(self, painter):
		pass

	def paint(self, painter, QStyleOptionGraphicsItem, widget=None):
		self.drawBackground(painter)
		self.trackAllLink()

	def addPinLink(self, pinItemOne, pinItemTwo):
		pass

	def removePinLink(self, pinLinkItem):
		pass

	def addFlowLink(self, flowItemOne, flowItemTwo):
		pass

	def removeFlowLink(self, flowLinkItem):
		pass

	def trackAllLink(self):
		pass

	def itemChange(self, change, Any):
		if change == QGraphicsItem.ItemPositionHasChanged:
			#print("Position changed")
			self.trackAllLink()
		return super(FFNodeGraphicsItem, self).itemChange(change, Any)

	def cloneItem(self):
		pass

	def setNodePos(self, pos):
		self._NodeRef._Position = (pos.x, pos.y, 0)
		self.setPos(pos)

	def mouseMoveEvent(self, event):
		if self._MouseBtnDown == Qt.LeftButton:
			QApplication.instance().restoreOverrideCursor()
			cursor = QCursor(Qt.OpenHandCursor)
			QApplication.instance().setOverrideCursor(cursor)
			new_pos = event.scenePos()
			delta_pos = new_pos - self.oldScenePos
			self.oldScenePos = new_pos
			#self.setPos(self.scenePos() + delta_pos)
			self.setNodePos(self.scenePos() + delta_pos)
		elif self._MouseBtnDown == Qt.MiddleButton:
			pass
		elif self._MouseBtnDown == Qt.RightButton:
			pass

	def setSelected(self, isSelected):
		if isSelected != self._IsSelected:
			self._IsSelected = isSelected
			self.update()

	def mousePressEvent(self, event):
		self._LastMouseDownTime = time.time()
		self.oldScenePos = event.scenePos()

		self._MouseBtnDown = event.button()

	def mouseReleaseEvent(self, event):
		# 如果距离点击的事件不到200ms，那么判定为点击事件
		if (time.time() - self._LastMouseDownTime < 0.2):
			self.customMouseClickEvent(event)
		self._MouseBtnDown = 0
		QApplication.instance().restoreOverrideCursor()

	def customMouseClickEvent(self, event):
		pass

	def mouseDoubleClickEvent(self, event):
		pass

	# 通过FFPin来创建pinitem
	def createPinItem(self, pin):
		pinItem = FFPinItem()
		pinItem._PinRef = pin
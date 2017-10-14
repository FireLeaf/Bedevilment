from PyQt5.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsPathItem, QGraphicsRectItem, QTabBar, QGraphicsScene, QGraphicsLineItem
from PyQt5.QtGui import QBrush
from PyQt5.Qt import *
import time

from GraphView.Help.ResUtil import FFResUtil
from GraphView.GraphScene import FFGraphScene

class FFNodeGraphView(QGraphicsView):
	def __init__(self):
		super(FFNodeGraphView, self).__init__()
		self._GraphRef			= None # 对应的graph引用
		self._GraphScene = FFGraphScene()
		self.setScene(self._GraphScene)
		self.setSceneRect(0, 0, 100000, 100000)

		self._SelectRegionItem = None  # 选中框
		self._MidMouseDown = False
		self._LastMouseDownTime = 0

		#self.setBackgroundBrush(QBrush(FFResUtil.GraphPixmap()))
		self.setStyleSheet("background: transparent;border:0px")

		self.scale(1.0, 1.0)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

	def wheelEvent(self, event):
		# QGraphicsView.wheelEvent(self, event)
		if True or event.isAccepted():
			delta = event.angleDelta().y()
			# self.transform().
			if delta > 0:
				self.scale(1.1, 1.1)
			else:
				self.scale(0.9, 0.9)

	def mouseMoveEvent(self, event):

		if self._SelectRegionItem != None:
			self.rebuildRect(event)
		elif not self._MidMouseDown:
			QGraphicsView.mouseMoveEvent(self, event)
		elif True or not event.isAccepted():
			self._oldCenter = self.mapToScene(self.viewport().rect().center())
			newMousePos = event.pos()
			deltaPos = self.mapToScene(newMousePos) - self.mapToScene(self._oldMousePos)
			# self._oldMousePos = newMousePos
			self.centerOn(self._oldSceneCenter - deltaPos)


	def rebuildRect(self, event):
		# rect = QRectF()
		endPos = self._SelectRegionItem.mapFromScene(self.mapToScene(event.pos()))
		self._SelectRegionItem.setRect(0, 0, endPos.x(), endPos.y())

	def mousePressEvent(self, event):
		QGraphicsView.mousePressEvent(self, event)
		self._LastMouseDownTime = time.time()
		if not event.isAccepted():
			if event.button() == Qt.MiddleButton:
				print("view press")
				self._MidMouseDown = True
				# self._oldCenter = self.viewport().rect().center()
				self._oldMousePos = event.pos()
				self._oldSceneCenter = self.mapToScene(self.viewport().rect().center())
			elif event.button() == Qt.RightButton:
				selectItems = self.scene().items(self.mapToScene(event.pos()), Qt.IntersectsItemShape)
				for item in selectItems:
					if isinstance(item, QGraphicsPathItem):
						pen = QPen(QColor(0x00, 0xff, 0x00))
						pen.setWidth(2)
						item.setPen(pen)
			elif event.button() == Qt.LeftButton:
				startPos = self.mapToScene(event.pos())
				self._SelectRegionItem = QGraphicsRectItem()
				self.scene().addItem(self._SelectRegionItem)
				self._SelectRegionItem.setPos(startPos)
				self.rebuildRect(event)

	def mouseReleaseEvent(self, event):
		QGraphicsView.mouseReleaseEvent(self, event)
		if self._MidMouseDown:
			print("view release")
			self._MidMouseDown = False
		if self._SelectRegionItem != None:
			self.scene().SelectNone()
			rect = self._SelectRegionItem.mapToScene(self._SelectRegionItem.rect())
			selectItems = self.scene().items(rect, Qt.IntersectsItemBoundingRect)
			from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
			for item in selectItems:
				if isinstance(item, FFNodeGraphicsItem):
					self._GraphScene.SelectItem(item, True)
					#item.setSelected(True)
			self.scene().removeItem(self._SelectRegionItem)
			self._SelectRegionItem = None
		#elif event.button() == Qt.LeftButton:
		#	self._GraphScene.SelectNone()

		if (time.time() - self._LastMouseDownTime < 0.1):
			self.scene().SelectNone()

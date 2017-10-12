from PyQt5.QtWidgets import QGraphicsItem
from PyQt5.QtCore import QRect, QRectF

from Graph.Help.Util import *


class FFHLayoutItem(QGraphicsItem):
	def __init__(self, gap):
		super(FFHLayoutItem, self).__init__()
		self._Items = []
		self._Gap = gap
		self._LocationLeft = False
		self._BoundRect = QRectF(0, 0, 0, 0)

	def SetItems(self, items, locationLeft):
		self._LocationLeft = locationLeft
		for item in items:
			if item != None:
				self._Items.append(item)
		#self._Items = items
		w, h = 0, 0
		if self._LocationLeft:
			for item in self._Items:
				w += self._Gap
				item.setPos(w, 0)
				rect = item.boundingRect()
				w += rect.width()
				h = max(h, rect.height())
		else:
			for item in self._Items:
				w += self._Gap
				rect = item.boundingRect()
				w += rect.width()
				item.setPos(-w, 0)
				h = max(h, rect.height())
		self._BoundRect = QRectF(0, 0, w, h)

	def boundingRect(self):
		return self._BoundRect
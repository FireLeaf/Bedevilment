from PyQt5.QtWidgets import QGraphicsPathItem

'''
	连接线
'''

class FFLinkItem(QGraphicsPathItem):
	def __init__(self):
		self._LinkRef = None
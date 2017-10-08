from PyQt5.QtGui import QPixmap, QCursor
from PyQt5.QtCore import QSize
from PyQt5.Qt import *

class FFResUtil:
	pinPixmap = None
	@staticmethod
	def PinPixmap():
		if FFResUtil.pinPixmap == None:
			pixmap = QPixmap()
			pixmap.load("Res/pin.png")
			pixSize = QSize(16, 16)
			FFResUtil.pinPixmap = pixmap.scaled(16, 16)
		return FFResUtil.pinPixmap

	flowPixmap = None
	@staticmethod
	def FlowPixmap():
		if FFResUtil.flowPixmap == None:
			pixmap = QPixmap()
			pixmap.load("Res/flow.png")
			FFResUtil.flowPixmap = pixmap.scaled(16, 16)
		return FFResUtil.flowPixmap

	graphPixmap = None
	@staticmethod
	def GraphPixmap():
		if FFResUtil.graphPixmap == None:
			pixmap = QPixmap()
			pixmap.load("Res/graph.jpg")
			FFResUtil.graphPixmap = pixmap#pixmap.scaled(512, 512)
		return FFResUtil.graphPixmap

	@staticmethod
	def CreateCursor(path):
		pixSize = QSize(32, 32)
		pixmap = QPixmap()
		pixmap.load(path)
		scaledPixmap = pixmap.scaled(pixSize, Qt.KeepAspectRatio)
		cursor = QCursor(scaledPixmap, -1, -1)
		return cursor

	okCursor = None
	@staticmethod
	def OkCursor():
		if FFResUtil.okCursor == None:
			FFResUtil.okCursor = FFResUtil.CreateCursor("Res/ok.png")
		return FFResUtil.okCursor

	errorCursor = None
	@staticmethod
	def ErrorCursor():
		if FFResUtil.errorCursor == None:
			FFResUtil.errorCursor = FFResUtil.CreateCursor("Res/error.png")
		return FFResUtil.errorCursor

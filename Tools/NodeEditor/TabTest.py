from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.Qt import *
from NodeGraphicsView import FFNodeGraphicsView

class FFTabBar(QTabBar):
	def __init__(self, parent, *args, **kwargs):
		super(QTabBar, self).__init__(parent, *args, **kwargs)
		self.setContextMenuPolicy(Qt.CustomContextMenu)
		#self.connect(self, SIGNAL("customContextMenuRequested(QPoint)"))
		self.customContextMenuRequested.connect(self.contextMenuRequested)
		self.shortcuts = []

		for i in range(1, 10):
			shortcut = QShortcut("Ctrl+" + str(i), self)
			shortcut.activated.connect(self.selectTabAction)
			self.shortcuts.append(shortcut)

		self.setTabsClosable(True)
		self.tabCloseRequested.connect(self.closeTab)
		self.setSelectionBehaviorOnRemove(QTabBar.SelectPreviousTab)
		self.setMovable(True)

	def closeTab(self):
		pass

	def selectTabAction(self):
		shortCut = self.sender()
		index = self.shortcuts.index(shortCut)
		self.setCurrentIndex(index)

	def contextMenuRequested(self, pos):
		pass

	'''def mousePressEvent(self, event):
		pass

	def mouseMoveEvent(self, event):
		pass'''

class FFTabWidget(QTabWidget):
	def __init__(self, parent, *args, **kwargs):
		super(QTabWidget, self).__init__(parent, *args, **kwargs)
		self.setElideMode(Qt.ElideRight)
		self._tabBar = FFTabBar(self)
		self.setTabBar(self._tabBar)
		self.setDocumentMode(False)
		self.initTabs()
		self._tabBar.tabCloseRequested.connect(self.closeTab)

	def closeTab(self, index):
		view = self.widget(index)
		self.removeTab(index)
		view.deleteLater()

	def initTabs(self):
		for i in range(1, 10):
			nodeView = FFNodeGraphicsView(self)
			self.addTab(nodeView, self.tr("Test"))
			if i == 1:
				self.setCurrentWidget(nodeView)
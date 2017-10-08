from PyQt5.QtWidgets import QGraphicsItem, QGraphicsView, QGraphicsPathItem, QGraphicsRectItem, QTabBar, QGraphicsScene, QGraphicsLineItem
from PyQt5.QtGui import QBrush
from PyQt5.Qt import *

from Graph.Help.Util import *
from GraphView.Help.ResUtil import FFResUtil

class FFNodeGraphView(QGraphicsView):
	def __init__(self):
		super(FFNodeGraphView, self).__init__()
		self._NodeGraphicsItems = {}  # 所有的节点
		self._SelectedNodeItems = {}  # 选中的节点
		self._SelectRegionItem = None  # 选中框
		self._GraphRef			= None # 对应的graph引用
		self._GraphScene = QGraphicsScene()
		self.setScene(self._GraphScene)
		self.setSceneRect(0, 0, 100000, 100000)

		#self.setBackgroundBrush(QBrush(FFResUtil.GraphPixmap()))
		self.setStyleSheet("background: transparent;border:0px")

		self.scale(1.0, 1.0)
		self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
		self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

	def ClearGraph(self):
		self._GraphRef = None
		for _, nodeItem in self._NodeGraphicsItems:
			self.removeItem(nodeItem)
		self._NodeGraphicsItems.clear()
		self._SelectedNodeItems.clear()
		if self._SelectRegionItem != None:
			self.remove(self._SelectRegionItem)

	def RenderGraph(self, graphRef):
		self.ClearGraph()
		self._GraphRef = graphRef
		for _, node in self._GraphRef._Nodes:
			self.addItem(self.createNodeItem(node))

	def AddLink(self, inPin, outPin):
		pass

	def DelLink(self, link):
		inPin = link._InPin
		outPin = link._OutPin
		pass

	def AddFlow(self, inNode, outNode):
		pass

	def DelFlow(self, flow):
		pass

	def DelNode(self, node):
		pass

	def CreateNodeItem(self, node):
		nodeType = node._NodeType
		if nodeType == FFNodeType.NODE_SWITCH:
			from GraphView.GraphicsItem.SwitchNodeItem import FFSwitchNodeItem
			return FFSwitchNodeItem(node)
		elif nodeType == FFNodeType.NODE_ARITHMETIC or \
				nodeType == FFNodeType.NODE_LOGIC or \
				nodeType == FFNodeType.NODE_RELATION:
			from GraphView.GraphicsItem.Base.OperationNodeItem import FFOperationNodeItem
			return  FFOperationNodeItem(node)
		elif nodeType == FFNodeType.NODE_FOR:
			from GraphView.GraphicsItem.ForNodeItem import FFForNodeItem
			return FFForNodeItem(node)
		elif nodeType == FFNodeType.NODE_WHILE:
			from GraphView.GraphicsItem.WhileNodeItem import FFWhileNodeItem
			return FFWhileNodeItem(node)

		return None

	def AddNode(self, node):
		nodeItem = self.CreateNodeItem(node)
		self._GraphScene.addItem(nodeItem)
		nodeItem.setPos(node._Position[1], node._Position[1])
		return nodeItem
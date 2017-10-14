from PyQt5.QtWidgets import QGraphicsScene
from Graph.Help.Util import *

class FFGraphScene(QGraphicsScene):
	def __init__(self):
		super(FFGraphScene, self).__init__()
		self._NodeItems = {}  # 所有的节点
		self._GraphRef = None  # 对应的graph引用
		self._TopZ = 0

	def MoveSelectItemPos(self, deltaPos):
		for node, nodeItem in self._NodeItems.items():
			if nodeItem.isSelected():
				nodeItem.setNodePos(nodeItem.scenePos() + deltaPos)
		self.update()

	def ToggleSelect(self, item):
		self.SelectItem(item, not item.isSelected())

	def ToggleUniqueItem(self, item):
		for node, nodeItem in self._NodeItems.items():
			if item != nodeItem and nodeItem.isSelected():
				self.SelectItem(nodeItem, False)
		if item != None:
			self.ToggleSelect(item)

	def SelectUniqueItem(self, item):
		for node, nodeItem in self._NodeItems.items():
			if item != nodeItem and nodeItem.isSelected():
				#nodeItem.setSelected(False)
				self.SelectItem(nodeItem, False)
		if item != None:
			self.SelectItem(item, True)
			#item.setSelected(True)

	def SelectNone(self):
		self.SelectUniqueItem(None)

	def SelectItem(self, item, isSelected):
		if item != None:
			item.setZValue(isSelected if 1 else 0)
			item.setSelected(isSelected)


	def GetSelectedItems(self):
		items = []
		for node, nodeItem in self._NodeItems.items():
			if nodeItem.isSelected():
				items.append(nodeItem)
		return items

	def ClearGraph(self):
		self._GraphRef = None
		for _, nodeItem in self._NodeItems.items():
			self.removeItem(nodeItem)
		self._NodeItems.clear()
		if self._SelectRegionItem != None:
			self.remove(self._SelectRegionItem)

	def RenderGraph(self, graphRef):
		self.ClearGraph()
		self._GraphRef = graphRef
		for _, node in self._GraphRef._Nodes.items():
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
		del self._NodeItems[self._NodeItems.index(node)]

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
		self.addItem(nodeItem)
		self._NodeItems[node] = nodeItem
		nodeItem.setPos(node._Position[1], node._Position[1])
		return nodeItem

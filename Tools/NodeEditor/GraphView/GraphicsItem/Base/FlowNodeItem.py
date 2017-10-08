from GraphView.GraphicsItem.Base.NodeItem import FFNodeGraphicsItem
from GraphView.GraphicsItem.Parts.FlowGroupItem import FFFlowGroupItem

class FFFlowNodeItem(FFNodeGraphicsItem):
	def __init__(self, nodeRef):
		super(FFFlowNodeItem, self).__init__(nodeRef)
		self._InFlowItem = FFFlowGroupItem(self, self._NodeRef._InFlow)
		self._OutFlowItem = FFFlowGroupItem(self, self._NodeRef._OutFlow)

	'''
		头部包括标题和
	'''
	def repositionHead(self):
		self.repositionFlowItem(self.boundingRect().width(), self.DEFAULT_TITLE_HEIGHT)

	def headWidthAndHeight(self):
		headWidth, headHeight = super(FFFlowNodeItem, self).headWidthAndHeight()
		defFlowWidth = self.DEFAULT_FLOW_WIDTH * 2
		return  max(headWidth, defFlowWidth), headHeight + self.DEFAULT_FLOW_HEIGHT

	def repositionFlowItem(self, nodeWidth, curHeight):
		height = curHeight + 4#+ self._InFlowItem.boundingRect().height() / 2
		itemWidth = self._InFlowItem.boundingRect().width()
		self._InFlowItem.setPos(0, height)
		self._OutFlowItem.setPos(nodeWidth, height)
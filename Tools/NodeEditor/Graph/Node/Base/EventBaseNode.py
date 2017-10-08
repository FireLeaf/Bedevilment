from Graph.Node.Base.Node import FFNode
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *
'''
	事件节点，所有的事件节点，例如状态生命周期事件，游戏事件，定时事件，帧事件
	此类事件节点特点，没有输入的pin和输入执行流，只有一些输出pin和一个输出执行流
'''
class FFEventBaseNode(FFNode):
	def __init__(self):
		super(FFEventBaseNode, self).__init__()
		self._OutFlow = FFFlow()
		self._OutPins = []
		self._EventName = ""

	def GetName(self):
		return self._EventName
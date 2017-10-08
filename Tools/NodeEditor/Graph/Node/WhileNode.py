from Graph.Node.Base.FlowNode import FFFlowNode
from Graph.Help.Pin import FFPin
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *

'''
	调用函数的节点，此节点继承自FFFlowNode，有输入流也有输出流
	而且也可以有多个输入pin以及多个输出pin
'''


class FFWhileNode(FFFlowNode):
	def __init__(self):
		super(FFWhileNode, self).__init__()
		self._NodeType = FFNodeType.NODE_WHILE
		self._CondPin = FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_IN, "Condition", 0)
		self._LoopBodyFlow = FFFlow(self, FFFlag.FLAG_FLOW_OUT, "LoopBody")

	def GetName(self):
		return "WhileLoop"
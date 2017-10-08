from Graph.Node.Base.FlowNode import FFFlowNode
from Graph.Help.Pin import FFPin
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *

'''
	调用函数的节点，此节点继承自FFFlowNode，有输入流也有输出流
	而且也可以有多个输入pin以及多个输出pin
'''
class FFForNode(FFFlowNode):
	def __init__(self):
		super(FFForNode, self).__init__()
		self._NodeType = FFNodeType.NODE_FOR
		self._StartIdxPin = FFPin(self, FFType.TYPE_INT, FFFlag.FLAG_PIN_IN, "StartIndex", 0)
		self._EndIdxPin = FFPin(self, FFType.TYPE_INT, FFFlag.FLAG_PIN_IN, "EndIndex", 0)
		self._StepIdxPin = FFPin(self, FFType.TYPE_INT, FFFlag.FLAG_PIN_IN, "EndIndex", 1)
		self._LoopBodyFlow = FFFlow(self, FFFlag.FLAG_FLOW_OUT, "LoopBody")


	def GetName(self):
		return "ForLoop"
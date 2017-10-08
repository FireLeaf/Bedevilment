from  Graph.Help.Util import *
from Graph.Node.Base.OperationNode import FFOperationNode

from Graph.Help.Pin import FFPin

'''
	算数运算节点，包括+，-，*，/，%
'''
class FFArithmeticNode(FFOperationNode):
	def __init__(self, opSubType, valueType):
		super(FFArithmeticNode, self).__init__(opSubType)
		self._NodeType = FFNodeType.NODE_ARITHMETIC
		self._ValueType = valueType
		self._InPins.append(FFPin(self, valueType, FFFlag.FLAG_PIN_IN, "op1", 0))
		self._InPins.append(FFPin(self, valueType, FFFlag.FLAG_PIN_IN, "op2", 0))
		self._OutPin = FFPin(self, valueType, FFFlag.FLAG_PIN_OUT, "result", 0)

	def incPin(self):
		self._InPins.append(FFPin(self, self._ValueType, FFFlag.FLAG_PIN_IN, "op%d"%(len(self._InPins) + 1), 0))

	def decPin(self):
		if len(self._InPins) > 2:
			pass
			return True
		return False
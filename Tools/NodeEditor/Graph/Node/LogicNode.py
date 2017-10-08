from  Graph.Help.Util import *
from Graph.Node.Base.OperationNode import FFOperationNode

from Graph.Help.Pin import FFPin

'''
	逻辑运算节点，包括and，or，not
'''
class FFLogicNode(FFOperationNode):
	def __init__(self, opSubType):
		super(FFLogicNode, self).__init__(opSubType)
		self._NodeType = FFNodeType.NODE_LOGIC
		self._InPins.append(FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_IN, "op1", 0))
		self._InPins.append(FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_IN, "op2", 0))
		self._OutPin = FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_OUT, "result", 0)

	def incPin(self):
		self._InPins.append(FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_IN, "op%d"%(len(self._InPins) + 1), 0))

	def decPin(self):
		if len(self._InPins) > 2:
			pass
			return True
		return False
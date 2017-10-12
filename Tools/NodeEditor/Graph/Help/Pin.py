from Graph.Help.Util import *


class FFPin:
	def __init__(self, nodeRef, valueType, pinFlag, pinName, customValue):
		self._NodeRef = nodeRef  # 引用的节点
		self._PinValueType = valueType
		self._PinFlag = pinFlag
		self._PinName = pinName  # 这里的名字很关键，在一个node中具有唯一性, 参数名字、返回值名字、或者类成员变量
		self._CustomValue = customValue

	def SetDeafultValue(self, value):
		self._CustomValue = value

	def IsInPin(self):
		return  self._PinFlag == FFFlag.FLAG_PIN_IN

	def IsCompatibility(self, peerPin):
		if peerPin == None:
			return False

		if self._NodeRef == peerPin._NodeRef:
			return False

		if self._PinFlag == peerPin._PinFlag:
			return False

		if not FFType.CheckTypeCompatibility(self._PinValueType, peerPin._PinValueType):
			return False

		return True

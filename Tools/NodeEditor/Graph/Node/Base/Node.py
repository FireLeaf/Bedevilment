from Utility.Log import FFLog
from Graph.Help.Link import FFPinLink, FFFlowLink

# 所有节点的基类
class FFNode:
	def __init__(self):
		self._NodeID    = 0
		self._Position  = (90, 90, 90)
		self._FlowLinks  = []
		self._PinLinks  = []
		#self._Name      = ""

	def SetPos(self, x, y, z):
		self._Position = (x, y, z)

	def GetName(self):
		pass

	def CheckHaveLink(self, pinOne, pinTwo):
		for link in self._PinLinks:
			if (link._PinIn == pinOne and link._PinOut == pinTwo) or (link._PinIn == pinTwo and link._PinOut == pinOne):
				return True
		return False

	def AddPinLink(self, pinOne, pinTwo):
		if pinOne._NodeRef != self and pinTwo._NodeRef != self:
			FFLog.Logger().error("add error pin link")
			return False

		if self.CheckHaveLink(pinOne, pinTwo):
			FFLog.Logger().error("Already have same link")
			return True

		link = FFPinLink.CreateLink(pinOne, pinTwo)
		if link != None:
			self._PinLinks.append(link)
			return True
		else:
			FFLog.Logger().error("create pin link error")
		return False

	def RemovePinRawLink(self, link):
		del self._PinLinks[self._PinLinks.index(link)]

	def RemovePinLink(self, link):
		if (link._PinIn != None and link._PinIn._NodeRef == self) or \
		  link._PinOut != None and link._PinOut._NodeRef == self:
			self.RemovePinRawLink(link)
			return True
		return False

	def AddFlowLink(self, flowOne, flowTwo):
		if flowOne._NodeRef != self and flowTwo._NodeRef != self:
			FFLog.Logger().error("add error flow link")
			return False

		if self.CheckHaveLink(flowOne, flowTwo):
			FFLog.Logger().error("Already have same link")
			return True

		link = FFFlowLink.CreateLink(flowOne, flowTwo)
		if link != None:
			self._PinLinks.append(link)
			return True
		else:
			FFLog.Logger().error("create flow link error")
		return False

	def RemoveFlowRawLink(self, link):
		del self._FlowLinks[self._FlowLinks.index(link)]

	def RemoveFlowLink(self, link):
		if (link._PinIn != None and link._PinIn._NodeRef == self) or \
		  link._PinOut != None and link._PinOut._NodeRef == self:
			self.RemoveFlowRawLink(link)
			return True
		return False


	def generateNodeID(self):
		return  1

	def Compile(self):
		pass

	def Link(self):
		pass
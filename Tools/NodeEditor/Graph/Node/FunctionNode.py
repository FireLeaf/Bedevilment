from Graph.Node.Base.Node import FFNode
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *

'''
	包括函数的开始以及函数的结束节点
'''

'''
	函数开始节点
'''
class FFFuncBeginNode(FFNode):
	def __init__(self):
		super(FFFuncBeginNode, self).__init__()
		self._OutFlow = FFFlow()
		self._OutPins = []

'''
	函数结束节点
'''
class FFFuncEndNode(FFNode):
	def __init__(self):
		super(FFFuncEndNode, self).__init__()
		self._InFlow = FFFlow()
		self._InPins = []

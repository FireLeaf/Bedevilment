
from Graph.Node.Base.Node import FFNode
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *

'''
	同时带有入口流和出口流的节点
'''
class FFFlowNode(FFNode):
    def __init__(self):
        super(FFFlowNode, self).__init__()
        self._InFlow = FFFlow(self, FFFlag.FLAG_FLOW_IN, "") # 节点入口
        self._OutFlow = FFFlow(self, FFFlag.FLAG_FLOW_OUT, "") # 节点出口

    def AddFlowLink(self, selfFlow, peerFlow):
        if self._OutFlow == selfFlow:
            pass
from Graph.Help.Util import *

class FFFlow:
    def __init__(self, nodeRef, flowFlag, flowName):
        self._NodeRef   = nodeRef
        self._FlowFlag  = flowFlag
        self._FlowName  = flowName

    def IsInFlow(self):
        return self._FlowFlag == FFFlag.FLAG_FLOW_IN

    def IsCompatibility(self, peerFlow):
        if peerFlow == None:
            return False
        if self._FlowFlag == peerFlow._FlowFlag:
            return False
        if self._NodeRef == peerFlow._NodeRef:
            return False
        return True
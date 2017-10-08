class FFFlow:
    def __init__(self, nodeRef, flowFlag, flowName):
        self._NodeRef   = nodeRef
        self._FlowFlag  = flowFlag
        self._FlowName  = flowName

    def IsCompatibility(self, peerFlow):
        if peerFlow == None:
            return False
        if self._FlowFlag == peerFlow._FlowFlag:
            return False
        if self._NodeRef == peerFlow._NodeRef:
            return False
        return True
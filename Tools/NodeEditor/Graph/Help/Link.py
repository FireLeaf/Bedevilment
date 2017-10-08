from Graph.Help.Util import *

class FFFlowLink:
    def __init__(self):
        self._FlowIn = None
        self._FlowOut = None

    @staticmethod
    def CreateLink(flowOne, flowTwo):
        link = None
        if flowOne._FlowFlag == flowTwo._FlowFlag:
            return link
        link = FFFlowLink()
        if flowOne._PinFlag == FFFlag.FLAG_FLOW_IN and flowTwo._PinFlag == FFFlag.FLAG_FLOW_OUT:
            link._FlowIn = flowOne
            link._FlowOut = flowTwo
        elif flowOne._PinFlag == FFFlag.FLAG_FLOW_OUT and flowTwo._PinFlag == FFFlag.FLAG_FLOW_IN:
            link._FlowIn = flowTwo
            link._FlowOut = flowOne
        else:
            return None

class FFPinLink:
    def __init__(self):
        self._PinIn = None # 输入方
        self._PinOut = None # 输出方

    @staticmethod
    def CreateLink(pinOne, pinTwo):
        link = None
        if pinOne._PinFlag == pinTwo._PinFlag:
            return link
        if not FFType.CheckTypeCompatibility(pinOne._PinType, pinTwo._PinType):
            return link

        link = FFPinLink()
        if pinOne._PinFlag == FFFlag.FLAG_PIN_IN and pinTwo._PinFlag == FFFlag.FLAG_PIN_OUT:
            link._PinIn = pinOne
            link._PinOut = pinTwo
        elif pinOne._PinFlag == FFFlag.FLAG_PIN_OUT and pinTwo._PinFlag == FFFlag.FLAG_PIN_IN:
            link._PinIn = pinTwo
            link._PinOut = pinOne
        else:
            return None

        return link

    def CheckLinkValid(self):
        if self._PinIn != None and self._PinOut != None:
            if self._PinIn._PinFlag != FFFlag.FLAG_PIN_IN or self._PinOut._PinFlag != FFFlag.FLAG_PIN_OUT:
                return False
            elif not FFType.CheckTypeCompatibility(self._PinIn._PinType, self._PinOut._PinType):
                return  False
        return True
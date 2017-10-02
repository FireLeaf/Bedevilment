
class FFNodeGraphicView:
    pass

class FFStateGraphView:
    def __init__(self):
        self._StateGraph        = None # hold一个状态图
        self._NodeGraphicsItems = {} # 所有的节点
        self._SelectedNodeItems = {} # 选中的节点
        self._SelectRegionItem  = None # 选中框

    def AddLink(self, inPin, outPin):
        pass

    def DelLink(self, link):
        inPin = link._InPin
        outPin = link._OutPin
        pass

    def AddFlow(self, inNode, outNode):
        pass

    def DelFlow(self, flow):
        pass

    def DelNode(self, node):
        pass

    def AddNode(self, node):
        pass


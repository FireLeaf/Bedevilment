

class FFGraph:
    def __init__(self):
        self._Nodes         = {} # 所有在状态里的节点，除成员函数图,是map，节点ID到节点的映射
        self._UniqueID      = 0  # 用来产生唯一ID

    def AddNode(self, node):
        while (self._Nodes.has_key(self._UniqueID)):
            self._UniqueID += 1

        node._NodeID = self._UniqueID
        self._Nodes[node._NodeID] = node
        return  node

    def RemoveNode(self, node):
        if (self._Nodes.has_key(node._NodeID)):
            self._Nodes[node._NodeID] = None
        else:
            pass


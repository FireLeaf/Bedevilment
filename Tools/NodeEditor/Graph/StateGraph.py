
import json

class FFStateGraph:
    def __init__(self):
        self._Nodes         = {} # 所有在状态里的节点，除成员函数图,是map，节点ID到节点的映射
        self._MethodsGraph  = {} # 所有成员函数的图(Function Graph)
        self._Fields        = [] # 属性字段列表
        self._UniqueID      = 0 #

    def Load(self):
        pass

    def LoadStateLayout(self):
        pass

    def LoadStateGraphNodes(self):
        pass

    def LoadStateMethod(self):
        pass


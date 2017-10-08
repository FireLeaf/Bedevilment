
import json


class FFStateGraph(FFGraph):
    def __init__(self):
        self._MethodsGraph  = {} # 所有成员函数的图(Function Graph)
        self._Fields        = [] # 属性字段列表

    def Load(self):
        pass

    def LoadStateLayout(self):
        pass

    def LoadStateGraphNodes(self):
        pass

    def LoadStateMethod(self):
        pass



class FFFunctionGraph:
    def __init__(self):
        self._Nodes = {} # 所有的节点
        self._FuncInNode = None # 函数入口节点
        self._FuncOutNode = None # 函数返回节点
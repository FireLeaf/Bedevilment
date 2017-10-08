
from Graph.Help.Pin import FFPin
from Graph.Node.Base.Node import FFNode


# 二元运算类节点
class FFBinaryOperationNode(FFNode):
    def __init__(self):
        super(FFBinaryOperationNode, self).__init__()
        self._LeftOperandPin = None
        self._RightOperandPin = None
        self.ResultPin = None
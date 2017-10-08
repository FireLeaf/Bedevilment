
from Graph.Help.Pin import FFPin
from Graph.Node.Base.Node import FFNode
from Graph.Help.Util import *

# 二元运算类节点
class FFOperationNode(FFNode):
    def __init__(self, opSubType):
        super(FFOperationNode, self).__init__()
        self._InPins = []
        self._OutPin = None
        self._OpSubType = opSubType

    OperationNodeName = {
        FFNodeSubType.NST_ARITHMETIC_ADD: "ADD",
        FFNodeSubType.NST_ARITHMETIC_SUB: "SUB",
        FFNodeSubType.NST_ARITHMETIC_MUL: "MUL",
        FFNodeSubType.NST_ARITHMETIC_DIV: "DIV",
        FFNodeSubType.NST_ARITHMETIC_MOD: "MOD",

        FFNodeSubType.NST_LOGIC_AND: "AND",
        FFNodeSubType.NST_LOGIC_OR: "OR",
        FFNodeSubType.NST_LOGIC_NOT: "NOT",

        FFNodeSubType.NST_RELATION_GT: ">",
        FFNodeSubType.NST_RELATION_GE: ">=",
        FFNodeSubType.NST_RELATION_LT: "<",
        FFNodeSubType.NST_RELATION_LE: "<=",
        FFNodeSubType.NST_RELATION_EQ: "==",
        FFNodeSubType.NST_RELATION_NEQ: "!=",
    }
    def GetName(self):
        return self.OperationNodeName[self._OpSubType]
from Graph.Node.Base.FlowNode import FFFlowNode
from Graph.Help.Pin import FFPin
from Graph.Help.Flow import FFFlow
from Graph.Help.Util import *

'''
    开关节点，类似与 if a then else b end
    
'''
class FFSwitchNode(FFFlowNode):
    def __init__(self):
        super(FFSwitchNode, self).__init__()
        self._NodeType = FFNodeType.NODE_SWITCH
        self._NodeName = "Switch"
        self._CondPin = FFPin(self, FFType.TYPE_BOOLEAN, FFFlag.FLAG_PIN_IN, "Condition", False)
        self._TrueFlow = FFFlow(self, FFFlag.FLAG_FLOW_OUT, "True")
        self._FalseFlow = FFFlow(self, FFFlag.FLAG_FLOW_OUT, "False")

    def GetName(self):
        return "Switch"


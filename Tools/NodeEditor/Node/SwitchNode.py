
"""
选择节点
"""
from Node.Node import FFNodeBase
from Node.Pin import FFPin

class FFSwitchNode(FFNodeBase):
    def __init__(self):
        super.__init__(self)
        self.NodeName = "Switch"
        self.CondPin = FFPin()
        self.TruePin = FFPin()
        self.FalsePin = FFPin()


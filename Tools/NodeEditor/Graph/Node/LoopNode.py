from Graph.Node.Base.FlowNode import FFFlowNode

'''
	调用函数的节点，此节点继承自FFFlowNode，有输入流也有输出流
	而且也可以有多个输入pin以及多个输出pin
'''
class FFCallNode(FFFlowNode):
    def __init__(self):
        super(FFFlowNode, self).__init__()
        self._InPins = []
        self._OutPins = []
        self._FuncName = ""

    def GetName(self):
        return self._FuncName
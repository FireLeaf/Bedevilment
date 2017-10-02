
class FFNode:
    # 表达式类
    NODE_ARITHMETIC = 1 # 算术节点
    NODE_LOGIC      = 2 # 逻辑节点
    NODE_RELATION   = 3 # 关系运算符节点
    NODE_SELECT     = 4 # 三元表达式

    # 流程类
    NODE_CALL       = 1001 # 调用函数节点
    NODE_SWITCH     = 1002 # 开关节点
    NODE_FOR        = 1003 # for节点
    NODE_WHILE      = 1004 # while节点
    NODE_LOOP       = 1005 # loop节点

    #
    NODE_EVENT      = 2001 # 事件相关节点（内部包括有状态生命周期事件、游戏事件、帧事件）
    NODE_FUNCTION   = 2002 # 函数相关节点

# 所有节点的基类
class FFNodeBase:
    def __init__(self):
        self.NodeID = self.generateNodeID()

    def generateNodeID(self):
        return  1

    def Compile(self):
        pass

    def Link(self):
        pass

# 控制类节点
class FFFlowNode(FFNodeBase):
    def __init__(self):
        super(FFFlowNode, self).__init__()
        self._InFlow = FFFlow() # 进入当前节点
        self._OutFlow = FFFlow() # 下一个节点

# 二元运算类节点
class FFBinaryOperationNode(FFNodeBase):
    def __init__(self):
        super(FFBinaryOperationNode, self).__init__()
        self._LeftOperandPin = FFPin()
        self._RightOperandPin = FFPin()

class FFEventNode(FFNodeBase):
    def __init__(self):
        super(FFEventNode, self).__init__()
        self._OutFlow = FFFlow()
        self._OutPins = []

class FFCallNode(FFFlowNode):
    def __init__(self):
        super(FFFlowNode, self).__init__()
        self._InPins = []
        self._OutPins = []
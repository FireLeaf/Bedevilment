from Graph.Node.Base.EventBaseNode import FFEventBaseNode

'''
	状态生命周期的节点，主要有OnActive， OnSimulate，OnDeactive之类的
'''
class FFLifeCycleEventNode(FFEventBaseNode):
	def __init__(self):
		super(FFLifeCycleEventNode, self).__init__()

'''
	游戏事件节点
'''
class FFGameEventNode(FFEventBaseNode):
	def __init__(self):
		super(FFGameEventNode, self).__init__()


'''
	定时器节点
'''
class FFTimerEventNode(FFEventBaseNode):
	def __init__(self):
		super(FFTimerEventNode, self).__init__()

'''
	帧事件节点
'''
class FFFrameEventNode(FFEventBaseNode):
	def __init__(self):
		super(FFFrameEventNode, self).__init__()
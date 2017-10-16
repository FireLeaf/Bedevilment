
from Workspace.Meta.ClassMeta import FFClass

class FFNodeClass(FFClass):
    def __init__(self):
        pass

    def AddMethod(self, methodName, params, returnVals, methodFlag):
        pass

    def AddField(self, fieldName, fieldType):
        pass

class FFNodeClassAdmin:
    def __init__(self):
        self._NodeClass = {}

    def AddNodeClass(self, className):
        pass

    def RemoveNodeClass(self, className):
        pass

    def FindNodeClass(self, className):
        pass

    def GetNodeStateClass(self):
        pass

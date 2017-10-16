
class FFField:
    def __init__(self):
        self._FieldName = ""
        self._FieldFlag = 0
        self._FieldType = ""

class FFMethod:
    def __init__(self):
        self._MethodName = ""
        self._ReturnValues = [] # 返回值列表
        self._Parameters = [] # 参数列表
        self._MethodFlag = 0 # 方法类型

class FFClass:
    def __init__(self):
        self._Fields = {}
        self._Methods = {}
        self._ClassConfig = {}

    def LoadClass(self):
        import json
        f = open("Settings.json", encoding='utf-8')# 设置以utf - 8解码模式读取文件，encoding参数必须设置，否则默认以gbk模式读取文件，当文件中包含中文时，会报错
        setting = json.load(f)
        family = setting['BaseSettings']['size'] # 注意多重结构的读取语法
        size = setting['fontSize']
        return family
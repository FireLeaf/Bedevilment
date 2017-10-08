class FFError:
    pass

class FFNodeType:
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

class FFNodeSubType:
    # 运算类
    NST_ARITHMETIC_ADD  = 1 # +
    NST_ARITHMETIC_SUB  = 2 # -
    NST_ARITHMETIC_MUL  = 3 # *
    NST_ARITHMETIC_DIV  = 4 # /
    NST_ARITHMETIC_MOD  = 4  # %

    # 逻辑类
    NST_LOGIC_AND       = 101 # and
    NST_LOGIC_OR        = 102 # or
    NST_LOGIC_NOT       = 103 # not

    # 关系类
    NST_RELATION_GT     = 201 # >
    NST_RELATION_GE     = 202 # >=
    NST_RELATION_LT     = 203 # <
    NST_RELATION_LE     = 204 # <=
    NST_RELATION_EQ     = 205 # ==
    NST_RELATION_NEQ    = 206 # !=

class FFType:
    TYPE_NONE       = 0, # 无类型
    TYPE_BOOLEAN    = 1, # 布尔值
    TYPE_INT        = 2, # int 类型
    TYPE_REAL       = 3, # 实数类型，在帧同步这块指的是fixfloat，状态同步中用double或者float（暂时没开发状态同步代码）
    TYPE_NUMBER     = 4, # 数值类型,TYPE_INT或者TYPE_REAL都行
    TYPE_STRING     = 5, # 字符串类型
    TYPE_FUNCTION   = 6, # 函数类型
    TYPE_COBJECT    = 7, # C层类类型
    TYPE_LOBJECT    = 8, # Lua层类类型

    @staticmethod
    def CheckTypeCompatibility(leftType, rightType):
        return leftType == rightType

class FFFlag:
    FLAG_PIN_IN     = 1 << 0, # 该pin是作为输入pin，例如调用函数的参数之类
    FLAG_PIN_OUT    = 1 << 1,
    FLAG_FLOW_IN	= 1 << 2, #
    FLAG_FLOW_OUT	= 1 << 3,
class MetaFlag:
    MF_CLASS_CX         = 1 << 0 # c++/C#类
    MF_CLASS_LUA        = 1 << 1 # lua类
    MF_CLASS_LOCAL      = 1 << 2 # 客户端类
    MF_CLASS_AUTHORITY  = 1 << 3 # 权威服务器类
    MF_CLASS_HOST       = 1 << 4 # 客户端和服务器都有的类
    MF_CLASS_NODE_STATE = 1 << 5 # 节点状态类

    MF_METHOD_STATIC    = 1 << 10 # 静态方法
    MF_METHOD_LOCAL     = 1 << 11 # 客户端方法
    MF_METHOD_AUTHORITY = 1 << 12 # 权威服务器方法
    MF_METHOD_HOST      = 1 << 13 # 客户端和服务器都有的字段
    MF_METHOD_EVENT     = 1 << 14 # 事件处理方法

    MF_FIELD_STATIC     = 1 << 20 # 静态字段
    MF_FIELD_LOCAL      = 1 << 21 # 客户端字段
    MF_FIELD_AUTHORITY  = 1 << 22 # 权威服务器字段
    MF_FIELD_HOST       = 1 << 23 # 客户端和服务器都有的字段
import gc
import sys

gc.set_debug(gc.DEBUG_STATS | gc.DEBUG_LEAK)


class A:
    def __del__(self):
        self.b.c = 10
        print("aaa")


class B:
    def __del__(self):
        self.a.c = 9
        print("bbb")


def C():
    class D:
        def __del__(self):
            print("hello")

    a = D()


C()

a = A()
b = B()
print(hex(id(a)))
print(hex(id(a.__dict__)))
a.b = b
b.a = a
del a
del b

print(gc.collect())
print(gc.garbage)
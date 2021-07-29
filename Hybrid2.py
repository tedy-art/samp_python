class A:
    def fun1(self):
        print("Hey there, you are in class A")

class B(A):
    def fun2(self):
        print("Hey there, you are in class B")

class C(A):
    def fun3(self):
        print("Hey there, you are in class C")

class D(C,A):
    def fun4(self):
        print("Hey there, you are in class D")

ob=D()
ob.fun1()
ob.fun3()
ob.fun4()

#here,A,B,C classes are Hierachical inheritance and A,C,D classes are Multi-level inheritance
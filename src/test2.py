class A:
    def a(self):
        print("A")

class B(A):
    def a(self):
        super().a()
        print("B")

class B1(A):
    def a(self):
        super().a()
        print("B1")

class C(B1, B):
    def a(self):
        super().a()
        print("C")

C().a()
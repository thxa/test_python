class A:
	def func(self):
		print("A.func()")


class B:
	def func(self):
		print("B.func()")


class C(A, B):pass


print(C.__mro__)

c = C()
c.func()

class C(B, A):pass


print(C.mro())

c = C()
c.func()

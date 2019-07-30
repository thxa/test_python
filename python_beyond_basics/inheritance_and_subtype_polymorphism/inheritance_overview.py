class Base(object):
	def __init__(self):
		print("Base initializer")

	def f(self):
		print('Base.f()')


class Sub(Base):
	pass


Sub()


class Sub(Base):
	def __init__(self):
		print("Sub initializer")


print()
Sub()

class Sub(Base):
	def __init__(self):
		print("Sub initializer")

	def f(self):
		print('Sub.f()')


print()
Sub().f()


class Sub(Base):
	def __init__(self):
		super().__init__()
		print("Sub initializer")
	
	def f(self):
		print('Sub.f()')


print()
Sub().f()
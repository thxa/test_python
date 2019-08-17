# https://docs.python.org/3/reference/datamodel.html#metaclasses

class Widget(object, metaclass=type): # default 
	pass
# class Widget: # default 
# 	pass


def main():
	print("\n\nclass Widget(object, metaclass=type): # default\n\tpass\n\n")
	
	w = Widget() ; print("w = Widget()")
	print("w -> ", w)
	print("type(w) -> ", type(w))
	print("type(Widget) -> ", type(Widget))
	print()

	print("w.__class__ -> ", w.__class__)
	print("w.__class__.__class__ -> ", w.__class__.__class__)
	print("w.__class__.__class__.__class__ -> ", w.__class__.__class__.__class__)
	print()

	a = list("A list") ; print("a = list(\"A list\")")
	print("a -> ", a) 
	print("type(a) ->", type(a))
	print("type(type) ->", type(type))

if __name__ == '__main__':
	main()
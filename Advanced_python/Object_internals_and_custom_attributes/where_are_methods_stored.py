from vector_2 import Vector

def main():
	v = Vector(p=5, q=2)
	print(v)
	print(v.__dict__)
	print(v.__class__)
	print(v.__class__.__dict__) # here stored methods
	print(v.__class__.__dict__["__repr__"])
	
	print(v.__class__.__class__)
	# v.__class__.__dict__["a_vector_class_attribute"] = 5 # Can't set this
	setattr(v.__class__, "a_vector_class_attribute", 2)


if __name__ == '__main__':
		main()	
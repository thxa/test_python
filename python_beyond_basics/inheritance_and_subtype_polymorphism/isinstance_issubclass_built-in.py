class A(object):pass
class B(A):pass

a = A()
b = B()

# isinstance Function
print("class A inheritance from object = {0}".format(isinstance(A, object)))
print("class B inheritance from object = {0}".format(isinstance(B, object)))
print()
print("object a inheritance from class A  = {0}".format(isinstance(a, A )))
print("object b inheritance from class B  = {0}".format(isinstance(b, B )))
print("object a inheritance from class B  = {0}".format(isinstance(a, B )))
print("object b inheritance from class A  = {0}".format(isinstance(b, A )))


print()

# issubclass Function
print("class A issubclass from class B  = {0}".format(issubclass(A, B)))
print("class B issubclass from class A  = {0}".format(issubclass(B, A)))


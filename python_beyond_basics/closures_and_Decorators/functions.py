#!/usr/bin/env python
# store = []
# def sort_by_last_letter(strings):
# 	# Local Function
# 	def last_letter(s):
# 		return s.split()[-1]

# 	store.append(last_letter)
# 	print(last_letterk)
# 	return sorted(strings, key=last_letter)

# s = ["Thamer harbi", "Khaled Anse"]
# print(sort_by_last_letter(s))
# def globalfunc(x):
# 	def localfunc(y):
# 		return x + y
# 	return localfunc
# s = globalfunc("hi__")
# print(s.__closure__)
# print(s("1"))

message = "global"

def enclosing():
	message = 'enclosing'

	def local():
		# global message
		nonlocal message
		message = 'local'

	print("enclosing message:", message)
	local()
	print("enclosing message:", message)

print("global message: ", message)
enclosing()
print("global message: ", message)

import time

def make_timer():
	last_called = None

	def elapsed():
		nonlocal last_called
		now = time.time()
		
		if last_called is None:
			last_called = now
			return	None
		
		result = now - last_called
		last_called = now
		
		return result

	return elapsed

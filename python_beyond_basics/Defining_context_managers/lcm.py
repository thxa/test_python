

# https://www.python.org/dev/peps/pep-0343/
class LoggingContextManager:
	def __enter__(self):
		print("LoggingContextManager.__enter__()")
		return "You are in a with-block!"

	def __exit__(self, exc_type, exc_val, exc_tb):
		if exc_type is None:
			print("LoggingContextManager.__exit__:\n" 
				  "normal exit detected.")
		else:
			print("LoggingContextManager.__exit__:\n"
				  "Exception detected!\n"
				  "type={}, value={},  traceback={}".format(exc_type, exc_val, exc_tb))
		# return


def main():
	try:
		with LoggingContextManager() as x:
			raise ValueError("Something has gone wrong!")
			print(x)
	except ValueError:
		print("*** ValueError detected ***")

if __name__ == '__main__':
	main()

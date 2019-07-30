import contextlib
import sys

@contextlib.contextmanager
def logging_context_manager():
	# ENTRY
	print("logging_context_manager: enter")
	try:
		yield "You are in a with-block"
		print("logging_context_manager: normal exit")
	except Exception:
		print("logging_context_manager: exceptional exit", sys.exc_info())
		raise

def main():
	with logging_context_manager() as x:
		print(x)
		raise ValueError("Something went wrong!")

if __name__ == '__main__':
		main()	
import contextlib

class Transaction:
	def __init__(self, conn):
		self.conn = conn
		self.idx = conn._start_transaction()

	def commit(self):
		self.conn._commit_transaction(self.idx)
	
	def rollback(self):
		self.conn._rollback_transaction(self.idx)


@contextlib.contextmanager
def start_transaction(connection):
	tx = Transaction(connection)

	try:
		yield tx
	except:
		tx.rollback()
		raise

	tx.commit()
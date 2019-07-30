from db import Connection, Transaction, start_transaction


def main():
	con = Connection()
	# tx = Transaction(con)
	# tx.rollback()
	# tx.commit()
	
	# with exception
	try:
		with start_transaction(con) as tx:
			x = 1 + 1
			raise ValueError()
			y = x + 2
			print("transaction 0 =", x, y)	
	except ValueError:
		print("Oops! Transaction 0 failed.")
	

	try:
		with start_transaction(con) as tx:
			x = 1 + 1
			y = x + 2
			print("transaction 1 =", x, y)	
	except ValueError:
		assert False

if __name__ == '__main__':
	main()
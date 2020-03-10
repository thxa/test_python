from strategy.strategy_abc import  ABCStrategy

class FedExStrategy(ABCStrategy):
	
	def calculate(self, order):
		return 3.00
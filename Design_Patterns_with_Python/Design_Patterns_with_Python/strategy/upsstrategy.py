from strategy.strategy_abc import  ABCStrategy


class UPSStrategy(ABCStrategy):

	def calculate(self, order):
		return 4.00

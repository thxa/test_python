from strategy.strategy_abc import ABCStrategy


class PostalStrategy(ABCStrategy):

	def calculate(self, order):
		return 5.00

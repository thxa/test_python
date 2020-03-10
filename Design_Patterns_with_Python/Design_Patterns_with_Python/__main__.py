#!/usr/bin/env python3
# https://app.pluralsight.com/course-player?clipId=12351921-3f43-4a18-ad84-89bded787396
from before_strategy import Order, Shipper, ShippingCost

# Test Federal Express shipping
order = Order(Shipper.fedex)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 3.0


# Test UPS shipping
order = Order(Shipper.ups)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 4.0


# Test Postal Service shipping
order = Order(Shipper.postal)
cost_calulator = ShippingCost()
cost = cost_calulator.shipping_cost(order)
assert cost == 5.0

print("Before Tests passed")


# https://app.pluralsight.com/course-player?clipId=4b54680b-f685-4804-9434-fb1d72b5aea7
# Strategy
from strategy import Order, ShippingCost, FedExStrategy, UPSStrategy, PostalStrategy


# Test Federal Express shipping
order = Order()
strategy = FedExStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 3.0


# Test UPS shipping
order = Order()
strategy = UPSStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 4.0


# Test Postal Service shipping
order = Order()
strategy = PostalStrategy()
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 5.0

print("Strategy Tests passed")


# https://app.pluralsight.com/course-player?clipId=24ec6a4e-8876-4aea-a9a4-91491730686c
# Strategy Variations:
	# Strategies as functions
	# Strategies as lambdas
from StrategyVariation import Order, ShippingCost
	
def fedex_strategy(order):
	return 3.0

ups_strategy = lambda order: 4.0

order = Order()

# Test Federal Express shipping
strategy = fedex_strategy
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 3.0


# Test UPS shipping
strategy = ups_strategy
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 4.0


# Test Postal Service shipping
strategy = lambda order: 5.0
cost_calulator = ShippingCost(strategy)
cost = cost_calulator.shipping_cost(order)
assert cost == 5.0

print("Strategy Variation Tests passed")


# switch Statements with if Statements
def play1():

	position = (0, 0)
	alive = True

	while position:

		if position == (0, 0):
			print("You are in maze of twisty passages, all alike.")

		elif position == (1, 0):
			print("You on a road in a dark forest. To the north you can see a tower.")
		
		elif position == (1, 1):
			print("You is a tall tower here, with on obvious door. A path leads east.")

		else:
			print("There is nothing here.")


		command = input()

		x, y = position
		if command == "N":
			position = (x, y + 1)

		elif command == "E":
			position = (x + 1, y)

		elif command == "S":
			position = (x, y - 1)

		elif command == "W":
			position = (x - 1, y)

		elif command == "L":
			pass

		elif command == "Q":
			position = None

		else:
			print("I don't understand")




def go_north(position):
	x, y = position
	new_position = (1, y + 1)
	return new_position

def go_east(position):
	x, y = position
	new_position = (x + 1, y)
	return new_position

def go_south(position):
	x, y = position
	new_position = (x, y - 1)
	return new_position

def go_west(position):
	x, y = position
	new_position = (x - 1, y)
	return new_position

def look(position):
	return position

def quit(position):
	return None



def labyrinth(position, alive):
	print("You are in maze of twisty passages, all alike.")
	return position, alive

def dark_forest_road(position, alive):
	print("You on a road in a dark forest. To the north you can see a tower.")
	return position, alive

def tall_tower(position, alive):
	print("You is a tall tower here, with on obvious door. A path leads east.")
	return position, alive

def rabbit_hole(position, alive):
	print("You fall down a rabbit hole into labyrinth")
	return (0, 0), alive

def lava_pit(position, alive):
	print("You fall into a lava pit.")
	return position, False
# with lambda
# locations = {
# 	(0, 0): lambda: print("You on a road in a dark forest. To the north you can see a tower."),	
# 	(1, 0): lambda: print("You is a tall tower here, with on obvious door. A path leads east."),
# 	(1, 1): lambda: print("There is a tall tower here, with no obvious door. A path leads east."),
# 	}

# switch Statements without if Statements
def play():

	position = (0, 0)
	alive = True

	while position:

		locations = {
			(0, 0): labyrinth,
			(1, 0): dark_forest_road,
			(1, 1): tall_tower,
			(2, 1): rabbit_hole,
			(1, 2): lava_pit
		}

		try:
			location_action =  locations[position]
		except KeyError:
			print("There is nothing here.")
		else:
			position, alive =  location_action(position, alive)

		command = input()

		actions = {
			'N': go_north,
			'E': go_east,
			'S': go_south,
			'W': go_west,
			'L': look,
			'Q': quit,
		}

		try:
			command_action = actions[command]
		except KeyError:
			print("I don't understand")

		else:
			position = command_action(position)

		if not alive:
			print("You're dead!")
			break
	else: # No Break
		print("You have chosen to leave the game")

	print("Game Over")


def main():
	# play1()
	play()

if __name__ == '__main__':
	main()
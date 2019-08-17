# https://docs.python.org/3/library/struct.html
# https://docs.python.org/3/library/binascii.html
# https://docs.python.org/3/library/code.html
import struct
from binascii  import hexlify
from pprint import pprint as pp

class Vector:
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def __repr__(self):
		return "Vector({!r}, {!r}, {!r})".format(self.x, self.y, self.z)


class Color:
	def __init__(self, red, green, blue):
		self.red = red
		self.green = green
		self.blue = blue

	def __repr__(self):
		return "Color({!r}, {!r}, {!r})".format(self.red, self.green, self.blue)


class Vertex:
	def __init__(self, vector, color):
		self.vector = vector
		self.color = color

	def __repr__(self):
		return "Vertex({!r}, {!r})".format(self.vector, self.color)

def make_colored_vertex(x, y, z, red, green, blue):
	return Vertex(Vector(x, y, z),
				  Color(red, green, blue))


def main():
	with open("colors.bin", "rb") as f:
		buffer = f.read()
	print("buffer: {} bytes".format(len(buffer)))

	indexes = ' '.join(str(n).zfill(2) for n in range(len(buffer)))
	print(indexes)

	# print(buffer)
	# print(hexlify(buffer))
	# print(hex_buffer)
	hex_buffer = hexlify(buffer).decode("ascii")
	hex_pairs = ' '.join(hex_buffer[i:i+2] for i in range(0, len(hex_buffer), 2))
	print(hex_pairs)

	# struct.error: iterative unpacking requires a buffer of a multiple of 18 bytes
	# indexes ->   00 01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79
	# hex_pairs -> d1 b2 4f 45 d9 11 cd 45 ed 1c 12 46 e0 0b 77 86 31 d4 5d f9 db 3f ee 45 b2 e3 1e 45 7c 7c 19 46 e0 7f de 14 11 09 00 00 e5 4e d2 45 64 b3 12 45 27 d5 55 45 cf b0 c3 8d 5d 8f 00 00 f8 80 c6 45 c7 81 56 45 ee 8c 18 46 9e db 04 8f ce 2b 00 00
	#																      x  x 														  x  x														 x   x 														  x  x

	# print("\xd1")
	# items = struct.unpack_from("@3f3H", buffer) # @fffHHH == @3f3H
	# # x, y, z, red, green, blue = fields
	# print(repr(items))

	vertices = []
	for fields in struct.iter_unpack("@3f3Hxx", buffer):
		vertex = make_colored_vertex(*fields)
		vertices.append(vertex)

	pp(vertices)


if __name__ == '__main__':
	main()
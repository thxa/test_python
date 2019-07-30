"""A module for dealing with BMP bitmap image files."""

def write_grayscale(filename, pixels):
	"""Create and writes a grayscale BMP file.

	Args:
		filename: The name of BMP file  

		pixels: A rectangular image stored as a sequence of rows.

	
	"""

	height = len(pixels)
	width = len(pixels[0])

	with open(file=filename, mode='wb') as bmp:
		# BMP Header
		bmp.write(b'BM')

		size_bookmark = bmp.tell()
		bmp.write(b'\x00\x00\x00\x00')

		bmp.write(b'\x00\x00')
		bmp.write(b'\x00\x00')

		pixel_offset_bookmark = bmp.tell()
		bmp.write(b'\x00\x00\x00\x00')

		# Image Header
		bmp.write(b'\x28\x00\x00\x00')
		bmp.write(_int32_to_bytes(width))
		bmp.write(_int32_to_bytes(height))
		bmp.write(b'\x01\x00')
		bmp.write(b'\x08\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')
		bmp.write(b'\x00\x00\x00\x00')

		# Color palette - a linear grayscale
		for c in range(256):
			bmp.write(bytes((c, c, c, 0)))

		# Pixel data
		pixel_data_bookmark = bmp.tell()
		for row in reversed(pixels):
			row_data = bytes(row)
			bmp.write(row_data)
			padding = b'\x00' * (4 - (len(row) % 4))
			bmp.write(padding)

		# End of file
		eof_bookmark = bmp.tell()

		# Fill in file size placeholder
		bmp.seek(size_bookmark)
		bmp.write(_int32_to_bytes(eof_bookmark))

		# Fill in pixel offset placeholder
		bmp.seek(pixel_offset_bookmark)
		bmp.write(_int32_to_bytes(pixel_data_bookmark))


def dimensions(filename):
	with open(file=filename, mode='rb') as f:
		magic = f.read(2)
		if magic != b'BM':
			raise ValueError(f"{filename} is not a BMP file")
		f.seek(18)
		width_bytes = f.read(4)
		height_bytes = f.read(4)
		return (_bytes_to_int32(width_bytes),
				_bytes_to_int32(height_bytes))

def _int32_to_bytes(i):
	"""Convert an integer to four bytes in little-endian format."""

	return bytes((i & 0xff,
	 			  i >> 8 & 0xff,
	  			  i >> 16 & 0xff,
	   			  i >> 24 & 0xff))


def _bytes_to_int32(b):
	"""Convert an bytes to four integer in little-endian format."""

	return b[0] | (b[1] << 8) | (b[2] << 16) | (b[3] << 24) 

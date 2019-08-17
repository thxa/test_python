# https://wiki.python.org/moin/BitwiseOperators
# https://docs.python.org/3/library/stdtypes.html#bitwise-operations-on-integer-types
# https://docs.python.org/3.2/library/stdtypes.html#bitwise-operations-on-integer-types
"""
	& is And examples:
					  1 And 1 = 1 
					  1 And 0 = 0  
					  0 And 0 = 0  
	

	| is Or examples:
					 1 Or 1 = 1
					 1 Or 0 = 1
					 0 Or 0 = 0
	

	^ is Exclusive-Or(XOR) examples:
									1 XOR 1 = 0
									1 XOR 0 = 1
									0 XOR 0 = 0

	~ is Not examples: 
					Not 1 = 0
					Not 0 = 1
	

	<<  is Left shift examples:
		00000000 is 8-bit

		00000001 
		1 << 0 = 1
		
		00000010
		1 << 1 = 2
		
		00000100
		1 << 2 = 4
		
		00001000
		1 << 3 = 8
		
		00010000
		1 << 4 = 16
		
		00100000
		1 << 5 = 32
		
		01000000
		1 << 6 = 64
		
		01000000
		1 << 7 = 128
		
		10000000
		1 << 8 = 256
			

	>> is Right shift 9-bit 100000000 = 256

		100000000
		256 >> 0 = 256

		010000000
		256 >> 1 = 128

		001000000
		256 >> 2 = 64

		000100000
		256 >> 3 = 32

		000010000
		256 >> 4 = 16

		000001000
		256 >> 5 = 8

		000000100
		256 >> 6 = 4

		000000010
		256 >> 7 = 2

		000000001
		256 >> 8 = 1

		000000000
		256 >> 9 = 0
"""
# binary
print(0b11110000)
print(bin(240))

# XOR
print(bin(0b11100100 ^ 0b00100111)) 
"""
11100100
00100111
XOR

11000011
"""

# Not
print(bin(~0b11110000))
"""
	11110000
	Not
	00001111
"""

"""
	Signed decimal							Unsigned decimal 
	-127 <= x <= 128						0 <= x <= 255 
	 -58 -> abs -> 58 -> 00111010  == 58
						 flip(Not)
						 11000101  == 197
						 add 1
						 11000110  == 198
"""

print(bin(4))
print(bin(-4))


v = 0b11110000 # 8-bit
print(v)  # =  011110000 9-bit <-  240 <- +0b11110000 
print(~v) # =  100001111 9-bit -> -241 -> -0b11110001
		  #								   abs
		  #								   11110001
		  #								   flip(NOT)
		  #								   00001110
		  #								   add 1
		  #								   00001111

def twos_complement(x, num_bits):
	if x < 0:
		return x + (1 << num_bits)
	return x

print(twos_complement(~v, 8)) # 0b00001111
print(bin(twos_complement(~v, 8)))

print(bin(~0b11110000 & 0b11111111))  # 8-bit and 8-bit = 0b1111 8-bit
print(bin(~0b11110000 & 0b111111111)) # 8-bit and 9-bit = 0b100001111 9-bit

# https://docs.python.org/3.2/library/stdtypes.html#int.bit_length
print(int(32).bit_length())  # 6-bit
print(int(240).bit_length()) # 8-bit
print(int(241).bit_length()) # 8-bit
print(int(256).bit_length()) # 9-bit
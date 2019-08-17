print(b"This is Ok because it's 7-bit ASCII")


# print(ord("أ"))
# print(ord("و"))

# print(b"Norwegian characters like أ and و are not 7-bit ASCII")
print(b"Norwegian characters like \xd8\xa3 and \xd9\x88 are not 7-bit ASCII")
norsk = b"Norwegian characters like \xd8\xa3 and  \xd9\x88 are not 7-bit ASCII"

print(norsk.decode("utf-8"))
print(norsk[0])
print(norsk[21:25])

# print(ord('أ'))
# print(ord('و'))
# print(chr(1608))
# print(chr(1571))

# print(bytes("Norwegian characters أ and و are not 7-bit ASCII", "utf-8"))
print(bytes("Norwegian characters أ and و", "utf-16"))

# from str to bytes to hex format utf-8
print(bytes("The quick brown fox", "utf-8").hex())
# from hex to bytes
print(bytes.fromhex("54686520717569636b2062726f776e20666f78"))


print(bytes())
print(bytes(5))
print(bytes(range(65, 65+26)))
# print(bytes([63, 127, 255, 511]))

text = "Hello World"
text_to_bytes = bytes(text, "utf-8")

print(text_to_bytes)

bytes_to_hex = text_to_bytes.hex()
print(bytes_to_hex)


print("-> str = {} \n-> bytes -> {} \n-> hex -> {}".format(text, text_to_bytes, bytes_to_hex))

# bytes("The quick brown fox", "utf-8").hex() = ''.join(hex(c)[2:] for c in b"The quick brown fox")

print(hex(b"T"[0])) # 0x54

print(hex(b"T"[0])[2:]) # 54

print(list(c for c in b"The quick brown fox"))

print(''.join(hex(c)[2:] for c in b"The quick brown fox"))

print(bytes("The quick brown fox", "utf-8").hex() == ''.join(hex(c)[2:] for c in b"The quick brown fox"))

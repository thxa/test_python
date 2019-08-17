# https://docs.python.org/3.2/library/stdtypes.html#int.to_bytes
print(int(0xcafebabe).to_bytes(length=4, byteorder="big"))
print(int(0xcafebabe).to_bytes(length=4, byteorder="little"))


import sys

print(sys.byteorder)

little_cafebabe = int(0xcafebabe).to_bytes(length=4, byteorder=sys.byteorder)

print(little_cafebabe)
# https://docs.python.org/3.2/library/stdtypes.html#int.from_bytes
number_of_hex = int.from_bytes(little_cafebabe, byteorder=sys.byteorder)
print(number_of_hex)
print(hex(number_of_hex))

# print(int(-241).to_bytes(length=2, byteorder="little"))
print(int(-241).to_bytes(length=2, byteorder="little", signed=True))
print(bin((~0b11110000).to_bytes(2, byteorder="little", signed=True)[0]))

# number_from_bytes = int.from_bytes(b'\x00Thamer AL-Harbi', "big")
# print(number_from_bytes)
# print(int(number_from_bytes).to_bytes(16, "big"))
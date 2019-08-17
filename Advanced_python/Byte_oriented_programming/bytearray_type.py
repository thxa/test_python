print(bytearray())
print(bytearray(5))
print(bytearray(b"Construct from a sequence of bytes"))
print(bytearray("Norwegian characters أ and و", "utf-8"))
print(bytearray.fromhex("54686520717569636b2062726f776e20666f78"))

s = "54686520717569636b2062726f776e20666f78"

print(" ".join(s[c] + s[c + 1] for c in range(len(s) - 1)))

print(" ".join(s[c:c+2] for c in range(0, len(s) - 1)))

print(" ".join(s[c:c+2] for c in range(0, len(s), 2)))

pangram = bytearray(b"The quick brown fox")
print(pangram)
pangram.extend(b" jumps over the lazy dog")
print(pangram)
pangram[40:43] = b"cat"
print(pangram)

print(pangram.upper())
print(pangram.lower())

words = pangram.split()
print(words)

print(bytearray(b' '.join(words)))

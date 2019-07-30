positevies = filter(lambda n: n > 0, [1, -4, 10, 0, 2, -5, -3, -6, 50, 10, -1, 0])

print(list(positevies))

trues = filter(None, ['test', 0, '', [], 12, None, True, False, 1, 0])
print(list(trues))
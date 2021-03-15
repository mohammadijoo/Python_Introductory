def test2():
    return 'abc', 100, [0, 1, 2]

a, b, c = test2()

print(a)		# abc
print(b)	# 100
print(c)		# [0, 1, 2]
_, x, _ = test2()
print(x)	# 100

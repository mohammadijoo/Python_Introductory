def test():
    return 'abc', 100
result = test()

print(result[2])		# IndexError: tuple index out of range

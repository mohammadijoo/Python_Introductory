def test():
    return 'abc', 100

_, x = test()		
print(x)	   # 100
x, _ = test()		
print(x)	   # abc

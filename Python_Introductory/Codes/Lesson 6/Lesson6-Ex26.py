def test():
    return 'abc', 100
result = test()

print(result[0])	 	     # abc
print(type(result[0]))        # <class 'str'>
print(result[1])                  # 100
print(type(result[1]))        # <class 'int’>


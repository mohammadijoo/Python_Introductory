i = int(input("enter the start of range: "))
j = int(input("enter the end of range: "))


def test_range(n):
    if n in range(i,j):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
test_range(5)

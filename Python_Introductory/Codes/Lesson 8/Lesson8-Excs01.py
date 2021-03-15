
def string_reverse(s):
    str1 = ''
    index = len(s)
    while index > 0:
        str1 += s[index - 1]
        index = index - 1
    return str1


x = input("Enter a string: ")
print("Rverse is: ", string_reverse(x))

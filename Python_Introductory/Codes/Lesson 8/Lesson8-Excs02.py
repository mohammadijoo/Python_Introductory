def charChange(x):
    s = ""
    for i in range(0, len(x)):
       if x[i].islower() == True:
           s += x[i].upper()
       else:
           s += x[i].lower()
    return s

strg = input("Enter a string: ")
print("Result is: ", charChange(strg))

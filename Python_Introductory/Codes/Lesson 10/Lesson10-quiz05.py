fileName = input("Enter filename: ")
line1 = int(input("Enter start row: "))
line2 = int(input("Enter end row: "))

myFile = open(fileName, 'r')
lines = myFile.readlines()
myFile.close()
print(lines[line1-1 : line2])

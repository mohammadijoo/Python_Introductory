fileName = input("Enter name of file: ")
n = int(input("Enter n: "))
myFiles = open(fileName)
lines = myFiles.readlines()
for i in range(n-1 , len(lines)):
    print(lines[i] , end='')

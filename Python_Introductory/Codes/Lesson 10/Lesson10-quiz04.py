fileName = input("Enter name of file: ")
n = int(input("Enter n: "))
myFiles = open(fileName)
lines = myFiles.readlines()
lines=[i.rstrip("\n") for i in lines]  
for i in range(1 , n+1):
    print(lines[-i])

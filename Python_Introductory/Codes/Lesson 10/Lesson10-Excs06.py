fileName = input("Name of file: ")
letter = input("Letter for count: ")
myfile = open(fileName, "r")
countLetter = 0
while True:
    line = myfile.readline()
    if line !="":
        for i in range(0, len(line)):
            if line[i] == letter:
                countLetter = countLetter + 1
    else:
        break
myfile.close()
print("Amount of letter" , countLetter)
                

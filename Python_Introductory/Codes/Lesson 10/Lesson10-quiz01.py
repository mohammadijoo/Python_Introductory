def ReplaceTextFile(urlFile, textReplace, newText):
    myfileRd = open(urlFile , "r")
    myfileWr = open("newfile.txt" , "w")
    while True:
        line = myfileRd.readline()
        if line != "":
            line = line.replace(textReplace , newText)
            myfileWr.write(line)
        else:
            break
    myfileWr.close()
    myfileRd.close()

def main():
    fileName = input("Enter name of file: ")
    oldString = input("Enter old string: ")
    newString = input("Enter new string: ")
    ReplaceTextFile(fileName, oldString, newString)

main()

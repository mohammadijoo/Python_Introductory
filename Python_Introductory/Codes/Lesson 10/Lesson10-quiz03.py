fileName1 = input("Enter file name1: ")
fileName2 = input("Enter file name2: ")

with open(fileName1) as fh1, open(fileName2) as fh2:
    content1 = fh1.read()
    content2 = fh2.read()

print(content1)
print(content2)

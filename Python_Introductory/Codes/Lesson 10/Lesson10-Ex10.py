file = open("example.txt", 'r')
content = file.read()
print(content)
file.seek(0)

print("\n\n\n")
content2 = file.readline() 
print(content2)

"""This script creates an empty file"""

filename="sample1.txt"

#create empty file
def create_file():
    with open(filename,"w") as file:
        file.write("") #writing empty string

create_file()

import datetime
filename=datetime.datetime.now()
print(filename)
def create_file():
    with open(filename.strftime("%Y-%B-%d-%H-%M") + ".txt", "w") as file:
        file.write("salam")
        file.close()
create_file()


def display(x , y):
    for i in range(x, y+1):
        if i % 2 != 0:
            print(" ", i , end=' ')

def main():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print("Odd numbers are: ", end='')
    display(x, y)

main()

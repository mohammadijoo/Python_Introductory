
def fact(n):
    f = 1
    for i in range(n, 1, -1):
        f *= i
    return f

def sumFact(n):
    sum = 0
    for i in range(1, n+1):
        sum += fact(i)
    return sum

def main():
    n = int(input("Enter n: "))
    print("Sum is: ", sumFact(n))

main()
    

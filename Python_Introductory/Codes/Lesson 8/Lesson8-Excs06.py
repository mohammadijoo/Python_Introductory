s=1
pow=1
sum=0
sum1=0

x = int(input("Enter the number for x: "))
n = int(input("Enter the number for n: "))

for i in range(1,n+1):
        pow = pow * x
        sum1 = sum1 + i * pow
        sum = sum + s * 1/sum1
        s=-s

print("Sum is: ", sum)



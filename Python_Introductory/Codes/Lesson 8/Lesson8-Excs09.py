def C_nk(n , k):
        if n==0 or n==k or k==0:
                return 1
        elif k==1:
                return n
        elif k>n:
                print("n should be equal or greater than k")
        else:
                return C_nk(n-1 , k) + C_nk(n-1 , k-1)

def main():
        n = int(input("Enter n: "))
        k = int(input("Enter k: "))               
        print("Result is: ", C_nk(n,k))

main()

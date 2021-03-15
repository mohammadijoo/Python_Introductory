def catalanNumber(num):
        if num <=1:
                return 1
        res_num = 0
        for i in range(num):
                res_num += catalanNumber(i) * catalanNumber(num-i-1)
        return res_num

def main():
        n = int(input("Enter n: "))
        print("result is: ", end='')
        for x in range(1,n+1):
                print(catalanNumber(x), end='\t')
main()

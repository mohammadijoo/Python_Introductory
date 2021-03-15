while True:
        num = int(input("Enter a number: "))
        sum = 0
        for i in range(1, num):
                if (num % i == 0):
                        sum += i
        if (sum == num):
                print('\t', "Entered number is prefect")
        else:
                print('\t', "Entered number is NOT prefect")
        Question= input("Continiue? (y/n) ")
        if (Question[0]=='n' or Question[0]=='N'):
                break
        


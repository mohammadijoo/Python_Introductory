from random import randint

val = randint(0,10)
def guessANumber(val):
        guess = int(input('Enter your guess: '))
        if guess > val:
                print('it is high.')
                return 1
        elif guess < val:
                print('it is low.')
                return -1
        else:
                print('Congratulations!!! Your guess is rigth.')
                return 10000
        
while(guessANumber(val)!=10000):
        print('Guess Again.')
        guessANumber(val)


#print("original number is: ", val)

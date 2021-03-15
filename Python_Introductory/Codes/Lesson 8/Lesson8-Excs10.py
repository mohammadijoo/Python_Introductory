def countVowels(my_string):
        count = 0
        for s in my_string:
                if s.lower() in 'aeiou':
                        count += 1
        return count

stg = input('Enter your string: ')
print('The entered string has ' + str(countVowels(stg)) + ' vowels in it.')



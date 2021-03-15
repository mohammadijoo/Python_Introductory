def sortString(s1):
        flag = 1
        s = s1
        while flag == 1:
                flag = 0
                for i in range(0, len(s)-1):
                        if s[i] > s[i+1]:
                                s2=""
                                for j in range(0,i):
                                        s2 = s2 + s[j]
                                s2 = s2 + s[i+1] + s[i]
                                for j in range(i+2, len(s)):
                                        s2 = s2 + s[j]
                                s=s2
                                flag = 1
        s1= ""
        for ch in s:
                s1 = s1 + ch
        return s1
def main():
        count = 0
        max = 0
        maxch = chr(0)
        t = chr(0)
        s = input("Enter a string: ")
        s = sortString(s)
        t = s[0]
        for i in range(1, len(s)):
                if s[i] == t:
                        count = count + 1
                else:
                        count = 0
                if count > max:
                        max = count
                        maxCh = s[i]
                t = s[i]
        print("Max Char Repeat: ", maxCh)
        print("Count Repeat: ", max+1)

main()
                
                                        


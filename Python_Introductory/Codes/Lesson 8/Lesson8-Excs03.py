
def search_string(s1, s2):
    for i in range(0,len(s1)):
        k = i
        j = 0
        while j < len(s2) and k < len(s1) and s2[j] == s1[k]:
            j = j + 1
            k = k + 1
        if j == len(s2):
            return i + 1
        #if j == len(s2) and k == len(s1):
            #return i + 1
    return 0

def main():
    s1 = input("Enter string 1: ")
    s2 = input("Enter string 2: ")
    location = search_string(s1, s2)
    if location != 0:
        print("Found in location ", location)
    else:
        print("Not found ")

main()

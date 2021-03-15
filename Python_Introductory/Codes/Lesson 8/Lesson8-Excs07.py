s1 = input("Enter string 1: ")
s2 = input("Enter string 2: ")
s3 = ""
count = 0
while count < len(s1) and count < len(s2):
        s3 += s1[count]
        s3 += s2[count]
        count = count + 1
if count == len(s1) and count < len(s2):
        while count < len(s2):
                s3 += s2[count]
                count = count + 1
elif count == len(s2) and count < len(s1):
        while count < len(s1):
                s3 += s1[count]
                count = count + 1

print("String S3: " , s3)

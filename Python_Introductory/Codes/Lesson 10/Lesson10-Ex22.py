with open("example.txt", "a+") as file:
     file.seek(0) 
     content = file.read() 
     file.write("\nLine 6")
     file.close()
# Result: Reopen example.txt and you see line 6 at the end of file

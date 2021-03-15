def string_length(mystring): 
     if type(mystring) == int: 
          return "Sorry, integers don't have length" 
     elif type(mystring) == float: 
           return "Sorry, floats don't have length" 
     else: 
            return len(mystring)

#x = string_length(3.7)
#print(x)

import re

 #indian mobile number validation 
def isValid(s): 

    Pattern = re.compile("(0/91)?[7-9][0-9]{9}") 
    return Pattern.match(s) 

s = input("enter u r 10 digit valid mobile number:")
#print(type(s))

if (isValid(s)):  
    print ("Valid Number")      
else : 
    print ("Invalid Number") 

import re 
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
 
def check(email):  
  
    if(re.search(regex,email)):  
        print("Valid Email")  
          
    else:  
        print("Invalid Email")  
      
  
      
 
email = "ankitrai326@gmail.com"
      
    # calling run function  
check(email) 
  
email = "my.ownsite@ourearth.org"
check(email) 
  
email = "ankitrai326.com"
check(email) 
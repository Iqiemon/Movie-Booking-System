import re   
  
regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'  
  
 
  
    
      
if __name__ == '__main__' :   
      
    email = str(input("Please enter email:"))
    if(re.search(regex,email)):   
        print("Valid Email")   
    else:   
        print("Invalid Email")   

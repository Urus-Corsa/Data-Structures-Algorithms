def convertor(decimalNumber):
    
    assert int(decimalNumber) == decimalNumber and decimalNumber >= 0, "decimalNumber must be a positive integer" 
    #edge cases to provide avoid failure points of function
   
    if int(decimalNumber/2) == 0: #base condtion to avoid infintie recursion
       return decimalNumber%2  
    else:
        return int(decimalNumber%2 + (10 * convertor(int(decimalNumber/2)))) 
        #in each divison of decimalNumber by 2, from last divison to first, 
        #multiply last remainder from bottom by 10 and add to previous remainder from bigger division recursively
   

def gcd(a,b):
    assert a > 0 and b > 0, "zero is not a common factor of any number" #edge cases to avoid infinite recursion
    if a == 1: #base conditions if any of two numbers is 1 then terminate recursion
        return 1
    elif b == 1: #base condition to return 1 if one of the numbers is 1 as the GCD
        return 1
    elif a == b:  
        return a 
    x = max(a,b) #find the largest number
    y = min(a,b) #find the smallest number
    
    if x%y == 0: #base condition where the latgest number is divisble by the smallest
        return y #return smaller number as GCD between the two numbers
    else:
        return gcd(y,x%y) #recursivley divide smallest number by remainder to reach on of the base condition

print(gcd(55,1))
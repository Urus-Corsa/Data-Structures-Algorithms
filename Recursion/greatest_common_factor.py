def gcd(a,b):
    assert a > 0 and b > 0, "zero is not a common factor of any number"
    if a == 1:
        print("test1")
        return 1
    elif b == 1:
        print("test2")
        return 1
    elif a == b:
        return a 
    x = max(a,b)
    y = min(a,b)
    
    if x%y == 0: 
        return y 
    else:
        return gcd(y,x%y)

print(gcd(55,1))
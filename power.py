def powerd(a,n):
    r=a
    for i in range(1,n):
        r=r*a
    return r

def power(a,n):
    if(n==0):
        return 1
    x=power(a,n//2)
    if(n%2==0):
        return x*x
    else:
        return a*x*x
    
    
    
    
    
    
    
    
    
    
    
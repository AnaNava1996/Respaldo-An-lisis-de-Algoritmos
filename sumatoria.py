def testp(n):
    for k in range(2,n):
        if n%k==0:
            return 0
    return 1

def listp(n):
    p=[]
    for l in range(2,n+1):
        if(testp(l)!=0):
            p=p+[l]
    return p



'''

sumatoria de k de 1 a n... (1+2+...+n)  =  (n^2 + n) / 2

'''
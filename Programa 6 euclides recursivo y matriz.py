def euclides(a,b):
    if(a%b==0):
        return b
    else:
        return euclides(b,a%b)

def euclidex(a,b):
    if(a%b==0):
        return 0,1,b
    else:
        m,n,r = euclidex(b,a%b)
        return n,m-(a//b)*n,r
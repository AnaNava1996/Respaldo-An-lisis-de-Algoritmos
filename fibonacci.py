#fibonacci recursivo?... sin recalcular tanto...

fibb={0:0,1:1}

'''Es mi favorito porque usa tuplas, y es mas rapido ya que el programa no recalcula'''
def fib(n):
    if not(n in fibb.values()):
        fibb[n]=(fib(n-1)+fib(n-2))
    return fibb[n]


def fib2(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    elif(n==2):
        return 1
    else:
        return(fib2(n-2)+fib2(n-1))


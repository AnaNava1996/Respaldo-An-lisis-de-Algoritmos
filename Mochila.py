import numpy
def knap():
    v=[0,10,40,30,50]
    we=[0,5,4,6,3]
    w=10
    n=len(v)
    vm=numpy.zeros(n,w+1)
    for i in range(1,n):
        for w in range(1,w+1):
            if we[i]<=w:
                vm[i,w]=max(vm[i-1,w],v[i]+vm[i-1,w-we[i]])
            else:
                vm[i,m]=vm[i-1,w]
    return vm
print(int(knap()))

def ordenar(a):##################################################### Intuitivo
    list2=[]
    for i in range(len(a)):
        list2.append(min(a))
        a.remove(min(a))
    print(list2)

def mergesort(a):################################################## Merge Sort
    if(len(a)==1):
        return a
    else:
        return merge(mergesort(a[0:len(a)//2]),mergesort(a[len(a)//2:len(a)]))

def merge(a,b):
    c=[]
    while((len(a)>=0) and (len(b)>=0)):
        if(len(a)==0 or len(b)==0):
            break
        elif(a[0]>b[0]):
            c.append(b[0])
            b.remove(b[0])
        else:
            c.append(a[0])
            a.remove(a[0])
    while(len(a)>0):
        c.append(a[0])
        a.remove(a[0])
    while(len(b)>0):
        c.append(b[0])
        b.remove(b[0])
    return c    

a=[3,5,8,2,1,4,0,9]
print(mergesort(a))

ordenar(a)
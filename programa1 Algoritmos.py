def sbin(z,num):
    n=len(z)#es 8
    m=int(n/2)#es 4
    p=int(n/2)#es 4
    print("p="+str(p)+"  m="+str(m))
    while(num!=z[m]):
        if(p==0):
            print("el numero no se encuentra")
            break
        elif(num<z[m]):
            p=int(p/2)
            m=m-p
            print("p="+str(p)+"  m="+str(m))
        elif(num>z[m]):
            p=int(p/2)
            m=m+p
            print("p="+str(p)+"  m="+str(m))
    if(num==z[m]):
        print("El numero se encuentra en la posicion:"+str(m))    


def search(a,x):
    if len(a)==1:
        if x==a[0]:
            print("el numero: "+str(a[0])+" se encuentra")
            return 0
        else:
            return 0
    else:
        if x<a[int(len(a)/2)]:
            return search(a[:int(len(a)/2)],x)
        else:
            return search(a[int(len(a)/2):],x)

a=[1,2,3,4,5,6,7,8]
x=int(2) #este es el numero a buscar....
#se puede poner: input("numero a buscar: ")
#search(a,x)

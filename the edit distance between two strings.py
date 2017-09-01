a=['','v','i','n','t','n','e','r']
b=['','w','r','i','t','e','r','s']
def t(i,j):
    if(a[i]==b[j]):
        return 0
    else:
        return 1
def D(i,j):
    if(i==0):
        return j
    elif(j==0):
        return i
    return min(D(i,j-1)+1,D(i-1,j)+1,D(i-1,j-1)+t(i,j))


print(D(7,7))

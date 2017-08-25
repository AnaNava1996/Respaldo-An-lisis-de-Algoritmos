def invertir(list):
    if(len(list)==1 or len(list)==0):
        return list
    else:
        return invertir(list[1:])+[list[0]]

    
list=[9,8,7,6,5,4,3,2,1]
print(invertir(list))
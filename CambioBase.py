def cambioBase(n,b):
    if(n<b):
        return [n]
    else:
        return cambioBase(n//b,b)+[n%b]
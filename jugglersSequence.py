import math
def juggler(n):
    a=n
    print(a,end=" ")
    while(a!=1):
        b=0
        if(a%2==0):
            b=math.floor(math.sqrt(a))
        else:
            b=math.floor(math.sqrt(a)*math.sqrt(a)*math.sqrt(a))
        print(b,end=" ")
        a=b
    print()

juggler(6)
import math
t=int(input())
while(t):
    t-=1
    x,k=map(int,input().split())
    f=1
    arr=[]
    while(x%2==0):
        arr.append(2)
        x=x//2
    for i in range(3,math.ceil(math.sqrt(x)),2):
        while(x%i==0):
            x=x/i
            arr.append(i)
    if(x>2):
        arr.append(x)
    if(len(arr)<k):
        f=0
    print(f)   

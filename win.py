import operator as op
from functools import reduce

def ncr(n,r,p): 
    num,den = 1,1 
    for i in range(r): 
        num = (num * (n - i)) % p 
        den = (den * (i + 1)) % p 
    return (num * pow(den, p - 2, p)) % p 
 
def ways(n,arr):
    s=0
    # print("x",l,r)
    for i in range(n):
        # print("i",i)
        s=s^arr[i]

    if(s==0):
        return 0

    temp=0  
    for i in range(n):
        leave=s^arr[i]
        if(arr[i]>leave):
            temp+=ncr(arr[i],leave,998244353)
    return int(temp)

t=int(input())
while(t):
    t-=1
    n=int(input())
    arr=[int(n) for n in input().split()]
    q=int(input())
    while(q):
        q-=1
        l,r=map(int,input().split())
        d={}
        for i in range(l-1,r):
            if arr[i] in d:
                temp=d[arr[i]]
                d[arr[i]]=temp+1
            else:
                d[arr[i]]=1
        tarr=[]
        for i in d:
            tarr.append(d[i])
        #print(tarr)
        print((ways(len(tarr),tarr))%998244353)
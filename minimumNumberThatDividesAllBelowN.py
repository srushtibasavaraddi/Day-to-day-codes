t=int(input())
import math 
  
def primeFactors(n): 
    while(n % 2 == 0): 
        d[2]=d.get(2,0)
        d[2]=d[2]+1
        n = n // 2
    for i in range(3,int(math.sqrt(n))+1,2): 
        
        while(n % i== 0): 
            d[i]=d.get(i,0)
            d[i]=d[i]+1
            n = n // i 
           
    if (n > 2): 
        d[n]=d.get(n,0)
        d[n]=d[n]+1

while(t):
    t-=1
    n=int(input())
    dd={}
    for i in range(2,n+1):
        d={}
        primeFactors(i)
        for i in range(2,n+1):
            i_d=d.get(i,0)
            idd=dd.get(i,0)
            if(i_d>idd):
                dd[i]=i_d
        # print(d,dd)
    a=1
    for k,v in dd.items():
        # print(k,v)
        a=a*pow(k,v)
    print(a)


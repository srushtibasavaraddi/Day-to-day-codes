def belong(n):
    if((n%2==0) and (n%4!=0)):
        return True
    return False

t=int(input())
while(t):
    t-=1
    n=int(input())
    arr=[int(n) for n in input().split()]
    ans=((n)*(n+1))//2
    # print(ans)
    op,p,f,pp=0,0,0,0
    for i in arr:
        k=0
        if(belong(i)):
            k=1
        if(i==1):
            k+=p
            op+=1
            
        else:
            if(i%2==0):
                if(i%4!=0):
                    f=1
                    k+=op
                else:
                    f=0
                pp=op
                op=0
            else:
                if(f):
                    k+=1
                    k+=pp
                op+=1
        ans-=k
        p=k    
    print(ans)


            
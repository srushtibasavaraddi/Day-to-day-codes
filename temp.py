t=int(input())
while(t):
    t-=1
    n=int(input())
    arr=[int(n) for n in input().split()]
    ans=0
    # print(ans)
    # f=0
    for i in range(n):
        p=1
        for j in range(i,n):
            p*=arr[j]
            if((p%2==0) and (p%4!=0)):
                f=1
            else:
                ans+=1
            # print(p)
    print(ans)
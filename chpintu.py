t=int(input())
while(t):
    t=t-1
    n,m=map(int,input().split())
    f=[int(n) for n in input().split()]
    p=[int(n) for n in input().split()]
    d={}
    for i in range(n):
        if f[i] in d:
            d[f[i]]+=p[i]
        else:
            d[f[i]]=p[i]
        #print(d)
    m=9999999999
    for i in d:
        if(d[i]<m):
            m=d[i]
    print(m)

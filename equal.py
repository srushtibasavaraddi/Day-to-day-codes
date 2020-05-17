t=int(input())
while(t):
    t-=1
    n=int(input())
    arr=[int(n) for n in input().split()]
    m=min(arr)
    a=999999999
    for j in range(5):
        mm=m-j
        ans=0
        for i in arr:
            s=i-mm
            ans+=s//5
            s=s%5
            ans+=s//2
            s=s%2
            ans+=s//1
        if(ans<a):
            a=ans
    print(a)

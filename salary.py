t=int(input())
while(t):
    t-=1
    n,arr=int(input()),[int(n) for n in input().split()]
    print(sum(arr)-n*min(arr))
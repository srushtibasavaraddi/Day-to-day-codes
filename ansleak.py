def most_frequent(List): 
    return max(set(List), key = List.count) 

t=int(input())
while(t):
    t-=1
    n,m,k=map(int,input().split())
    ans=[]
    for i in range(n):
        arr=[int(k) for k in input().split()]
        ans.append(most_frequent(arr))
    print(*ans)
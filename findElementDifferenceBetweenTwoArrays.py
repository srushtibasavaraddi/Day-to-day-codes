import collections
n=int(input())
arr=[int(n) for n in input().split()]
m=int(input())
brr=[int(m) for m in input().split()]
ans=[]
ca=dict(collections.Counter(arr))
cb=dict(collections.Counter(brr))
for i in cb:
    tb=cb.get(i,0)
    ta=ca.get(i,0)
    if(tb>ta):
        ans.append(i)
print(*ans)


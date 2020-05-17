n,k=map(int,input().split())
arr=[int(n) for n in input().split()]
arr.append(0)
ans=0
c=0
for i in range(n):
    if(arr[i]==1):
        c+=1
        if(arr[i+1]==0):
            ans+=c//k
            c=0
            if(c%k!=0):
                ans+=1
    
print(ans)
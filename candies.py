n=int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))

ans=[1]
for i in range(1,n):
    if(arr[i]>arr[i-1]):
        ans.append(ans[i-1]+1)
    else:
        ans.append(1)
# print(arr)
for i in range(n-2,-1,-1):
    if(arr[i]>arr[i+1] and ans[i]<=ans[i+1]):
        ans[i]=ans[i+1]+1
# print(arr)
print(sum(ans))


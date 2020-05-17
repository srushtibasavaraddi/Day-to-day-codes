import math
n,k=int(input()),int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr=sorted(arr)
m=math.inf
for i in range(n-k+1):
    temp=arr[i+k-1]-arr[i]
    if(temp<m):
        m=temp
print(m)


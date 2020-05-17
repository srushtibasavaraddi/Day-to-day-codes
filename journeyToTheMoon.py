n,p=map(int,input().split())
arr=[i for i in range(n)]

def union(u,v):
    temp=arr[u]
    for i in range(len(arr)):
	    if(arr[i]==temp):
	        arr[i]=arr[v]
    return arr

for i in range(p):
    p-=1
    a,b=map(int,input().split())
    arr=union(a,b)
    # print(arr)
c=0
d={}
for i in range(n):
    if(arr[i] in d):
        temp=d[arr[i]]
        d[arr[i]]=temp+1
    else:
        d[arr[i]]=1
# print(d)
arr=[]
for i in d.values():
    # print(i)
    arr.append(i)

a=0
s=0
for i in range(len(arr)-1):
    s+=arr[i]
    a+=s*arr[i+1]
print(a)
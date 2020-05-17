import sys
n,p=map(int,input().split())
arr=[[0 for i in range(n)] for j in range(n)]
f=0
for i in range(p):
    a,b=map(int,input().split())
    arr[a-1][b-1]=1
    arr[b-1][a-1]=1
s=int(input())
l=int(input())
visited=[0 for i in range(n)]
c=0
def dfs(m,v,s,l):
    visited[s]=1
    for i in range(v):
        if(m[s][i]==1 and visited[i]==0):
            if(c!=l):
                print(i)
                c=c+1
            else:
                sys.exit()
            dfs(m,v,i) 
dfs(arr,n,s,l)

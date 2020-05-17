def noOfNoDes(source):
    visited[source]=1
    c=0
    for i in range(n):
        if((graph[source][i]==1) and (visited[i]==0)):
            c+=noOfNoDes(i)
    if((c+1)>1 and (n-(c+1))>1):
        global res
        res+=2
    return c+1

res=2
n=int(input())
graph=[[0 for i in range(n)] for j in range(n)]
for i in range(n-1):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1
visited=[0 for i in range(n)]
noOfNoDes(0)
print(res)
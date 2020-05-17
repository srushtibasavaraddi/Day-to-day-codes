import math
def findMin(dist,visited,n):
    m=math.inf
    mi=0
    for i in range(n):
        if(dist[i]<m and visited[i]==0):
            m=dist[i]
            mi=i
    return mi
def dijeckstra(graph,n,src):
    dist=[math.inf for i in range(n)]
    dist[src]=0
    visited=[0 for i in range(n)]

    for i in range(n):
        u=findMin(dist,visited,n)
        visited[u]=1
        for j in range(n):
            if(graph[u][j]>0 and visited[j]==0 and dist[j]>dist[u]+graph[u][j]):
                dist[j]=dist[u]+graph[u][j]
    return dist


n,m=map(int,input().split())
graph=[[0 for i in range(n)]for j in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    graph[a-1][b-1]=w
    graph[b-1][a-1]=w

print(dijeckstra(graph,n,0))
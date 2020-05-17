def union(arr,u,v):
    temp=arr[u]
    for i in range(len(arr)):
        if(arr[i]==temp):
            arr[i]=arr[v]
    return arr

def find(u,v):
    if(u==v):
        return True
    return False

def kruskal(graph,egdes,n):
    arr=[i for i in range(n)]
    s=0
    visited=set()
    edges=sorted(egdes,key=lambda e:graph[e[0]][e[1]])
    for i in edges:
        if(not find(arr[i[0]],arr[i[1]])):
            s+=graph[i[0]][i[1]]
            visited.add(i[0])
            visited.add(i[1])
            arr=union(arr,i[0],i[1])
    
    return s

n,m=map(int,input().split()) 
graph=[[0 for i in range(n)] for j in range(n)]
edges=set()
for i in range(m):
    u,v,w=map(int,input().split())
    graph[u-1][v-1]=w
    graph[v-1][u-1]=w
    edges.add((u-1,v-1))

print(kruskal(graph,edges,n))
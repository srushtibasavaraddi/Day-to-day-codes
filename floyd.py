import math
#works for directed graph looser
#can't handle negative cycle
def floyd(graph,n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j]=min(graph[i][j],graph[i][k]+graph[k][j])
    # for i in graph:
    #     print(i)
    return graph

n,m=map(int,input().split())
graph=[[math.inf for j in range(n)] for i in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    graph[a-1][b-1]=w
#initialising self node as 0
for i in range(n):
    graph[i][i]=0
graph=floyd(graph,n)
q=int(input())
while(q):
    q-=1
    a,b=map(int,input().split())
    if(graph[a-1][b-1]==math.inf):
        print(-1)
    else:
        print(graph[a-1][b-1])

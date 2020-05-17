import math 
#works for directed graph looser
#can't handle negative cycle
def floyd(graph,V): 
    """ dist[][] will be the output matrix that will finally 
        have the shortest distances between every pair of vertices """
    """ initializing the solution matrix same as input graph matrix 
    OR we can say that the initial values of shortest distances 
    are based on shortest paths considering no  
    intermediate vertices """
    dist = map(lambda i : map(lambda j : j , i) , graph) 
      
    """ Add all vertices one by one to the set of intermediate 
     vertices. 
     ---> Before start of an iteration, we have shortest distances 
     between all pairs of vertices such that the shortest 
     distances consider only the vertices in the set  
    {0, 1, 2, .. k-1} as intermediate vertices. 
      ----> After the end of a iteration, vertex no. k is 
     added to the set of intermediate vertices and the  
    set becomes {0, 1, 2, .. k} 
    """
    for k in range(V): 
  
        # pick all vertices as source one by one 
        for i in range(V): 
  
            # Pick all vertices as destination for the 
            # above picked source 
            for j in range(V): 
  
                # If vertex k is on the shortest path from  
                # i to j, then update the value of dist[i][j] 
                dist[i][j] = min(dist[i][j],dist[i][k]+ dist[k][j]) 
    for i in dist:
        print(i)

n,m=map(int,input().split())
graph=[[math.inf for j in range(n)] for i in range(n)]
for i in range(m):
    a,b,w=map(int,input().split())
    graph[a-1][b-1]=w
#initialising self node as 0
for i in range(n):
    graph[i][i]=0
graph=floyd(graph,n)
floyd(graph); 
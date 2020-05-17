def noOfNoDes(source):
    visited[source]=1
    c=0
    for i in range(n):
        if((graph[source][i]==1) and (visited[i]==0)):
            c+=noOfNoDes(i)
    return c+1

q=int(input())
while(q):
    q-=1
    n,m,cLib,cRoad=map(int,input().split())
    graph=[[0 for i in range(n)] for j in range(n)]
    for i in range(m):
        a,b=map(int,input().split())
        graph[a-1][b-1]=1
        graph[b-1][a-1]=1

    if(cLib<=cRoad):
        print(n*cLib)
    else:
        visited=[0 for i in range(n)]
        ans=0
        for i in range(n):
            if(visited[i]==0):
                temp=noOfNoDes(i)
                ans+=(temp-1)*cRoad+cLib
        print(ans)

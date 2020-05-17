res=0

n,e=map(int,input().split())
graph=[[0 for i in range(n)] for j in range(n)]
for i in range(e):
    a,b=map(int,input().split())
    graph[a-1][b-1]=1
    graph[b-1][a-1]=1

def dfs(source):
    visited[source]=1
    c=0
    for i in range(n):
        if((graph[source][i]==1) and (visited[i]==0)):
            temp=dfs(i)
            if(temp%2==0):
                global res
                res+=1
            else:
                c+=temp
    return c+1

visited=[0 for i in range(n)]
dfs(0)
print(res)


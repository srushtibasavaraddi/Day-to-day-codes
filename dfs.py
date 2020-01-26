m=[[0, 1, 1, 0, 0],
   [1, 0, 0, 1, 1],
   [1, 0, 0, 0, 1],
   [0, 1, 0, 0, 0],
   [0, 1, 1, 0, 0]]

v=5   
visited=[0 for i in range(v)]
source=4

def dfs(m,v,source):
	visited[source]=1
	for i in range(v):
		if(m[source][i]==1 and visited[i]==0):
			print(i)
			dfs(m,v,i) 


print(source)
dfs(m,v,source)

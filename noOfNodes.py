def noOfNodes(source):
    visited[source]=1
    c=0
    for i in range(n):
        if((graph[source][i]==1) and (visited[i]==0)):
            c+=noOfNodes(i)
    # print(source,c+1)
    return c+1

import math
def isSafe(row, col, visited):
    return ((row>=0 and row<r) and (col>=0 and col<c) and arr[row][col] and (not visited[row][col]))

def dfs(row, col, visited, count): 
    rowNbr = [-1,-1,-1,0,0,1,1,1]  
    colNbr = [-1,0,1,-1,1,-1,0,1]  
    visited[row][col]=True
    for k in range(8): 
        if(isSafe(row+rowNbr[k],col+colNbr[k],visited)):                           
            count[0]+=1
            dfs(row+rowNbr[k],col+colNbr[k],visited,count) 

def largestArea(): 
    visited = [[0] * c for i in range(r)] 
    ans= -math.inf
    for i in range(r): 
        for j in range(c): 
            if(arr[i][j] and (not visited[i][j])):                  
                # NOT visited implies new region
                #count is a list because list in python is pass by refrence lol.
                count=[1]
                dfs(i,j,visited,count)  
                ans=max(ans,count[0]) 
    return ans 
  
r,c=int(input()),int(input())
arr=[[int(c) for c in input().split()] for i in range(r)]
print(largestArea())
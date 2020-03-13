def root(arr,i):
	while(arr[i]!=i):
		i=arr[i]
	return i
def union(arr,u,v):
	arr[root(arr,u)]=root(arr,v)
	return arr

def find(u,v):
	if(root(arr,u)==root(arr,v)):
		return True
	return False

arr=[0,1,2,3,4,5,6,7,8,9]
arr=union(arr,2,1)
print(arr)

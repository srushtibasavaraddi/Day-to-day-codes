def union(arr,u,v):
	temp=arr[u]
	for i in range(len(arr)):
		if(arr[i]==arr[u]):
			arr[i]=arr[v]
	return arr

def find(u,v):
	if(u==v):
		return True
	return False

arr=[0,1,2,3,4,5,6,7,8,9]
arr=union(arr,2,1)
print(arr)

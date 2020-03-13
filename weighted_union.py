def root(arr,i):
	while(arr[i]!=i):
		i=arr[i]
	return i

def weighted_union(arr,size,u,v):
	rootu=root(arr,u)
	rootv=root(arr,v)	
	if(size[rootu]>size[rootv]):
		arr[rootv]=rootu
		size[rootu]+=1		
	else:
		arr[rootu]=rootv
		size[rootv]+=1
				
def find(u,v):
	if(root(arr,u)==root(arr,v)):
		return True
	return False

arr=[0,1,2,3,4,5]
size=[1 for i in range(len(arr))]
weighted_union(arr,size,0,1)
weighted_union(arr,size,1,2)
weighted_union(arr,size,3,2)
print(arr,size)

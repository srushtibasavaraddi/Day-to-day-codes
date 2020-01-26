max_wt=7
wt=[1,3,4,5]
val=[1,4,5,7]

arr=[[0 for j in range(max_wt+1)] for i in range(len(wt)+1)]

for i in range(len(val)+1):
	for j in range(max_wt+1):
		if(i==0):
			arr[i][j]=0
		elif(wt[i-1]<=j):
			arr[i][j]=max(arr[i-1][j],val[i-1]+arr[i-1][j-wt[i-1]])
		else:
			arr[i][j]=arr[i-1][j]
	print(arr[i])

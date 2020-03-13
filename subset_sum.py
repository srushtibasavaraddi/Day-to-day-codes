ss=[1,2,3,5,7]
s=9
arr=[[0 for j in range(s+1)] for i in range(len(ss)+1)]


for i in range(len(ss)+1):
	arr[i][0]=1

for i in range(1,len(ss)+1):
	for j in range(1,s+1):
		if(arr[i-1][j]==1):
			arr[i][j]=1
		else:
			if(j<ss[i-1]):
			#i-1 because 3rd element will be avaliable there
				arr[i][j]=0
			else:
				if(arr[i-1][j-ss[i-1]]==1):
					#print(i,j)
					arr[i][j]=1
for i in range(len(ss)+1):
	print(arr[i])

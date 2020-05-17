t=int(input())
while(t):
	t=t-1
	mat=[]
	'''
	mat=[[1,1,2,3,3,3,3,4],
		 [1,2,3,4,2,3,1,2],
		 [2,3,6,3,2,3,6,1],
		 [3,4,3,3,3,4,3,1],
		 [3,5,2,3,4,5,4,3],
		 [3,5,6,4,1,4,6,1],
		 [3,5,6,3,1,3,6,1]]
	 
	mat=[[3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3],
		 [3,3,3,3,3,3,3,3]]
	'''
	n,m=map(int,input().split())
	ans=n*m
	
	for i in range(n):
		temp=[int(m) for m in input().split()]
		mat.append(temp)
	
	tt=0
	ttt=0
	for i in range(1,n-1):
		for j in range(1,m-1):
			if((mat[i-1][j]==mat[i+1][j])and(mat[i][j+1]==mat[i][j-1])):
				tt=tt+1
				f=1
			else:
				f=0
			k=2
			#print(i,j,f)
			while( ((i-k)>=0) and ((i+k)<n) and ((j-k)>=0) and ((j+k)<m) and (f==1) ):
				#print("ss")
				if((mat[i-k][j]==mat[i+k][j])and(mat[i][j+k]==mat[i][j-k])):
					f=1
					ttt=ttt+1
				else:
					f=0
				k=k+1
	#print(ans,tt,ttt)
	print(ans+tt+ttt)
	
	
	
	
	

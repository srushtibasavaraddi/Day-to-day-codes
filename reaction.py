t=int(input())
while(t>0):
	t=t-1
	r,c=map(int,input().split())
	grid=[[int(c) for c in input().split()] for i in range(r)]	
	s=1	
	for i in range(r):
		for j in range(c):
			if( (i==0 and j==0) or ((i==0) and j==(c-1)) or ( i==(r-1) and j==0 ) or ( i==(r-1) and j==(c-1) )):
				if(grid[i][j]>=2):
					s=0	  
			elif(i==0 or j==0 or i==(r-1) or j==(c-1)):
				if(grid[i][j]>=3):
					s=0
			else:
				if(grid[i][j]>=4):
					s=0
	if(s==1):
		print("Stable")
	else:
		print("Unstable")


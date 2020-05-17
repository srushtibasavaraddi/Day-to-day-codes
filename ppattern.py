t=int(input())
while(t):
	t-=1
	n=int(input())
	arr=[[0]*n for i in range(n)]
	c=0
	no=1
	for i in range(n):
		r=0
		c=i
		for j in range(i+1):
			arr[r+j][c-j]=no
			no+=1
	i=0
	for i in range(n-1):
		c=n-1
		r=i+1
		for j in range(n-1-i):
			arr[r+j][c-j]=no
			no+=1
	
	for i in range(n):
		for j in range(n):
			print(arr[i][j],end=' ')
		print()

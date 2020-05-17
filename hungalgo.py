t=int(input())
while(t):
	t=t-1
	dr={}
	dc={}
	n=int(input())
	arr=[[int(n) for n in input().split()] for n in range(n)]
	for i in range(n):
		for j in range(n):
			if(arr[i][j]==0):
				dr[i]=0
				dc[j]=0
	if((len(dr)==n) and (len(dc)==n)):
		print("YES")
	else:
		print("NO")

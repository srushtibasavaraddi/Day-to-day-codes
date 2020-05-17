t1=int(input())
while(t1):
	t1=t1-1
	n,m,k,l,r=map(int,input().split())
	arr=[]
	while(n):
		n=n-1
		t,p=map(int,input().split())
		for i in range(m):
			if(t>(k+1)):
				t=t-1
			elif(t<(k-1)):
				t=t+1
			else:
				t=k
		if(t>=l and t<=r):
			arr.append(p)
	if(arr):
		print(min(arr))
	else:
		print("-1")


t=int(input())
while(t>0):
	t=t-1
	n,m=map(int,input().split())
	arr={}
	a,b=map(int,input().split())
	arr[a]=b	
	m=b
	mi=a
	for i in range(n-1):
		a,b=map(int,input().split())
		if(b>m):
			m=b
			mi=a
		if a in arr:
			if(arr[a]<b):
				arr[a]=b
		else:
			arr[a]=b
	arr[mi]=0
	s=m+max(arr.values())
	print(s)
		
	


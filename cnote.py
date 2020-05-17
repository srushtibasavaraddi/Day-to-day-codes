t=int(input())
for j in range(t):
	x,y,k,n=map(int,input().split())
	arr=[]
	v=2
	for i in range(n):
		t=[int(v) for v in input().split()]
		arr.append(t)
	f=0
	if(x>y):
		r=x-y
		for i in range(n):
			if((arr[i][0]>=r) and (arr[i][1]<=k)):
				f=1
				break
	else:
		f=1
	
	if(f==1):
		print("LuckyChef")
	else:
		print("UnluckyChef")

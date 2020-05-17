t=int(input())
while(t>0):
	t=t-1
	r=int(input())
	arr=[int(r) for r in input().split()]
	d=arr[1]-arr[0]
	ans=[]
	ans.append(arr[0])
	for i in range(1,r):
		ans.append(ans[i-1]+d)
	diff=0
	for i in range(r):
		if(ans[i]!=arr[i]):
			diff=diff+1
	if(diff<=1):
		for i in range(r):
			print(ans[i],end=" ")
		print()
	else:
		d=arr[r-1]-arr[r-2]
		i=r-2
		ans[r-1]=arr[r-1]
		while(i>=0):
			ans[i]=ans[i+1]-d
			i=i-1
		for i in range(r):
			print(ans[i],end=" ")
		print()


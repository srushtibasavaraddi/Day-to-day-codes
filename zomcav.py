import math
t=int(input())
while(t):
	t=t-1
	n=int(input())
	rp=[int(n) for n in input().split()]
	zh=[int(n) for n in input().split()]
	zhs=0
	ans=0
	for i in range(n):
		zhs=zhs+zh[i]	
		l=(i+1)-rp[i]
		r=(i+1)+rp[i]
		if(l<=0):
			l=1
		if(r>n):
			r=n	

		ans=ans+(r-l)+1
	
	if(zhs==ans):
		print("YES")
	else:
		print("NO")
	


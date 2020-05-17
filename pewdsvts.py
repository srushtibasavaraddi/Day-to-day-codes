import math
import heapq
t=int(input())
while(t>0):
	t=t-1
	n,a,b,x,y,z=map(int,input().split())
	arr=[-int(n) for n in input().split()]
	dh=math.ceil((z-b)/y) 
	m=a+(dh-1)*x
	need=z-m
	extra=0
	z=heapq.heapify(arr)
	c=0
	r=0
	while(extra<need):
		if(arr[0]==0):
			r=1
			break
		temp=heapq.heappop(arr)
		extra=extra-temp
		heapq.heappush(arr,math.ceil(temp/2))
		c=c+1
	if(r):
		print("RIP")
	else:
		print(c)


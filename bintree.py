N=int(input())
import math
c=0

for k in range(N):
	i,j=map(int,input().split())
	c=0
	while(i!=j):
		if(i>j):
			i=i//2
			c=c+1
		else:
			j=j//2
			c=c+1
	print(c)


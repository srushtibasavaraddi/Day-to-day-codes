n,c=map(int,input().split())
import math
import sys
x=math.floor(math.sqrt(n))
m=x*x
i=1
flag=0
while(i<=x):
	print("1",i*x)
	sys.stdout.flush()
	a=int(input())
	if(a==0):
		i=i+1
		flag=0
	elif(a==1):
		print("2")
		flag=1
		break
		

if(flag==0):
	j=m+1
	k=n
else:
	j=(i-1)*x+1
	k=i*x
	
while(j<=k):
	print("1",j)
	a=int(input())
	if (a==0):
		j=j+1
	elif(a==1):
		print("2")
		print("3",j)
		break		

 


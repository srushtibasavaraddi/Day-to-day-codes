t=int(input())
while(t>0):
	t=t-1
	n=int(input())
	o=input()
	d=input()
	c1=0
	c2=0
	for i in range(n):
		if(o[i]!=d[i]):
			if(o[i]=="1"):
				c1=c1+1
			else:
				c2=c2+1
	if(c1==c2):
		print("YES")
	else:
		print("NO")	


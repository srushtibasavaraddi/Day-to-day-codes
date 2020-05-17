t=int(input())
while(t):
	t=t-1
	l,r,g=map(int,input().split())
	x1=l%g
	if(x1==0):
		b1=l//g
	else:
		x=g-x1
		b1=(l+x)//g
	x=r%g
	b2=(r-x)//g
	temp=b2-b1+1
	if(temp==1 and b2!=1):
		print("0")
	else:
		print(b2-b1+1)

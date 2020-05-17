t=int(input())
while(t):
	t-=1
	n,p=map(int,input().split())
	if((n!=1) and (n!=2)):
		sno=(n//2)-1
		ss=(10+((sno-1)*2))
		ss=ss/2
		ss=ss*sno
		ut=int(4+ss)
		nn=n
		if(n%2!=0):
			nn=n-1
		nn=nn//2
		a=(3*(nn+2))
		diff=p-n
		ss=(2*a+((diff-1)*6))
		ss=ss/2
		ss=ss*diff
		m=int(ut+ss)
		print(m)
	else:
		if(n==1):
			diff=p-n+1
			ss=diff*diff*diff
			print(ss)
		else:
			diff=p-n+2
			ss=diff*diff*diff
			print(ss)
		
		

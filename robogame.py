t=int(input())
while(t):
	t-=1
	s=input()
	l=len(s)
	v=[0]*l
	flag=0
	i=0
	while(i<l and flag==0):
		if s[i]!='.':
			st=i-int(s[i])
			if st<0:
				st=0
			ep=i+int(s[i])
			if ep>=l:
				ep=l-1
			for j in range(st,ep+1):
				if(v[j]==1):
					flag=1
					break
				else:
					v[j]=1
		i+=1
	if flag==1:
		print("unsafe")
	else:
		print("safe")		
				
					
		

n=50
marked=[0 for i in range(n+1)]
p=2
while(p*p<=n):
	if(marked[p]==0):
		for j in range(p*p,n+1,p):
			marked[j]=1
	p+=1
	
for i in range(2,n+1):
	if(marked[i]==0):
		print(i)

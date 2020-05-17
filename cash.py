t=int(input())
while(t):
	t=t-1
	n,k=map(int,input().split())
	arr=[int(n) for n in input().split()]
	narr=[arr[i]%k for i in range(n)]
	darr=[]
	for i in range(n):
		if(narr[i]!=0):
			darr.append(abs(k-narr[i]))
		else:
			darr.append(0)
	#print(narr)
	#print(darr)
	
	pn=[narr[0]]
	
	darr=darr[::-1]
	pd=[darr[0]]
	for i in range(1,n):
		pn.append(pn[i-1]+narr[i])
		pd.append(pd[i-1]+darr[i])
	pd=pd[::-1]
	#print(pn)
	#print(pd)
	r=99999999999
	for i in range(n-1):
		if(pn[i]>=pd[i+1]):
			if((pn[i]-pd[i+1])<r):
				r=pn[i]-pd[i+1]
	if(r==99999999999):
		print(pn[n-1])
	else:
		print(r)

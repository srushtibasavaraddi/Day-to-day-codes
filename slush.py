t=int(input())
while(t>0):
	t=t-1
	n,m=map(int,input().split())
	s=0
	arr=[]
	arrm=[int(m) for(m) in input().split()]
	for i in range(n):
		d,v,c=map(int,input().split())
		if(arrm[d-1]!=0):
			s=s+v
			arr.append(d)
			arrm[d-1]=arrm[d-1]-1
		else:
			s=s+c
			arr.append(0)	
	print(s)
	arr1=[]
	for i in range(m):
		if(arrm[i]!=0):
			arr1.append([i+1,arrm[i]])	
	j=0
	for i in range(n):
		if(arr[i]==0):
			arr[i]=arr1[j][0]
			arr1[j][1]=arr1[j][1]-1
			if(arr1[j][1]==0):
				j=j+1		
		print(arr[i],end=" ")
		
	


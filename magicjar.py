t=int(input())
while(t):
	t-=1
	n=int(input())
	arr=[int(n) for n in input().split()]
	s,c=0,0
	for i in range(n):
		if (arr[i]!=1):
			s+=arr[i]
			c+=1
	print(s-c+1)	


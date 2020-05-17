def sum(n):
	s=0
	while(n!=0):
		t=n%10
		s=s+t
		n=n//10
	return s
	
t=int(input())
while(t):
	mp=0
	t=t-1
	n=int(input())
	arr=[int(n) for n in input().split()]
	for i in range(n-1):
		for j in range(i+1,n):
			tmp=sum(arr[i]*arr[j])
			if(tmp>mp):
				mp=tmp
	print(mp)

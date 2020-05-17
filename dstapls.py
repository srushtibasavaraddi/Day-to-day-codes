t=int(input())
while(t):
	t=t-1
	n=int(input())
	parr=[int(n) for n in input().split()]
	farr=[int(n) for n in input().split()]
	m=0
	for i in range(n):
		temp=parr[i]*20-farr[i]*10
		if(temp>m):
			m=temp
	if(m>0):	
		print(m)
	else:
		print("0")

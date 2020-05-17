t=int(input())
while(t):
	t=t-1
	n=int(input())
	arr=[int(n) for n in input().split()]
	ans=0	
	for i in range(n):
		temp=arr[i]	
		for j in range(i+1,n):
			temp=temp^arr[j]
			if(temp==0):
				ans=ans+(j-i)
	print(ans)
			


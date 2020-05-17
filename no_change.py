t=int(input())
while(t):
	t=t-1
	n,p=map(int,input().split())
	arr=[int(n) for n in input().split()]
	narr=[0 for i in range(n)]
	f=0
	for i in range(n):
		if(p<arr[i]):
			narr[i]=1
			f=1
			break
		if(p%arr[i]!=0):
			x=p//arr[i]
			narr[i]=x+1
			f=1
			break
	#print("f",f)		
	if(f==0):
		for i in range(n-1):
			if(arr[i+1]%arr[i]!=0):
				x=p//arr[i+1]
				if(p%arr[i+1]==0):
					x=x-1
				y=p-(x*arr[i+1])
				y=y//arr[i]
				narr[i+1]=x
				narr[i]=y+1
				f=1
				break
	if(f==1):
		print("YES",end=" ")
		print(*narr,end=" ")
		print()
	else:
		print("NO")
	
	
			
								
				

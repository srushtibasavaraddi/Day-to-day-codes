t=int(input())
while(t):
	t=t-1
	n,k,p=map(int,input().split())
	arr=[int(n) for n in input().split()]
	if(k%2!=0):	
		if(p==0):
			print(max(arr))
		else:
			print(min(arr))
	else:
		if(p==0):
			x=arr[1]
			if(arr[n-2]>x):
				x=arr[n-2]
			for i in range(1,n-1):
				x2=arr[i-1]
				if(x2>arr[i+1]):
					x2=arr[i+1]
				if(x2>x):
					x=x2
			print(x)
		else:
			x=arr[1]
			if(arr[n-2]<x):
				x=arr[n-2]
			for i in range(1,n-1):
				x2=arr[i-1]
				if(x2<arr[i+1]):
					x2=arr[i+1]
				if(x2<x):
					x=x2
			print(x)
			

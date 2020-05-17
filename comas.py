t=int(input())
import sys
while(t):
	arr=[]
	t=t-1
	n=int(input())
	i=0
	x=(n//5 * 5)-5
	while(i<n):
		if i<=x:
			print("?",i+1,i+2,i+3,i+4,i+5)
			sys.stdout.flush()
			a,b=map(int,input().split())
			j=i
			while(j<i+5):
				if(j+1==a or j+1==b):
					arr.append(0)
				else:
					arr.append(1)
				j=j+1
			i=i+5
		else:
			arr.append(1)
			i=i+1	
	ones=0
	arr1=[]
	for i in range(n):
		if(arr[i]==1):
			arr1.append(i+1)
			ones=ones+1	
	while(ones>4):
		i=0
		while(i+5<=ones):
			print("?",arr1[i],arr1[i+1],arr1[i+2],arr1[i+3],arr1[i+4])
			sys.stdout.flush()
			c=b
			a,b=map(int,input().split())
			arr[a-1]=0
			arr[b-1]=0
			i=i+5
		ones=0
		arr1=[]
		for i in range(n):
			if(arr[i]==1):
				arr1.append(i+1)
				ones=ones+1	
			
	arr2=[]	
	if(len(arr1)==4):
		print("?",arr1[0],arr1[1],arr1[2],arr1[3],a)
		sys.stdout.flush()
		p,q=map(int,input().split())
		for i in range(4):
			if arr1[i]!=p and arr1[i]!=q:
				arr2.append(arr1[i])
		if p in arr1:
			c=p
		else:
			c=q
		print("?",arr2[0],arr2[1],a,b,c)
		sys.stdout.flush()
		a1,b1=map(int,input().split())
		
					
		print("?",arr2[2],arr2[1],a,b,c)
		sys.stdout.flush()
		a2,b2=map(int,input().split())
					
		print("?",arr2[0],arr2[2],a,b,c)
		sys.stdout.flush()
		a3,b3=map(int,input().split())
		
		if(a1==a2 and b1==b2):
			print("!",arr2[1])
		elif(a1==a3 and b1==b3):
			print("!",arr2[0])
		else:
			print("!",arr2[2])	
			
	else:
		print("?",arr1[0],arr1[1],a,b,c)
		sys.stdout.flush()
		a1,b1=map(int,input().split())
		
					
		print("?",arr1[2],arr1[1],a,b,c)
		sys.stdout.flush()
		a2,b2=map(int,input().split())
					
		print("?",arr1[0],arr1[2],a,b,c)
		sys.stdout.flush()
		a3,b3=map(int,input().split())
		
		if(a1==a2 and b1==b2):
			print("!",arr1[1])
		elif(a1==a3 and b1==b3):
			print("!",arr1[0])
		else:
			print("!",arr1[2])	
				
			
			
			
			
			
			
			

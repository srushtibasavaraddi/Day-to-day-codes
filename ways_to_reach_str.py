import copy

def ways(n):
	global arr
	arr=[0 for i in range(n+1)]
	arr[0]=1
	for i in range(3,n+1):
		arr[i]=arr[i-3]+arr[i]
	#print(arr)
	for i in range(5,n+1):
		arr[i]=arr[i-5]+arr[i]
	#print(arr)
	for i in range(10,n+1):
		arr[i]=arr[i-10]+arr[i]
	print(arr)
n=int(input())
ways(n)

def subs(arr):
	gen=[[] for i in range(n+1)]
	print(gen)
	arr[0]=0
	for i in range(3,n+1):
		if(i==3):
			gen[i]=[[3]]
		if(i==5):
			gen[i]=[[5]]
		if(i==10):
			gen[i]=[[10]]
		if(((i-3)>=0) and (arr[i-3]>0)):
			temp=copy.deepcopy(gen[i-3])
			
			for j in range(len(temp)):
				temp[j].append(3)
			gen[i]=gen[i].append(temp)
		elif(((i-5)>=0) and (arr[i-5]>0)):
			temp=copy.deepcopy(gen[i-5])
			for j in range(len(temp)):
				temp[j].append(5)
			gen[i]=gen[i].append(temp)
		elif(((i-10)>=0) and (arr[i-10]>0)):
			temp=copy.deepcopy(gen[i-10])
			for j in range(len(temp)):
				temp[j].append(10)
			gen[i]=gen[i].append(temp)
			
			
		print(gen)
		
subs(arr)



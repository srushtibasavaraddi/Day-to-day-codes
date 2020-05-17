t=int(input())
while(t>0):
	t=t-1
	arr={}
	n=int(input())
	for i in range(n):	
		s=input()
		for i in s:
			if (i=='c' or i=='o' or i=='d' or i=='e' or i=='h' or i=='f'):
				if i in arr:
					arr[i]=arr[i]+1
				else:
					arr[i]=1

	if 'c' in arr:
		arr['c']=arr['c']//2
	if 'e' in arr:	
		arr['e']=arr['e']//2
	if(arr and len(arr)==6):
	 	print(min(arr.values()))
	else:
		print("0")

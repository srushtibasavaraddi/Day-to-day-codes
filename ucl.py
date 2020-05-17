t=int(input())
while(t):
	t=t-1
	arr={}	
	for i in range(12):
		s=input().split()
		x=int(s[1])-int(s[3])
		if s[0] in arr:
			arr[s[0]][1]=arr[s[0]][1]+int(s[1])-int(s[3])			
			if(x>0):
				arr[s[0]][0]=arr[s[0]][0]+3
			elif(x==0):
				arr[s[0]][0]=arr[s[0]][0]+1
		else:
			arr[s[0]]=[0,0]
			arr[s[0]][1]=int(s[1])-int(s[3])
			if(x>0):
				arr[s[0]][0]=3
			elif(x==0):
				arr[s[0]][0]=1

		x=int(s[3])-int(s[1])
		if s[4] in arr:
			arr[s[4]][1]=arr[s[4]][1]+int(s[3])-int(s[1])			
			if(x>0):
				arr[s[4]][0]=arr[s[4]][0]+3
			elif(x==0):
				arr[s[4]][0]=arr[s[4]][0]+1
		else:
			arr[s[4]]=[0,0]
			arr[s[4]][1]=int(s[3])-int(s[1])
			if(x>0):
				arr[s[4]][0]=3
			elif(x==0):
				arr[s[4]][0]=1
	mp=-1		
	for i in arr:
		if(arr[i][0]>mp):
			mp=arr[i][0]
			w1=i
		if(arr[i][0]==mp):
			if(arr[w1][1]<arr[i][1]):
				w1=i
	arr[w1][0]=-2	
	mp=-1		
	for i in arr:
		if(arr[i][0]>mp):
			mp=arr[i][0]
			w2=i
		if(arr[i][0]==mp):
			if(arr[w2][1]<arr[i][1]):
				w2=i
	print(w1,w2)		
		
		
		


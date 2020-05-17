n,q=map(int,input().split())
arr=[int(n) for n in input().split()]
marr=[0]
mirr=[0]
f=0
max_arr=[0]
inc=[0]
dec=[0]
lc=0
min_arr=[0]
for i in range(1,n):
	if(arr[i]>arr[i-1]):
		#print("index",i)
		if(f==0):
			marr.append(marr[i-1]+1)
		else:
			marr.append(marr[i-1])
		f=1
	else:
		marr.append(marr[i-1])
		f=0
		
		
	if(arr[i]>arr[i-1]):
		inc.append(inc[i-1]+1)
	else:
		inc.append(inc[i-1])
	if(i==(n-1)):
	
		if(arr[i]>arr[i-1]):
			if(inc[i]-inc[lc]==(i-lc)):
				max_arr.append(max_arr[i-1]+1)
			else:
				max_arr.append(max_arr[i-1])
		else:
			max_arr.append(max_arr[i-1])
	else:
		if((arr[i]>arr[i-1] and arr[i]>arr[i+1]) or (arr[i]<arr[i-1] and arr[i]<arr[i+1])):
			if(inc[i]-inc[lc]==(i-lc)):
				max_arr.append(max_arr[i-1]+1)
			else:
				max_arr.append(max_arr[i-1])
			lc=i
		else:
			max_arr.append(max_arr[i-1])
			
			
#min
	
lc=0
f=0

for i in range(1,n):
	if(arr[i]<arr[i-1]):
		#print("index",i)
		if(f==0):
			mirr.append(mirr[i-1]+1)
		else:
			mirr.append(mirr[i-1])
		f=1
	else:
		mirr.append(mirr[i-1])
		f=0		
		
	if(arr[i]<arr[i-1]):
		dec.append(dec[i-1]+1)
	else:
		dec.append(dec[i-1])
	if(i==(n-1)):
		if(arr[i]<arr[i-1]):
			#print(inc,lc)
			if(dec[i]-dec[lc]==(i-lc)):
				min_arr.append(min_arr[i-1]+1)
			else:
				min_arr.append(min_arr[i-1])
		else:
			min_arr.append(min_arr[i-1])
	else:
		if((arr[i]<arr[i-1] and arr[i]<arr[i+1]) or (arr[i]>arr[i-1] and arr[i]>arr[i+1])):
			if(dec[i]-dec[lc]==(i-lc)):
				min_arr.append(min_arr[i-1]+1)
			else:
				min_arr.append(min_arr[i-1])
			lc=i
		else:
			min_arr.append(min_arr[i-1])	
			
			
#print(marr,max_arr)
for i in range(q):			
	l,r=map(int,input().split())
	ma=marr[r-1]-max_arr[l-1]
	mi=mirr[r-1]-min_arr[l-1]
	#print(ma,mi)
	if(ma==mi):
		print("YES")
	else:
		print("NO")





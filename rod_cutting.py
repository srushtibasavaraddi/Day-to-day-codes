def rod_cutting(l):
	arr=[0 for i in range(l+1)]
	for i in range(2,l+1):
		for j in range(1,i//2+1):
			arr[i]=max((j*(i-j)),(j*arr[i-j]),arr[0])
	
	print(arr)

rod_cutting(7)

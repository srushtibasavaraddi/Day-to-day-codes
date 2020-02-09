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


	

arr=[5,11,3,15,30,25]
n=len(arr)
def longest_increasing_subsequesnce(arr,n):
	tarr=[1 for i in range(n)]
	for i in range(1,n):
		for j in range(0,i):
			if((arr[i]>arr[j]) and ((tarr[j]+1)>tarr[i])):
				tarr[i]=tarr[j]+1
	return tarr

print(longest_increasing_subsequesnce(arr,n))

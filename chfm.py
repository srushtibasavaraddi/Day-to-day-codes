t=int(input())
import statistics
while(t>0):
	t=t-1
	n=int(input())
	arr=[int(n) for n in input().split()]
	m=statistics.mean(arr)
	try:
		temp=arr.index(m)
		print(temp+1)
	except:
		print("Impossible")

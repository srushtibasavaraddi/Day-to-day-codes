t=int(input())
while(t):
	t=t-1
	n=int(input())
	arr1=[int(n) for n in input().split()]
	arr2=[int(n) for n in input().split()]
	arr1.sort()
	arr2.sort()
	s=0
	for i in range(n):
		s=s+min(arr1[i],arr2[i])
	print(s)

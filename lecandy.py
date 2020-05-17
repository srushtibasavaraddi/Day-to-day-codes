t=int(input())
while(t):
	t=t-1
	n,c=map(int,input().split())
	arr=[int(n) for n in input().split()]
	av=0
	for i in range(n):
		av=av+arr[i]
	if(av<=c):
		print("Yes")
	else:
		print("No")

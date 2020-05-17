arr=[1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404]

t=int(input())
while(t):
	ll=-1
	sl=-1
	t=t-1
	l,r=map(int,input().split())
	for i in range(len(arr)):
		if(arr[i]>=l and arr[i]<=r):
			sl=i
			break
	for i in range(len(arr)-1,-1,-1):
		if(arr[i]>=l and arr[i]<=r):
			ll=i
			break
	
	#print(ll,sl)
	if(ll==-1 and sl==-1):
		print(0)
	else:	
		print(ll-sl+1)

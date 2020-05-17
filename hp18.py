t=int(input())
while t:
	t-=1
	n,b,a=map(int,input().split())
	arr=[int(n) for n in input().split()]
	amul,bmul,cmul=0,0,0
	for i in range(n):
		if ((arr[i]%a==0) and (arr[i]%b==0)):
			cmul+=1
		elif arr[i]%a==0:
			amul+=1
		elif arr[i]%b==0:
			bmul+=1

	if ((amul<=bmul) and (cmul!=0)):
		print("BOB")
	elif(cmul==0):
		if amul<bmul:
			print("BOB")
		else:
			print("ALICE")
	else:
		print("ALICE")

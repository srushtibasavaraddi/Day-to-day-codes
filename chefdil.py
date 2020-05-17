t=int(input())
while(t):
	t=t-1
	s=input()
	l=len(s)
	m=1
	temp=0
	for i in s:
		if(i=="1"):
			temp=temp+1
	if(temp%2==0):
		print("LOSE")
	else:
		print("WIN")


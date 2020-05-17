t=int(input())
while(t):
	t=t-1
	day=[]
	ques=[]
	d=int(input())
	for i in range(d):
		a,b=map(int,input().split())
		day.append(a)
		ques.append(b)
	q=int(input())
	while(q):
		q=q-1
		a,b=map(int,input().split())
		s=0
		i=0
		while(i<d and day[i]<=a ):
			s=s+ques[i]
			i=i+1
			if i<d:
				continue
			else:
				break
		if s>=b:
			print("Go Camp")
		else:
			print("Go Sleep")
	

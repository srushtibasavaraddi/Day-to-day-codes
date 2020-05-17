t1=int(input())
while(t1):
	t1=t1-1
	n=int(input())
	grid=[[int(n) for n in input()] for n in range(n)]
	arr=[]
	pl=0
	pr=0
	tpl=0
	tpr=0
	x=0
	for i in range(n):
		for j in range(n):
			if(grid[i][j]==1):
				if(j<n//2):
					pl=pl+1
				else:
					pr=pr+1
		
		nl=pl-tpl
		nr=pr-tpr
		tpl=pl
		tpr=pr
		arr.append((nr-nl)*2)
	a=abs(pr-pl)
	if(a==0):
		print("0")
	else:
		for i in range(n):
			tpl=pl+arr[i]
			ta=abs(tpl-pr)
			if(ta==0):
				x=1	
				break
			if(ta<a):
				a=ta
		if(x==1):
			print("0")	
		else:
			print(a)
			
		


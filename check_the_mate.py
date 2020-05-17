n=int(input())
wp=[]
for i in range(n):
	wp.append([int(n) for n in input().split()])
#print(wp)
engaged_m=[0 for i in range(n)]
engaged_f=[0 for i in range(n)]
for i in range(n):
	for j in range(n):
		if((wp[i][j]!=-1) and (engaged_m[wp[i][j]-1]==0)):
			engaged_m[wp[i][j]-1]=1
			break
c=0
for i in range(n):
	if(engaged_m[i]==0):
		print(i+1)
	else:
		c=c+1
if(c==n):
	print(-1)	

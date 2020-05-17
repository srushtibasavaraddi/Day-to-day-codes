n=int(input())
mp=[]
for i in range(n):
	mp.append([int(n) for n in input().split()])
	
t=[]
for i in range(n):
	t.append([int(n) for n in input().split()])

fp=[[0 for i in range(n)] for j in range(n)]
for i in range(n):
	for j in range(n):
		fp[i][j]=t[j][i]
#print(fp)
engaged_m=[-1 for i in range(n)]
engaged_f=[-1 for i in range(n)]
p=[0 for i in range(n)]
rl=[[] for i in range(n)]
i=0
def propose(wi,mi):
	p[wi]=p[wi]+1
	if(engaged_f[wi]==-1):
		return 1,1
	elif(fp[wi][mi]<fp[wi][engaged_f[wi]]):
		return 1,0
	return 0,0
while(True):
	r=0
	#print("i",i)
	for pc in range(1,n+1):
		#print("pc",pc)
		for j in range(n):
			if(j in rl[i]):
				continue
			if(mp[i][j]==pc):
				r,s=propose(j,i)
				rl[i].append(j)
				if(r==1):
					
					if(s==0):
						x=engaged_f[j]
						engaged_m[x]=-1
					engaged_f[j]=i
					engaged_m[i]=j
					break
		if(r==1):
			break
	c=0
	for j in range(n):
		if(engaged_m[j]==-1):
			i=j
			break
		else:
			c=c+1
	#print(engaged_m,engaged_f)
	if(c==n):
		break
print(p)
q=int(input())

while(q):
	q=q-1
	x=int(input())
	print(p[x-1])
	
	

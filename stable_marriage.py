n=4
mp=[[1,2,3,4],[2,1,3,4],[1,2,4,3],[3,2,1,4]]
fp=[[4,3,2,1],[2,3,1,4],[1,2,4,3],[3,2,1,4]]
engaged_m=[-1 for i in range(n)]
engaged_f=[-1 for i in range(n)]

i=0
def propose(wi,mi):
	if(engaged_f[wi]==-1):
		return 1,1
	elif(fp[wi][mi]<fp[wi][engaged_f[wi]]):
		return 1,0
	return 0,0
while(True):
	r=0
	print("i",i)
	for pc in range(1,n+1):
		print("pc",pc)
		for j in range(n):
			if(mp[i][j]==pc):
				r,s=propose(j,i)
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
	print(engaged_m,engaged_f)
	if(c==n):
		break
	

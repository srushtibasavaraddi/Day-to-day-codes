n=3
mp=[[2,1,3],[3,1,2],[3,2,1]]
fp=[[3,1,2],[2,3,1],[3,1,2]]
engaged_m=[-1 for i in range(n)]
engaged_f=[-1 for i in range(n)]

i=0
while(True):
	if(engaged_m[i]==-1):
		#print("i",i)
		m=n+1	
		mi=-2
		for j in range(n): 		
			if((engaged_f[j]==-1) or (fp[j][i]<fp[j][engaged_f[j]])):
				#print("j",j)
				if(mp[i][j]<m):
					m=mp[i][j]
					mi=j
			#print("mi",mi,m)
		engaged_m[i]=mi
		if(engaged_f[mi]!=-1):
			x=engaged_f[mi]
			engaged_m[x]=-1
				
		engaged_f[mi]=i
		c=0
		for j in range(n):
			if(engaged_m[j]==-1):			
				i=j
				break
			else:
				c=c+1
		'''
		for j in range(n):
			print(engaged_m[j],engaged_f[j])
		'''
		if(c==3):
			break
		
print(engaged_m)
				

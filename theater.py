from itertools import permutations

df="ABCD"
df2=[12,3,6,9]
t=int(input())
st=0
while(t):
	t=t-1
	comb=permutations([0,1,2,3])
	n=int(input())
	arr=[[0 for i in range(4)] for i in range(4)]
	while(n):
		n=n-1
		m,sh=map(str,input().split())
		i=df.index(m)
		j=df2.index(int(sh))
		arr[i][j]=arr[i][j]+1
	#print(arr)
	m=-500
	for i in comb:
		w=[]
		w.append(arr[0][i[0]])
		w.append(arr[1][i[1]])
		w.append(arr[2][i[2]])
		w.append(arr[3][i[3]])
		#print(i)
		#print("w",w)
		
		w.sort()
		c=w.count(0)
		w[0]=w[0]*25
		w[1]=w[1]*50
		w[2]=w[2]*75
		w[3]=w[3]*100
		s=sum(w)
		#print("s",s)
		#print("m",m)
		s=s-(100*c)
		if(s>m):
			m=s
	print(m)	
	st=st+m
print(st)		



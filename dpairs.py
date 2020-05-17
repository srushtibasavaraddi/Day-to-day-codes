n,m=map(int,input().split())
arrn=list(map(int,input().split()))
arrm=list(map(int,input().split()))
nmin=arrn[0]
imin=0
for i in range(1,n):
	if arrn[i]<nmin:
		nmin=arrn[i]
		imin=i
		
for i in range(m):
	print(imin,i)
mmax=arrm[0]
imax=0
for i in range(1,m):
	if arrm[i]>mmax:
		mmax=arrm[i]
		imax=i

for i in range(n):
	if(i!=imin):
		print(i,imax)

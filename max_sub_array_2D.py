def kadane(arr,n):
    tmax=0
    m=-10000000        
    p=0
    for i in range(n):
        tmax=tmax+arr[i]
        if(m<tmax):
            m=tmax
            start=p
            end=i
        if(tmax<0):
            tmax=0
            p=i+1
    return m,start,end

r,c=map(int,input().split())
arr=[[int(c) for c in input().split()] for i in range(r)]

Max= -10000000
for L in range(c):
	temp=[0 for i in range(r)]
	for R in range(L,c):
		for i in range(r):
			temp[i]+=arr[i][R]
		cMax,tmaxUp,tmaxDown=kadane(temp,r)
		#print(cMax)
		if(cMax>Max):
			Max=cMax
			maxUp=tmaxUp
			maxDown=tmaxDown
			maxLeft=L
			maxRight=R
			
print(Max)					

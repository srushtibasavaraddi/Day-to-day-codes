def ways(n,coin):
    arr=[0 for i in range(n+1)]
    arr[0]=1
    for j in coin:
        for i in range(j,n+1):
            arr[i]=arr[i-j]+arr[i]
    print(arr[-1])
	
n,nc=map(int,input().split())
coin=[int(nc) for nc in input().split() ]
ways(n,coin)


	
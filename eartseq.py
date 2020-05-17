n=620000
i=2
visited=[0]*n
visited[0]=1
prime_arr=[]
while(i*i<=n):
	j=i*i
	while(j<=n):
		visited[j-1]=1
		j+=i
	i+=1


for i in range(n):
	if(visited[i]==0):
		prime_arr.append(i+1)
uarr=[2,3,5]
j=4
for i in range(3,50000):
	if(i%2==0):
		uarr.append(prime_arr[j])
		j+=1
	elif((i+1)%4==0):
		uarr.append(7)
	else:
		uarr.append(5)
		
t=int(input())
while(t):
	t-=1
	n=int(input())
	print(uarr[0]*uarr[n-1],end=" ")
	for i in range(n-1):
		print(uarr[i]*uarr[i+1],end=" ")
	print()	
		
		

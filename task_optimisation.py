M=[[3,2,7],[5,1,3],[2,7,2]]
n=3
import math

dp=[math.inf for i in range((int(math.pow(2,n))))]
for i in range(int(math.pow(2,n))):
	x=bin(i)[2:].count("1")
	#i is the mask
	for j in range(n):
		if((i & 1<<j)==0):	
			dp[i|(i<<j)]=min(dp[i]+M[x][j])
			
print(dp)

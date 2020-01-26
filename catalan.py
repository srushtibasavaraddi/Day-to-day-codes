cat=[1,1]
n=10
for i in range(2,n):
	cat.append(0)
	for j in range(i):
		cat[i]=cat[i]+cat[j]*cat[i-1-j]
print(cat)

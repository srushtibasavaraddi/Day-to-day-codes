def LCS(s1,s2):
	l1,l2=len(s1),len(s2)
	arr=[[0 for i in range(l2+1)] for j in range(l1+1)]
	for i in range(1,l1+1):
		for j in range(1,l2+1):
			if(s1[i-1]==s2[j-1]):
				arr[i][j]=arr[i-1][j-1]+1
			else:
				arr[i][j]=max(arr[i][j-1],arr[i-1][j])
	
	#print(arr)
	return arr[l1][l2]

LCS("abcda","bdabac")
	

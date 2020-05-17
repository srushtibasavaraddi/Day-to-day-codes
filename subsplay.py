t=int(input())
while(t):
	t=t-1
	n=int(input())
	s=input()
	dic={}
	a=n
	for i in range(n):
		if s[i] in dic:
			tt=i-dic[s[i]]
			dic[s[i]]=i
			if(tt<a):
				a=tt
		else:
			dic[s[i]]=i
	print(n-a)

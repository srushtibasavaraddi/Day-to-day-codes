from itertools import combinatations

def modulo_multiplicative_inverse(A, M):
    gcd, x, y = ggcd(A, M)
    if x < 0:
        x += M
    
    return x

def ggcd(a, b):
    s = 0; old_s = 1
    t = 1; old_t = 0
    r = b; old_r = a

    while r != 0:
        quotient = old_r//r
        old_r, r = r, old_r - quotient*r
        old_s, s = s, old_s - quotient*s
        old_t, t = t, old_t - quotient*t
    return [old_r, old_s, old_t]

t=int(input())
while(t):
	t=t-1
	n=int(input())
	s=input()
	arr=[i for i in range(n)]
	p=permutations(arr,2)
	change=s.count(")")
	l=0
	for i in p:
		l=l+1
		#print(i)
		c=0
		for j in range(i[0],i[1]+1):
			if(s[j]=="("):
				c=c+1
			if(s[j]==")"):
				c=c-1
				if(c<0):
					change=change+1
					new = list(s)
					new[j] ='('
					s=''.join(new)
		#print(change,c,s)		


	a =l+n
	m=7+1000000000
	x=modulo_multiplicative_inverse(a,m)    
	#print("Modular multiplicative inverse is", x)
	x=change*x
	x=x%m
	print(x) 



   

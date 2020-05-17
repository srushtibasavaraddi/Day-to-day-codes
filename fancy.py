import re
t=int(input())
while t:
	t-=1
	s=input()
	if re.search(r'\bnot\b',s):
		print("Real Fancy")
	else:
		print("regularly fancy")
		

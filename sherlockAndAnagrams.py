def countAnagram(s): 
    n = len(s) 
    d = dict() 
      
    for i in range(n): 
        temp = '' 
        for j in range(i, n): 
            temp = ''.join(sorted(temp + s[j])) 
            d[temp] = d.get(temp, 0) 
            d[temp] += 1
        # print(d)
  
    ans = 0
    for k,v in d.items(): 
        ans += (v*(v-1))//2
    return ans 
n=int(input())
while(n):
    n-=1
    s=input()
    print(countAnagram(s))  


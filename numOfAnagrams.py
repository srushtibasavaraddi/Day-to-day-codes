def countAnagram(s): 
    n = len(s) 
    d = dict() 
      
    for i in range(n): 
        temp = '' 
        for j in range(i, n): 
            temp = ''.join(sorted(temp + s[j])) 
            d[temp] = d.get(temp, 0) 
            d[temp] += 1
        print(d)
  
    ans = 0
    for c in d.values(): 
        ans += (c*(c-1))//2
    return ans 
  
s = "mom"
print(countAnagram(s)) 